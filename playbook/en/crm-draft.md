# CRM draft · From conversation to workflow

A transcript only becomes productive when it creates work: a task, a lead, an opportunity. This prompt produces a **draft** that a human checks and then transfers to the CRM – by hand, by import (CSV) or via an automation.

> **Principle: draft, not autopilot.** The AI creates nothing by itself. It prepares, you approve. Only once a draft has been reliable for weeks is it worth automating the transfer – and even then with an approval point.

## The prompt

```text
{{CONTEXT}}

You are a CRM assistant. Read the transcript and create a DRAFT for the CRM.

1. Tasks
   Table: title | description (1 sentence) | owner (role) | due (date or "[to be clarified]") | evidence (quote)
   Only tasks that were promised or clearly agreed in the conversation.

2. Lead / contact
   Fields: company (placeholder) | contact's role | industry | size | source | need in one sentence.

3. Opportunity
   Fields: name | stage (e.g. qualification / needs analysis / proposal) | need | decision-maker | next activity |
   assessment cold/lukewarm/hot with reason. Do NOT invent amounts or a win probability in percent.

4. Call note
   5–8 sentences for the contact's activity history.

5. CSV
   Also output the tasks as CSV with a header row: Subject,Description,Owner,DueDate

Rules:
- Invent nothing. Whatever didn't come up in the conversation is "[to be clarified]".
- Keep the placeholders from anonymisation; I only replace them inside the CRM.

Transcript:
{{TRANSCRIPT_CLEAN}}
```

## Check before transferring

- Was every task really promised – or did the AI turn a good idea into a task?
- Are owners and due dates right?
- Replace placeholders with real records – inside the CRM, not in the AI chat.

## The road to automation (advanced)

Once the draft is reliable, an automation (e.g. with n8n, Make, Zapier or your CRM's built-in tools) can connect the steps: transcript arrives → AI creates the draft in the format above → **a human approves** → tasks, lead and opportunity are created. The approval point isn't distrust of the technology but quality assurance: a wrong CRM entry costs more time later than ten seconds of checking now.
