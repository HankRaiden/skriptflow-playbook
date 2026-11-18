# Phase 3 · Concept

**Goal of this phase:** the chosen solution becomes a concept you can show, discuss and implement.

Before: [Phase 2 · Solution](02-phase-2-solution.md). Start phase 3 only once a human has decided in step 8.

---

## Step 9 · AI: strategy paper and concept

**Who:** AI · **Result:** strategy paper (2–4 pages)

```text
{{CONTEXT}}

Based on the chosen solution, write a strategy paper for the other person.

Structure:
1. Situation – in their words (short quotes from the transcript).
2. Goal – what is different after implementation, described as everyday life, not technology.
3. Solution – the chosen variant, in simple words.
4. Benefit argument – per building block: feature → advantage → benefit for exactly this person.
5. Implementation in phases – with a first quick win after a few weeks.
6. What we need from you – decisions, access, contacts.
7. Risks and how we handle them.
8. Next steps.

Rules:
- Formal or informal address as stated in the context.
- NO made-up numbers, testimonials, studies or guarantees. Where a number is missing, write "[to be clarified]".
- No jargon without explanation.

Chosen solution and decision:
{{DECISION}}

Current-state analysis:
{{CURRENT_STATE}}
```

**Check:** Search specifically for made-up evidence. AI texts tend towards "Our customers report 25% more …". If you can't prove such a sentence, delete it. Trust is the only thing you are really selling in a first meeting.

More: [Benefit argument](benefit-argument.md)

---

## Step 10 · AI: flow diagram for implementation

**Who:** AI · **Result:** implementation diagram (phases, packages, dependencies)

```text
{{CONTEXT}}

From the strategy paper, create a flow diagram of the IMPLEMENTATION as Mermaid code (flowchart LR).
- One column (subgraph) per phase.
- In each phase the packages or work steps as boxes.
- Arrows for dependencies ("B needs A").
- Mark places where the customer has to decide or deliver with ◆.
- At most 14 boxes.
Then output a list of milestones at which we check together whether it works.

Strategy paper:
{{STRATEGY_PAPER}}
```

---

## Step 11 · AI: content for the presentation

**Who:** AI · **Result:** slide-by-slide content

```text
{{CONTEXT}}

Create the content for a presentation of at most 12 slides for the follow-up meeting.
For each slide: title (max. 8 words), key message (one sentence), 3 bullet points, suggestion for an image or diagram.

Mandatory slides:
- "This is what I understood" – with the confirmed current-state diagram.
- "This is what it could look like" – with the target diagram.
- "What it gives you" – benefit argument.
- "How we start" – first step, time frame, what we need from you.

Rules: speak the other person's language. No made-up numbers. No slide without a clear message.

Strategy paper:
{{STRATEGY_PAPER}}
Implementation diagram:
{{IMPLEMENTATION_DIAGRAM}}
```

---

## Step 12 · Human: build and discuss the presentation

**Who:** human · **Result:** finished presentation and a conversation as equals

The AI has supplied the content. You build the presentation yourself – in your language, with your feel for the person in front of you. This last prompt prepares you for the conversation:

```text
{{CONTEXT}}

I'm presenting the concept tomorrow. Prepare me:
1. The five most likely objections from the other person – and an honest, short answer to each.
2. Three questions I can open the meeting with, instead of starting with slides.
3. How I'll notice that something doesn't fit – and how I react then.

Material:
{{STRATEGY_PAPER}}
{{CURRENT_STATE}}
```

**Check:** The goal is not "selling" but a shared picture. If the other person recognises their company in the current-state diagram, the most important step is already done.

Back to the overview: [Checklist](checklist.md)
