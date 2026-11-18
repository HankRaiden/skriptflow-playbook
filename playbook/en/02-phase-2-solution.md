# Phase 2 · Solution

**Goal of this phase:** a confirmed current-state picture turns into several solution paths – tested by a critical opponent and chosen by a human.

Before: [Phase 1 · Current state](01-phase-1-current-state.md). Start phase 2 only once the other person has confirmed the current-state diagram.

---

## Step 5 · AI: 30 ideas for automation and improvement

**Who:** AI · **Result:** idea list with a rough rating

Why 30? Because the first ten ideas are the obvious ones. The interesting ones come after.

```text
{{CONTEXT}}

You are a consultant for process automation and AI in small and mid-sized companies.
Based on the current-state analysis and the confirmed diagram, develop 30 concrete ideas for improving or
automating the process.

Output a table with the columns:
No. | Idea (one sentence) | Solves pain point | Effort (small/medium/large) | Impact (small/medium/large) | Risk / prerequisite

Rules:
- Mix: quick wins without new software, automations with existing tools, use of AI, organisational changes.
- Every idea must address a pain point from the analysis.
- No advertising for specific vendors; name tools only as examples.
- At the end, mark the 5 ideas with the best impact-to-effort ratio.

Current-state analysis:
{{CURRENT_STATE}}

Confirmed diagram:
{{CURRENT_DIAGRAM}}
```

**Check:** Strike out what obviously doesn't fit this company. You know the culture, the budget and the people – the AI doesn't.

---

## Step 6 · AI: the solution as a flow diagram – the AI as consultant

**Who:** AI in an expert role · **Result:** three solution proposals, each as a target diagram

Here you give the AI a role that fits the request. If the other person is looking for someone in AI automation, for example, the role is "AI consultant with expertise in AI automation". If it's about a sales process, it's "B2B sales consultant for mid-sized companies".

```text
{{CONTEXT}}

Act as {{ROLE, e.g. "AI consultant with expertise in AI automation"}} with 15 years of hands-on experience.

Give me THREE different proposals for how we can meet the other person's requirements. The three should
really differ, e.g.:
- A: fast and lean (with existing tools, doable in weeks),
- B: balanced (a few new building blocks, clearly more impact),
- C: far-reaching (bigger rebuild, biggest lever).

For each proposal:
1. Core idea in two sentences.
2. Which ideas from the list of 30 it bundles (numbers).
3. Target process as Mermaid code (flowchart TD), same notation as the current-state diagram; mark new or automated steps with ✦.
4. What the other person has to do or decide for it.
5. Biggest risk.

Requirements and current-state analysis:
{{CURRENT_STATE}}

30 ideas:
{{IDEAS}}
```

**Check:** Put the current and target diagrams side by side. Can the difference be explained in one sentence? If not, the proposal is too complicated.

---

## Step 7 · AI: challenger – rate and improve

**Who:** AI as opponent · **Result:** rated and improved proposals

Every draft gets an opponent. Ideally in a **new chat**, so the AI doesn't defend its own proposals.

```text
{{CONTEXT}}

You are a critical challenger. Your job is NOT to like the proposals but to find their weaknesses before
the customer does.

For each of the three proposals:
1. Inversion: how would this project have failed six months from now? Name the three most likely reasons.
2. Which assumption is least supported?
3. What did the consultant overlook (data protection, team acceptance, maintenance, vendor lock-in, costs after launch)?
4. Rating 1–10 for: benefit to the customer, feasibility, risk (10 = lowest risk).
5. A concrete improvement that fixes the biggest weakness.

Finally: which proposal – after improvement – would you show the customer first, and why?

Proposals:
{{PROPOSALS}}

Current-state analysis for cross-checking:
{{CURRENT_STATE}}
```

**Check:** Adopt improvements deliberately, not automatically. A challenger who dislikes everything is as unhelpful as one who likes everything.

---

## Step 8 · Human: decide what to pursue

**Who:** human – you and/or the decision-maker on the other side · **Result:** chosen solution or service packages

No AI decides here. The AI has supplied material; now a human who bears the consequences chooses. This prompt only helps prepare the decision:

```text
{{CONTEXT}}

Prepare a decision memo on ONE page:
- Table of the three (improved) proposals: benefit, feasibility, risk, what the customer must contribute.
- One sentence per proposal: "Choose this one if …".
- Three questions the decision-maker should answer before choosing.
Do NOT make the decision yourself.

Material:
{{PROPOSALS}}
{{CHALLENGER_RESULT}}
```

**Check:** Record the decision in writing – with date and a one-sentence reason. That is the starting point for phase 3.

Next: [Phase 3 · Concept](03-phase-3-concept.md)
