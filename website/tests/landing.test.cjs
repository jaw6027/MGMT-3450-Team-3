/* Run from repository root: node website/tests/landing.test.cjs */
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const root = path.resolve(__dirname, '../..');
const artifacts = path.join(__dirname, 'artifacts');
let server, browser;
const pass = name => console.log('PASS', name);
(async () => {
  fs.mkdirSync(artifacts, {recursive: true});
  server = http.createServer((req, res) => {
    let file = path.resolve(root, '.' + new URL(req.url, 'http://localhost').pathname);
    if (!file.startsWith(root + path.sep)) {res.writeHead(403).end(); return;}
    if (file.endsWith(path.sep)) file += 'index.html';
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
    fs.readFile(file, (err, data) => {
      if (err) {res.writeHead(404).end(); return;}
      res.setHeader('Content-Type', ({'.html':'text/html','.js':'application/javascript','.css':'text/css','.svg':'image/svg+xml','.ttf':'font/ttf'})[path.extname(file)] || 'text/plain');
      res.end(data);
    });
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  browser = await chromium.launch({headless: true, executablePath: process.env.CHROMIUM_PATH || '/usr/bin/chromium', args: ['--disable-dev-shm-usage']});
  const ctx = await browser.newContext({viewport: {width: 1440, height: 1000}});
  const external = [], errors = [], failed = [];
  await ctx.route('**/*', route => {
    if (!route.request().url().startsWith(base + '/')) {external.push(route.request().url()); return route.abort();}
    return route.continue();
  });
  const page = await ctx.newPage();
  page.on('pageerror', e => errors.push(e.message));
  page.on('response', r => {if (r.status() >= 400) failed.push(r.url());});
  await page.goto(base + '/website/');
  await page.evaluate(() => document.fonts.ready);
  assert.match(await page.locator('h1').innerText(), /Know the load/);
  assert.match(await page.locator('.principle').innerText(), /An assistant, not a replacement/);
  assert(await page.evaluate(() => document.fonts.check('700 20px "Barlow Condensed"')));
  assert(await page.locator('.masthead img').evaluate(i => i.complete && i.naturalWidth > 0));
  pass('Landing content, approved logo and local brand fonts load');
  assert.equal(await page.locator('#score').innerText(), '71');
  assert.equal(await page.locator('#fuel').innerText(), '$406.15');
  assert.equal(await page.locator('#total-miles').innerText(), '660 mi');
  assert.equal(await page.locator('#per-mile').innerText(), '$2.11');
  pass('Default sample calculation matches payment, fuel and all-mile arithmetic');
  const calc = page.getByRole('button', {name: 'Calculate sample score'});
  await page.locator('[name=deadhead]').fill('600'); await calc.click();
  assert(Number(await page.locator('#score').innerText()) < 71);
  await page.locator('[name=payment]').fill('100000'); await calc.click();
  assert.equal(await page.locator('#score').innerText(), '100');
  await page.locator('[name=payment]').fill('0'); await calc.click();
  assert.equal(await page.locator('#score').innerText(), '1');
  await page.locator('[name=miles]').fill('0'); await calc.click();
  assert.equal(await page.locator('[name=miles]').evaluate(e => e.validity.rangeUnderflow), true);
  assert.equal(await page.locator('#score').innerText(), '1');
  await page.getByRole('button', {name: 'Reset example'}).click();
  await page.waitForFunction(() => document.querySelector('#score').value === '71');
  pass('Deadhead changes score; score stays in 1–100; invalid input blocked; reset restores sample');
  await page.locator('.method summary').click();
  assert.match(await page.locator('.method').innerText(), /not a market benchmark/);
  pass('Formula and excluded real-world factors are available');
  await page.locator('#signup-email').fill('not-an-email');
  await page.getByRole('button', {name:'Try signup preview'}).click();
  assert.equal(await page.locator('#signup-email').evaluate(e => e.validity.typeMismatch), true);
  assert.equal(await page.locator('#signup-status').innerText(), '');
  let submissions = 0;
  page.on('request', () => submissions++);
  await page.locator('#signup-email').fill('dispatcher@example.com');
  await page.locator('#signup-role').selectOption('Independent dispatcher');
  await page.getByRole('button', {name:'Try signup preview'}).click();
  assert.match(await page.locator('#signup-status').innerText(), /Nothing was sent or saved/);
  assert.equal(await page.locator('#signup-email').inputValue(), '');
  assert.equal(await page.evaluate(() => localStorage.length + sessionStorage.length), 0);
  assert.equal(submissions, 0);
  pass('Signup validates email, confirms preview, clears fields, sends no request and saves no data');
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.screenshot({path:path.join(artifacts,'landing-desktop.png'),fullPage:true});
  for (const width of [320, 390, 768, 1024, 1440]) {
    await page.setViewportSize({width, height:900});
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `Overflow at ${width}px`);
  }
  await page.setViewportSize({width:390,height:844});
  await page.screenshot({path:path.join(artifacts,'landing-mobile.png'),fullPage:true});
  pass('No horizontal overflow at 320, 390, 768, 1024 and 1440px');
  await page.getByRole('link', {name:'Content studio'}).click();
  await page.locator('#stats .stat').first().waitFor();
  assert.equal(await page.locator('#stats .stat strong').first().innerText(), '16');
  pass('Content studio link opens the preserved tracker');
  assert.deepEqual(external, []); assert.deepEqual(errors, []); assert.deepEqual(failed, []);
  pass('No third-party requests, failed assets or uncaught JavaScript errors');
  const noJS = await browser.newContext({javaScriptEnabled:false});
  const staticPage = await noJS.newPage(); await staticPage.goto(base + '/website/');
  assert(await staticPage.getByRole('button', {name:'Try signup preview'}).isDisabled());
  pass('Signup stays disabled without JavaScript, preventing accidental form submissions');
  await noJS.close(); await ctx.close();
})().catch(e => {console.error(e);process.exitCode=1;}).finally(async () => {
  if (browser) await browser.close();
  if (server) await new Promise(resolve => server.close(resolve));
});
