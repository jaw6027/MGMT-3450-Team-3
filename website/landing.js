'use strict';
const scoreForm = document.querySelector('#score-form');
function calculate() {
  if (!scoreForm.reportValidity()) return;
  const values = Object.fromEntries(new FormData(scoreForm));
  const total = Number(values.miles) + Number(values.deadhead);
  const fuel = total / 6.5 * Number(values.diesel);
  const perMile = (Number(values.payment) - fuel) / total;
  const score = Math.max(1, Math.min(100, Math.round(perMile / 3 * 99 + 1)));
  const dollars = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'});
  document.querySelector('#score').value = String(score);
  document.querySelector('#score-bar').style.width = `${score}%`;
  document.querySelector('#total-miles').textContent = `${total.toLocaleString('en-US')} mi`;
  document.querySelector('#fuel').textContent = dollars.format(fuel);
  document.querySelector('#per-mile').textContent = dollars.format(perMile);
}
scoreForm.addEventListener('submit', event => { event.preventDefault(); calculate(); });
scoreForm.addEventListener('reset', () => { setTimeout(calculate, 0); });
calculate();
const signup = document.querySelector('#signup-form');
signup.querySelector('button[type="submit"]').disabled = false;
signup.addEventListener('submit', event => {
  event.preventDefault();
  if (!signup.reportValidity()) return;
  document.querySelector('#signup-status').textContent = 'Preview complete. Nothing was sent or saved, and you have not been subscribed. Thank you for exploring ProfitLane.';
  signup.reset();
});
