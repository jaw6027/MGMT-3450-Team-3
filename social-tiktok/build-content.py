"""Regenerate reference calendar and scripts from the curated launch concepts.
Run from social-tiktok/: python3 build-content.py. Does not modify browser data.
"""
from pathlib import Path
from datetime import date, timedelta
import csv, json
ROOT = Path(__file__).resolve().parent
# title, pillar, hook, format, main message, caption, CTA
ideas = [
('AI beside the dispatcher', 'Brand awareness', 'AI should help your dispatch desk—not take it over.', 'Founder to camera', 'Introduce ProfitLane to independent dispatchers; proposed AI system tracking and recommendation-score concepts support human judgment.', 'Meet ProfitLane: proposed assistance for independent dispatchers. Your judgment stays at the center.', 'Follow @profitlane.dispatch for dispatcher education and product updates.'),
('Your load-review routine','Engagement','What do you check before you even discuss the rate?','Question card + talking head','Listen to real workflows before choosing features.','Every dispatcher has a first check. What is yours?','Comment with one check, without sharing private load details.'),
('The miles before the load','Education','That load starts before pickup. Count those miles.','Whiteboard example','Add deadhead to loaded miles before comparing revenue per mile.','The empty miles belong in the conversation too. Fictional example.','Save this total-miles check.'),
('A better filming checklist','Industry tips','A useful load video starts with clean inputs.','Desk checklist','Use fictional load data and clear labels in educational content.','No private rate confirmations needed to teach the basics.','Which input would you explain first?'),
('Revenue is not take-home pay','Education','A $1,200 load does not mean $1,200 in profit.','Calculator close-up','Subtract relevant costs; revenue per mile alone is incomplete.','Revenue first. Costs next. Your final decision last. Fictional figures.','Save the cost checklist.'),
('Build the next cost checklist','Industry tips','Which cost is easiest to leave out?','Checklist draft','Include fuel, tolls, time and allocated operating costs.','Help us build a more useful review checklist.','Suggest one overlooked cost.'),
('One week of questions','Engagement','What did this week leave unanswered?','Comment roundup','Use audience questions to choose the next explanation.','We are listening before adding more concepts.','Leave a question for next week.'),
('Angel and the mission', 'Brand awareness', 'The person at the dispatch desk still makes the call.', 'Casual founder desk interview; identified team introduction if needed', 'Angel introduces his dispatcher-first vision and an authentic explanation of what he would review; approve his approximately eight-year background wording before filming.', 'Meet the purpose behind ProfitLane: support the person making the call.', 'Follow @profitlane.dispatch; what would useful assistance look like at your desk?'),
('Prepare a rate conversation','Industry tips','Before asking for more, organize the reason.','Role-play rehearsal','Use accurate route, timing and cost facts; no guaranteed negotiation outcome.','Facts make a clearer conversation than a random counteroffer.','Write down your three key facts.'),
('Fuel math you can check','Education','How much fuel does this fictional trip actually need?','Whiteboard calculation','Total miles divided by assumed MPG, multiplied by fuel price, estimates fuel cost.','A fuel estimate is only as good as its assumptions. Fictional inputs.','Check your own assumptions before using an estimate.'),
('What changes your fuel estimate?','Engagement','Would you use the same MPG for every trip?','Question + input cards','Vehicle and route assumptions need review.','One estimate cannot describe every truck or route.','Tell us which assumption you revisit.'),
('A score is a starting point', 'Product concept', 'Would you accept a load because a screen says 76?', 'Labeled concept mockup', 'Proposed 1–100 recommendation tool: weight relative to distance, pre-trip deadhead, diesel prices in relevant areas, pallet count and load payment; unvalidated, with no guaranteed outcome.', 'Concept only: Angel’s proposed score supports review, especially for new dispatchers. The dispatcher decides.', 'Explore the proposed score in our concept videos; follow for confirmed product updates.'),
('Design the explanation', 'Product concept', 'What does Angel mean by AI system tracking?', 'Casual founder Q&A with labeled concept cards', 'Explain the intended identification of logistics companies using AI in broker–dispatcher communication so dispatchers can choose whom to work with. Method, accuracy and availability remain unverified.', 'AI system tracking: Angel’s proposed concept, not a working detection demonstration. Questions help shape a clearer explanation.', 'Which part of this proposed concept would you want Angel to explain?'),
('Your three-question review','Engagement','Which of these three checks comes first for you?','Comment-response plan','Invite audience priorities without presenting an acceptance rule.','Miles, time or costs—where do you start?','Comment with your order and why.'),
('Ask before you counter','Industry tips','Before you counter, what do you still need to know?','Two-person broker role-play','Clarify appointment times, accessorial terms and load details before negotiating.','A clearer question can improve your information. No rate outcome is promised.','Save these three questions.'),
('Time belongs in the review','Education','Two loads. Same miles. Different time commitments.','Side-by-side cards','Pickup windows, waiting and delivery timing affect the review.','Mileage does not tell the whole schedule. Fictional comparison.','What timing detail do you always confirm?'),
('The same rate, different trip','Education','Both loads pay $1,200. Would you review them the same way?','Split-screen calculation','Compare revenue across total miles while reviewing costs and time.','Same revenue can hide very different trips. Fictional examples.','Save this comparison for your next review checklist.'),
('Missing information matters','Product concept','What should an assistant do when an input is missing?','Mockup question','Flag unknown inputs instead of presenting certainty.','Concept in development: unknown should stay unknown.','Which missing input should trigger a follow-up?'),
('Walk through the proposed assistant', 'Product concept', 'Here is the idea—not a live product demo.', 'Paper prototype walkthrough', 'Walk through the proposed load recommendation inputs and explain AI system tracking separately; concept-only visuals, no live detection, scoring or booking demonstration.', 'Two proposed concepts. Clear limits. Your judgment. No working dispatch product is demonstrated here.', 'Now: follow for product updates. Once a real product page and demo-request route are approved: explore ProfitLane and request a demo through the profile link.'),
('Make labels readable','Industry tips','Can you read the important part in two seconds?','Overlay rehearsal','Keep concept labels visible and explain assumptions in captions.','Clear wording helps people understand what is real and what is proposed.','Which part would you simplify?'),
('Listen before the next batch','Engagement','What should we explain next: fuel, time or deadhead?','Poll-style question','Let qualified questions shape future education.','Choose a topic for the next recording session.','Comment fuel, time or deadhead.'),
('The dispatcher stays in control', 'Brand awareness', 'What should AI leave to the dispatcher?', 'Casual founder answer + practical checklist', 'Angel explains how dispatcher experience and relationships guide decisions; AI system tracking and the score remain proposed assistance concepts.', 'Made for dispatchers by dispatchers. AI assistance stays in a supporting role.', 'Follow @profitlane.dispatch; tell Angel which decision you would always review yourself.'),
('Build a useful reply video','Engagement','A good question deserves more than a quick reply.','Reply-video storyboard','Answer a real question accurately; do not invent a customer comment.','We are collecting questions for the next explanation.','Ask one specific load-review question.'),
('Three inputs to double-check','Industry tips','Before trusting any summary, check the inputs.','Three-card checklist','Verify total miles, fuel assumptions and schedule; this is not a complete operating checklist.','Better inputs help you ask better questions.','Save these checks and add your own.'),
('What a demo request should explain', 'Product concept', 'Before you request a demo, you should know what is available.', 'Founder update draft', 'Plan a product-exploration and demo CTA only after Angel confirms the actual feature, demo and request route. No business contact details or availability are supplied.', 'Product updates should tell you what you can really try.', 'Now: follow for development updates. Later, after approval and verification: explore the features and request a demo through the real profile link.'),
('Answer a real dispatcher question','Engagement','Let us work through one question from the dispatch desk.','Comment reply; use a genuine approved question','Use a real question with consent or label it as a team prompt.','A practical explanation starts with a specific question.','What would you like us to work through next?'),
('Review useful responses','Engagement','Which explanation helped you ask a better question?','Weekly recap preparation','Measure useful audience feedback without fabricating testimonials.','Your feedback helps shape the next month of education.','Name a topic we should revisit.'),
('Plan next month thoughtfully','Industry tips','Do more views always mean a more useful video?','Analytics worksheet','Compare equal observation windows and qualified responses.','Look beyond reach when reviewing what helped.','Choose one question to test next month.'),
('What we want to learn next', 'Brand awareness', 'What would make AI assistance worth trying for you?', 'Founder recap', 'Recap dispatcher-first education and both proposed concepts; invite qualified product questions to support awareness and potential-customer interest.', 'ProfitLane is in development. Your judgment stays at the center.', 'Follow @profitlane.dispatch for product updates. When a verified page and demo-request route exist, invite viewers to explore ProfitLane and request a demo.'),
('A month of learning','Engagement','What should stay on the calendar next month?','Month-end planning card','Review actual results and choose useful next experiments.','A thoughtful next month starts with what we learned.','Suggest one topic for the next calendar.')
]
post_days = {0,2,4,7,9,11,14,16,18,21,23,25,28}
activities = ['Publish' if i in post_days else ('Review & respond' if i % 7 in (5,6) else 'Prepare & engage') for i in range(30)]
tags = {'Education':'#ProfitLane #TruckDispatch #IndependentDispatcher #LoadPlanning','Industry tips':'#ProfitLane #DispatchTips #TruckDispatch #LoadPlanning','Engagement':'#ProfitLane #TruckDispatch #DispatcherLife','Product concept':'#ProfitLane #DispatchTools #AIassistant #TruckDispatch','Brand awareness':'#ProfitLane #TruckDispatch #SmallBusiness #DispatchTools'}
calendar=[]
for i,(title,category,hook,fmt,msg,caption,cta) in enumerate(ideas):
 calendar.append(dict(day=i+1,date=str(date(2026,11,9)+timedelta(days=i)),activity=activities[i],title=title,category=category,hook=hook,format=fmt,message=msg,caption=caption,hashtags=tags[category],cta=cta))
# Seven filming beats per video: end time, exact spoken words, visual, on-screen text.
# The first beat is a short 2–3 second hook. Timing includes pauses/visual holds.
filming = [
# 1 · Introduction
[
(3, "AI assists. You decide.", "Angel or an identified presenter faces the camera at a stationary desk.", "AI assists. You decide."),
(15, "If you work as an independent dispatcher, you already know a load is more than one number on a screen. There are questions behind the offer.", "Cut to original cards labeled miles, time and payment. Point to each as it is named.", "Miles • Time • Payment"),
(27, "ProfitLane is being developed with independent dispatchers as the primary audience. Independent operators who want to start their own dispatching are welcome too.", "Return to the presenter. Show the primary audience first and the secondary line underneath.", "Independent dispatchers first"),
(40, "Angel's proposed concepts include a load recommendation score and AI system tracking. We will explain their intended purpose, the information involved and their limits.", "Show two simple paper concept cards. Keep the in-development label visible.", "Proposed concepts • In development"),
(52, "Those concepts have not been demonstrated as working features here. A score or a tool still needs the dispatcher's questions, experience and final judgment.", "Keep the presenter in view. Place a human-review card beside the concepts; do not show a fake working dashboard.", "Your questions. Your judgment."),
(62, "This account will combine practical explanations, honest product updates and conversations with Angel. Think of it as a discussion at the dispatch desk.", "Use a relaxed desk shot and a quick cut to a fictional whiteboard example.", "Education + product updates"),
(70, "Follow ProfitLane at profitlane dot dispatch. What would you want help reviewing first?", "Finish on the presenter, then hold the approved logo and handle long enough to read.", "@profitlane.dispatch • Follow for updates")
],
# 2 · Total-mile calculation
[
(3, "Count the miles before pickup.", "Point to an empty route arrow drawn before a pickup pin.", "Before pickup counts too"),
(15, "Here is a fictional offer: twelve hundred dollars for five hundred loaded miles. The pickup is one hundred empty miles away. Let's write everything down.", "Reveal $1,200, 500 loaded miles and 100 deadhead miles on separate cards.", "Fictional example • $1,200 offer"),
(28, "If you divide twelve hundred by five hundred, you get two dollars and forty cents per loaded mile. That calculation leaves out the drive to pickup.", "Write $1,200 ÷ 500 = $2.40 per loaded mile. Briefly circle the separate deadhead card.", "$2.40 per loaded mile"),
(41, "Add the empty miles first. One hundred plus five hundred equals six hundred total miles. Now divide twelve hundred dollars by those six hundred miles.", "Animate 100 + 500 = 600, then place 600 beneath $1,200. Pause for the viewer to read.", "100 + 500 = 600 total miles"),
(54, "That gives two dollars per total mile. The payment has not changed. The denominator has changed because the comparison now includes the miles before pickup.", "Show the two divisions side by side, with labels for loaded miles and total miles.", "$1,200 ÷ 600 = $2.00/total mile"),
(66, "Neither number is profit. Fuel, tolls, operating costs and the schedule still need review. Also check what other empty travel belongs in your own comparison.", "Replace the calculator with a short checklist. Keep fictional-example labeling visible.", "Revenue per mile ≠ profit"),
(75, "Save this total-mile check. Before comparing your next offer, ask: which miles did I leave out?", "Return to the presenter and hold the completed 600-mile equation beside them.", "Save the check • What miles are missing?")
],
# 3 · Cost breakdown
[
(3, "Payment is not take-home pay.", "Hold a $1,200 payment card beside an empty expense list.", "Payment ≠ take-home pay"),
(18, "Let's use a fictional twelve-hundred-dollar load. These figures are made up for teaching. They are not typical industry costs, customer results or a ProfitLane calculation.", "Lay out a blank worksheet labeled fictional example. Keep that label throughout.", "Fictional inputs • Not a ProfitLane result"),
(32, "Suppose fuel is four hundred dollars and tolls are fifty dollars. That leaves seven hundred and fifty dollars before the other costs we still need to review.", "Subtract each item as it is spoken: $1,200 − $400 − $50 = $750. Hold the arithmetic.", "$750 remaining before other costs"),
(47, "Now suppose we allocate three hundred dollars in other operating costs. That leaves four hundred and fifty dollars. It is only a remainder within this example.", "Add the $300 line and show $750 − $300 = $450. Use a neutral label, not a green profit badge.", "$450 remaining in this example"),
(62, "It is not automatically the driver's wage, final take-home pay or profit. What counts as a cost depends on the business and what this worksheet actually includes.", "Return to the presenter. Show a card reading included costs, then a second card reading costs still to check.", "Check what is included and excluded"),
(77, "Your review may need labor, maintenance, insurance, financing, applicable fees and taxes. Do not assume a partial list is complete, or subtract the same expense twice.", "Reveal the possible review items gradually. Do not add invented percentages or tax amounts.", "Review applicable costs • Avoid double-counting"),
(90, "Start with the payment, then ask what it needs to cover. Save the checklist and follow ProfitLane for practical dispatcher education and honest product updates.", "Show the entire fictional worksheet, then the approved logo and handle. Hold the closing card briefly.", "@profitlane.dispatch • Save the checklist")
],
# 4 · Founder introduction
[
(3, "Meet the person behind ProfitLane.", "Angel faces the camera at a desk; if unavailable, an identified team presenter introduces him.", "Angel • ProfitLane founder"),
(15, "ProfitLane's founder, Angel, brings approximately eight years of trucking industry experience. His focus is independent dispatchers and the decisions they make at the desk.", "Use an approved founder portrait or desk interview. Confirm the experience wording before recording; never put that production note on screen.", "Independent dispatchers first"),
(28, "He is comfortable appearing in videos and prefers a client-to-client conversation. That gives us room for clear explanations, practical questions and a more natural tone.", "Show a relaxed interview setup. An identified team presenter or voiceover delivers this introduction while Angel appears in the desk footage.", "Straightforward desk conversations"),
(41, "One concept he wants to explain is AI system tracking. Its intended purpose concerns logistics companies using AI in negotiation or communication between brokers and dispatchers.", "Show an original concept card with broker–dispatcher communication. Do not use real company names or detection flags.", "AI system tracking • Proposed concept"),
(53, "The aim is to support dispatchers in choosing whom to work with. The method, accuracy and availability need confirmation; this video is explaining the concept.", "Return to the speaker and retain the concept label. Hold a short limits card beside it.", "Method, accuracy and availability unverified"),
(63, "Angel's mission is to assist dispatchers, not replace them. Your experience, relationships and judgment stay central as the product is developed.", "Use a simple close desk shot and the existing approved icon. Avoid invented stories or customer footage.", "AI assists. The dispatcher decides."),
(72, "Follow ProfitLane for more explanations. What question would you like Angel to work through at the dispatch desk?", "Finish with the speaker and an easy-to-read handle. Invite one specific question.", "@profitlane.dispatch • Ask Angel a question")
],
# 5 · Fuel arithmetic
[
(3, "Check the fuel assumptions first.", "Show three empty cards: total miles, MPG and price per gallon.", "Fuel estimate = assumptions + arithmetic"),
(15, "For this fictional trip, use six hundred total miles. That includes the one hundred deadhead miles and five hundred loaded miles from our earlier example.", "Fill the mileage card and show 100 + 500 = 600. Maintain fictional-example labeling.", "Fictional example • 600 total miles"),
(28, "Assume six miles per gallon. Six hundred divided by six gives one hundred gallons. Keep the units visible so the steps are easy to check.", "Write 600 miles ÷ 6 MPG = 100 gallons. Point to each unit and pause on the result.", "600 ÷ 6 = 100 gallons"),
(40, "Now assume fuel costs four dollars per gallon. Multiply one hundred gallons by four dollars. The estimated fuel cost is four hundred dollars.", "Fill the fuel-price card and write 100 × $4 = $400. This is not a live fuel-price display.", "100 gallons × $4 = $400"),
(53, "That is an estimate for those assumptions, not a quote for your truck. If you change the mileage, fuel economy or price, recalculate rather than reusing the answer.", "Highlight the three input cards one at a time. Keep the result labeled estimate.", "Change an input? Recalculate."),
(65, "Fuel is one part of a load review. This number does not include every operating cost or tell you whether to accept the offer.", "Slide the fuel calculation beside a broader costs-and-time checklist.", "Estimated fuel cost ≠ total cost"),
(75, "Save the three-step method: total miles, assumed fuel economy and fuel price. Which assumption would you check most carefully?", "Return to the presenter with the completed three-card calculation and a comment prompt.", "Save the method • Check your assumptions")
],
# 6 · Proposed score
[
(3, "What is behind that score?", "Show a paper 76/100 card with a visible concept label from the first frame.", "Concept mockup • 76 is arbitrary"),
(18, "Angel describes the proposed one-to-one-hundred load score as a recommendation tool. It is intended to help dispatchers, particularly people new to dispatching, review an opportunity before booking.", "Keep the paper card visible, then reveal a human-review checklist beside it. No acceptance button is shown.", "Proposed recommendation tool • In development"),
(33, "The proposed considerations include weight in relation to distance, deadhead miles before the trip and diesel prices in relevant areas. Each needs clear, understandable input information.", "Reveal three labeled paper cards as each factor is spoken. Use no actual score calculation.", "Weight/distance • Pre-trip deadhead • Area diesel prices"),
(47, "Pallet count and load payment are also part of Angel's description. He emphasizes the payment. No numerical weights or formula have been established in these materials.", "Add pallet count and payment cards; emphasize payment visually without assigning a percentage.", "Pallet count • Load payment • No published formula"),
(62, "The scoring method has not been validated. Seventy-six here is an arbitrary illustration. It is not a computed recommendation, acceptance threshold or promise that a load will be profitable.", "Point to the arbitrary-example label and replace the large score with a reminder to inspect the inputs.", "Unvalidated • No profitability guarantee"),
(77, "Before relying on any summary, you would still need to check assumptions, missing information, costs and timing. The dispatcher's judgment stays part of the decision.", "Show a person checking the input cards and marking unknowns as questions, without suggesting the product already does this.", "Review assumptions and missing information"),
(90, "Explore the proposed score in our concept videos and follow ProfitLane for confirmed updates. What would you need to understand before using a recommendation?", "Return to the presenter with the handle and one discussion question. Keep the in-development label visible through the end.", "@profitlane.dispatch • Your judgment stays central")
],
# 7 · Negotiation questions
[
(3, "Ask before you counter.", "Presenter holds three blank question cards at a desk.", "Three questions before the counteroffer"),
(15, "Let's rehearse a fictional conversation. A dispatcher is reviewing an offer, but some details are missing. Before discussing a counteroffer, the dispatcher needs clearer information.", "Two team members sit at separate desks or use split-screen. Identify the scene as fictional role-play throughout.", "Fictional role-play • No real company shown"),
(28, "First question: can you confirm the pickup and delivery dates, appointment times and time zones? A mileage number alone does not tell you the schedule.", "Dispatcher reads the first card; show an original appointment graphic with dates marked to confirm, not invented confirmed times.", "1. Confirm dates, times and time zones"),
(41, "Second question: what accessorial terms apply, and how are they documented? Ask for clarification before assuming an additional service or waiting time will be paid.", "Reveal the second card. Use a generic terms-to-confirm checklist, without a fake broker promise or rate agreement.", "2. Clarify applicable accessorial terms"),
(54, "Third question: are there other load requirements, stops or delivery details to review? The purpose is to understand the offer rather than fill in gaps yourself.", "Reveal the final card and a simple multi-stop route sketch. Leave unknown details visibly open.", "3. Verify requirements and stops"),
(68, "With clearer facts, the dispatcher can prepare a reasoned conversation using their own process and agreements. No script guarantees a better rate or a successful booking.", "Return to one speaker and show the three completed questions. Do not display a negotiated success amount.", "Clearer facts • No guaranteed rate outcome"),
(80, "Save these questions and follow ProfitLane for dispatcher education. Angel can walk through an authentic example later, after reviewing which details are appropriate to share.", "Close on the checklist and handle. The later founder example is an invitation, not an invented anecdote.", "@profitlane.dispatch • Save the questions")
],
# 8 · Comparing two trips
[
(3, "Same payment. Different total miles.", "Show two fictional load cards, each labeled $1,200.", "Fictional loads • Same $1,200 payment"),
(16, "For Load A, imagine five hundred loaded miles and one hundred empty miles before pickup. Add them together: six hundred total miles for this comparison.", "Build the Load A card with 500 + 100 = 600. Hold the completed sum.", "Load A: 600 total miles"),
(29, "For Load B, keep the five hundred loaded miles, but use two hundred empty miles before pickup. That makes seven hundred total miles. The payment stays twelve hundred dollars.", "Build Load B beside A, changing only the deadhead assumption in this fictional comparison.", "Load B: 700 total miles"),
(43, "Now divide each payment by its total miles. Load A gives two dollars per mile. Load B gives approximately one dollar and seventy-one cents per mile.", "Show $1,200 ÷ 600 = $2.00 and $1,200 ÷ 700 ≈ $1.71. Pause for viewers to compare.", "A: $2.00/total mile • B: about $1.71/total mile"),
(56, "Those figures describe revenue per total mile. They do not show profit or tell you which load to accept. This example isolates one difference, not every consideration.", "Circle the words revenue per total mile and place a separate costs-and-time card below both loads.", "Revenue per mile ≠ profit or an acceptance rule"),
(69, "The dispatcher still needs to review costs, appointment windows, other travel and the next move. Use your actual information rather than treating either fictional rate as a benchmark.", "Show the review checklist, leaving space for the dispatcher's own notes. No market-rate graph or invented benchmark.", "Review costs • Schedule • Next move"),
(80, "Save the comparison and follow ProfitLane for more examples. What other information would you ask for before making the call?", "Return to the presenter with both load cards and the question underneath.", "@profitlane.dispatch • What information is missing?")
],
# 9 · Two concepts, separate purposes
[
(3, "Two concepts. Clear limits.", "Show two paper cards labeled score and AI system tracking, with a concept label from frame one.", "Concept mockup • In development"),
(18, "This is a paper walkthrough, not a live product demo. First, consider Angel's proposed load recommendation score, intended to support review before a dispatcher decides whether to book.", "Focus on the score card and a person reviewing a fictional load sheet. No automated booking action.", "1. Proposed load recommendation score"),
(33, "The proposed inputs cover weight relative to distance, pre-trip deadhead, diesel prices in relevant areas, pallet count and load payment. No working or validated score is shown here.", "Reveal the proposed inputs one by one. Keep any score number off screen so no calculated result is implied.", "Proposed inputs • No validated score demonstrated"),
(48, "Separately, Angel's AI system tracking concept concerns logistics companies using AI in communication or negotiation between brokers and dispatchers. Its intended purpose is to help dispatchers choose whom to work with.", "Move to the second card and an original broker–dispatcher communication diagram. Do not show real names, detected-AI flags or a blacklist.", "2. AI system tracking • Proposed purpose"),
(63, "How identification would work, what information it would use and how accurate it could be still need confirmation. A diagram is not evidence of a functioning detection system.", "Show three question cards: method, information and accuracy. Retain the concept label and avoid animated scanning effects.", "Method • Data access • Accuracy: unverified"),
(77, "Both ideas are intended as assistance. The dispatcher's review and final judgment stay central. The local marketing tracker you are viewing is separate from the proposed dispatching product.", "Bring the two concept cards back beside a human-review card. Do not present the marketing dashboard as a product screen.", "AI assists. The dispatcher decides."),
(90, "Follow for product updates. Once a real product page and demo-request route are approved, we will share how to explore ProfitLane and request a demo.", "Close on @profitlane.dispatch. Do not add a fabricated website, email or demo link; the route remains conditional.", "Follow now • Demo details when available")
],
# 10 · Human judgment
[
(3, "What stays with the dispatcher?", "Angel or an identified presenter asks the question in a relaxed desk shot.", "Your judgment stays central"),
(15, "Think about the questions you ask, the relationships you know and the context behind an offer. A short summary cannot explain every part of that decision.", "Show three original cards: questions, relationships and context. Pause as each is revealed.", "Questions • Relationships • Context"),
(27, "Angel wants ProfitLane to support independent dispatchers, including people who are new to the work. Independent operators starting their own dispatching are a secondary audience.", "Return to the speaker. Place the primary audience first, with the secondary audience in smaller supporting text.", "Independent dispatchers first"),
(39, "The proposed recommendation score is intended to support load review. AI system tracking is a separate proposed concept about AI use in broker–dispatcher communication.", "Show two concept cards with separate names and purposes. Keep the in-development label visible.", "Two proposed concepts • In development"),
(51, "Working features and results have not been demonstrated here. We can explain the ideas honestly while keeping the limits clear and leaving the decision with the dispatcher.", "Put a human-review card beside the concepts; show no promised savings or automatic acceptance action.", "No verified product results claimed"),
(62, "That is the message behind ProfitLane: Made for dispatchers by dispatchers. Practical explanations should help you ask better questions, not pressure you into an offer.", "Use the exact approved tagline with the existing logo. Hold it for reading.", "Made for dispatchers by dispatchers."),
(72, "Follow ProfitLane at profitlane dot dispatch. What would you like Angel to explain next, in a conversation at the dispatch desk?", "Finish on the presenter and handle with one specific comment question.", "@profitlane.dispatch • Ask Angel")
]
]
posts=[x for x in calendar if x['activity']=='Publish']
scripts=[]
for i,p in enumerate(posts[:10]):
 beats=[]
 start=0
 for end,words,visual,text in filming[i]:
  beats.append(dict(start=start,end=end,spoken=words,visual=visual,text=text))
  start=end
 # Keep the calendar's hook synchronized with the spoken opening.
 p['hook']=beats[0]['spoken']
 scripts.append(dict(number=i+1,day=p['day'],date=p['date'],title=p['title'],hook=p['hook'],speaker=('Identified team presenter or voiceover introducing Angel' if i==3 else 'Angel or an identified team presenter'),length=f"About {start} seconds",duration=start,word_count=sum(len(b['spoken'].split()) for b in beats),script='\n\n'.join(b['spoken'] for b in beats),scenes='\n'.join(f"{b['start']}–{b['end']}s: {b['visual']}" for b in beats),text='\n'.join(f"{b['start']}–{b['end']}s: {b['text']}" for b in beats),beats=beats,caption=p['caption'],hashtags=p['hashtags'],cta=p['cta']))
data=dict(calendar=calendar,scripts=scripts)
(ROOT/'content.js').write_text('window.PROFITLANE_CONTENT = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
with (ROOT/'content-calendar.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(calendar[0]),lineterminator="\n"); w.writeheader(); w.writerows(calendar)
intro='# 30-day TikTok content calendar\n\nSuggested window: November 9–December 8, 2026. Publish three times weekly: 13 publishing slots. The other 17 days are production, response and review days with reserve concepts, not extra daily posts. Draft audience: independent dispatchers first; independent operators starting their own dispatching second. Goals: brand awareness and attracting potential customers. Tone: educational, professional, casual and relatable. All topics are plans; load examples are fictional. Dates remain suggested and can be shifted. The historical research and exact stakeholder responses are unchanged. Suggested publishing test: 6 p.m. in the audience’s primary time zone; validate through account analytics. See the CSV for spreadsheet use.\n\n'
for p in calendar:
 intro+=f"## Day {p['day']} · {p['date']} · {p['activity']}\n\n"
 for k,label in [('title','Video topic / reserve idea'),('category','Pillar'),('hook','Hook'),('format','Format'),('message','Main message'),('caption','Caption'),('hashtags','Hashtags'),('cta','CTA')]: intro+=f"- **{label}:** {p[k]}\n"
 if p['activity']!='Publish': intro+='- **Work today:** Prepare this reserve concept, respond to relevant comments, or review equal-window results. Do not publish an extra video by default.\n'
 intro+='\n'
(ROOT/'content-calendar.md').write_text(intro.rstrip()+'\n')
s="""# First ten TikTok videos · timed filming scripts

## How to use this guide

Each numbered video contains a complete speaking script broken into short sections. **SAY** is the exact commentary to record. **SHOW** describes the visual to display during that commentary. **ON-SCREEN TEXT** is a short overlay, not an extra line to read aloud. No ad-libbing is required.

Timecodes are elapsed video time in minutes:seconds. They are a recording/editing plan, not measured footage. Targets range from about 70 to 90 seconds, allowing pauses for calculations, concept cards and natural delivery. Most commentary sections are planned at roughly 100–150 words per minute; rehearse and adjust shot boundaries before filming. Keep the 2–3 second hook, and hold important figures briefly so viewers can read. Do not rush to force a take into the timeline.

Record vertical 9:16 while stationary. Use the approved brand assets, clear audio and checked subtitles of the spoken lines. Overlays supplement subtitles. Keep concept labels visible for the entire concept video and fictional-example labels visible during calculations. Avoid customer data and real company labels in mockups. No working dispatch product, validated score or measured product result is demonstrated.

Audience: independent dispatchers first; independent operators starting their own dispatching second. Tone: educational, professional, casual and relatable. Angel may appear, with an identified presenter or voiceover as an alternative. Confirm his experience wording and any real anecdote before recording; do not invent one. The exact stakeholder responses and four research entries remain intact. Follow CTAs assume the account is available; product exploration and demo requests wait for an approved real route.

## Video index

"""
for p in scripts:
 s+=f"{p['number']}. **{p['title']}** — {p['length']}\n"
s+='\n'
def timestamp(seconds):return f"{seconds//60:02d}:{seconds%60:02d}"
for p in scripts:
 s+=f"## {p['number']}. {p['title']}\n\n**Draft slot:** Day {p['day']} · {p['date']}\n\n**Target length:** {p['length']} · {p['word_count']} spoken words, plus visual holds\n\n**Speaker:** {p['speaker']}\n\n**Opening hook:** {p['hook']}\n\n"
 for b in p['beats']:
  s+=f"### {timestamp(b['start'])}–{timestamp(b['end'])}\n\n**SAY**\n\n> {b['spoken']}\n\n**SHOW:** {b['visual']}\n\n**ON-SCREEN TEXT:** {b['text']}\n\n"
 s+=f"**Caption:** {p['caption']}\n\n**Hashtags:** {p['hashtags']}\n\n**CTA / production instruction:** {p['cta']}\n\n---\n\n"
(ROOT/'video-scripts.md').write_text(s.rstrip()+'\n')
print('Created 30 calendar entries and 10 complete, timed filming scripts.')
