<div align="center">

# 🍲 Frankie's Bite
### Restaurant operations on autopilot

**Eight workflows that turn WhatsApp chaos into confirmed orders, matched payments and a self-reporting business, built entirely on free tools.**



![Zapier](https://img.shields.io/badge/Zapier-FF4A00?logo=zapier&logoColor=white)




![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?logo=googlesheets&logoColor=white)




![Gmail](https://img.shields.io/badge/Gmail-EA4335?logo=gmail&logoColor=white)




![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)




![Data](https://img.shields.io/badge/Data-100%25%20synthetic-lightgrey)




![Cost](https://img.shields.io/badge/Tool%20cost-%240-brightgreen)



[The 8 workflows](#the-8-workflows) · [Engineering decisions](#engineering-decisions) · [Results](#results) · [Limitations](#honest-limitations)

*Demo video: [watch here]* (https://youtu.be/XyfeHN3IKj8?si=0qDV6QOqSe7h9Sld)

</div>

---

## The problem
Picture a busy kitchen in Yenagoa, Bayelsa State. Orders arrive on WhatsApp, Instagram and phone calls. Bank transfers are checked against orders by hand. Stock runs out without warning. Late deliveries and complaints go unanswered because nobody has time.

Frankie's Bite is a fictional restaurant built to practise exactly that reality: messy Nigerian-English orders, underpaid transfers, missing references, and a manager who cannot be everywhere.

## What I built
A connected set of automations that handle the repetitive work and **hand anything uncertain to a human**.

```
INPUTS                          PROCESSING                    OUTPUTS

New orders ------------+
Bank alerts -----------+
Customer messages -----+--> Google Sheets --> Zapier --+--> Customer and staff emails
Deliveries ------------+                                +--> Audit logs
Complaints ------------+                                +--> Human review queue
Daily schedule --------+
```

### Deep dive: payment matching
Real bank alerts are messy, so matching works in steps and fails safe.

```
Bank alert arrives
      |
      v
Extract bank reference (regex)
      |
      v
Look up payment, then order
      |
      +-- Order NOT found ---------> Manager review: unmatched
      |
      +-- Order found
            |
            +-- Amount equals total --> Log as paid
            |
            +-- Amount differs -------> Manager review + email
                                        (underpaid or overpaid)
```

## The 8 workflows
| # | Workflow | Business outcome | Techniques |
|---|---|---|---|
| 1 | [Order confirmation](zaps/01-order-confirmation) | Customers get instant confirmation | Triggers, field mapping |
| 2 | [Kitchen alert](zaps/02-kitchen-alert) | Kitchen is told about live orders only | Filters |
| 3 | [Low-stock alert](zaps/03-low-stock) | Manager warned before items run out | Formula-driven status, updated-row trigger |
| 4 | [Payment matching](zaps/04-payment-matching) | Transfers matched to orders, exceptions escalated | Regex, lookups, branching |
| 5 | [Message routing](zaps/05-message-routing) | Messy WhatsApp text classified and routed, with no paid AI | Rule engine, branching |
| 6 | [Late-delivery apology](zaps/06-late-delivery) | Delayed customers get an apology, delays are logged | Filter, lookup, audit log |
| 7 | [Complaint routing](zaps/07-complaint-routing) | Urgent complaints reach the manager first | Priority branching |
| 8 | [Daily sales summary](zaps/08-daily-summary) | Owner gets the day's numbers without asking | Scheduling, sheet-side aggregation |

## Engineering decisions
- **Cheap logic before AI.** The message classifier is a transparent rule engine, not a paid model. It is free, testable and explainable. An AI step would only handle what the rules cannot.
- **Fail safe.** Anything unmatched, unclear or sensitive goes to a person. A wrong automatic action costs more than a slow manual one.
- **Compute in the sheet, route in Zapier.** Counting and classification live in formulas that are easy to inspect. Zapier handles triggers, branching and delivery.
- **Verify with a second method.** The daily summary is recomputed independently in Python ([`scripts/daily_summary.py`](scripts/daily_summary.py)) and matches the Zap's email.
- **Designed to be tested.** The data contains deliberate edge cases: underpaid and overpaid transfers, unmatched alerts, typos, incomplete orders and failed deliveries.
- **Mutually exclusive branches.** Path rules cannot overlap, so a record is never processed twice.

## Results
| Check | Result |
|---|---|
| Message classifier | **97 / 100** test messages correct; the 3 misses had typos and fell to "needs human" |
| Payment matching | Exact, underpaid and unmatched test alerts each took the correct path |
| Daily summary | 4 Nov 2026: 7 orders, 1 cancelled, ₦73,900, WhatsApp busiest, **matches the Python check** |
| Late deliveries | 22 of 211 flagged by the filter in the data; each test apology logged with a timestamp |

## Honest limitations
Good engineers state their limits.
- All data is synthetic, and the classifier's rules were tuned on the same 100 messages, so 97/100 is an upper bound, not real-world accuracy.
- I tested a few records per workflow, not every row.
- Test emails went to my own address because customer emails are fake.
- Free-plan task limits mean the daily Zap was switched off after testing.
- This is a portfolio project, not a production system, and it has no measured business impact yet.

## Data
Synthetic and reproducible, in [`data/`](data): 100 customers, a 40-item Nigerian menu, 300 orders, 646 order items, 285 payments, 60 bank alerts, 211 deliveries, 100 messages and 30 complaints. Phone numbers and emails are fake.

## Try it yourself
1. Import the files from `data/` into a Google Sheet (File, Import, Insert new sheets).
2. Build the workflows in order. Each folder in `zaps/` has the steps, screenshots and what went wrong.
3. Test each record once, because each test run writes real rows.

## Skills demonstrated
Workflow automation, API-style data handling, regex extraction, conditional logic and branching, data lookup and joins, exception handling and human-in-the-loop design, synthetic data design, testing and verification, technical documentation.

## Roadmap
- [ ] Rebuild two workflows in Make and n8n
- [ ] Add an AI step behind the rules for unclear messages
- [ ] Telegram channel for staff alerts
- [ ] Duplicate-payment protection

## Repository layout
```
zaps/      one folder per workflow: notes and screenshots
scripts/   Python verification script
data/      synthetic datasets
```

---


**Orkeghen Franklyn** · Workflow automation and AI operations
[LinkedIn](https://www.linkedin.com/in/franklyn-orkeghen-34bb40441/) · [Email](orkeghenfranklyn@gmail.com) · Open to remote roles

