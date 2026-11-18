# Roles · One conversation, many perspectives

A CTO hears something different in a conversation than a head of marketing or someone from customer service. You can use that: give the AI a role, and it reads the same transcript through a different lens.

**How to use the templates:** context block + role prompt + cleaned transcript. One role per run. Then compare the results – the differences are often the most valuable insights.

## The basic form

All roles follow the same form. You can use it to build any further role yourself (purchasing, HR, finance, quality …).

```text
{{CONTEXT}}

Act as {{ROLE}} with many years of experience in {{INDUSTRY}}.
Read the transcript exclusively from your perspective and answer:
1. From your point of view, what is this conversation really about?
2. Which three statements matter most for your area? (verbatim quote + why)
3. Which risks or opportunities do you see that others would miss?
4. Which questions would you ask in the next conversation?
5. What should happen first from your point of view?
Stay in your role. No general advice outside your field.

Transcript:
{{TRANSCRIPT_CLEAN}}
```

## Ready-made roles

### Management

```text
{{CONTEXT}}

Act as the managing director of a mid-sized company. Read the transcript with a view to: limits to growth,
dependence on individual people, decisions that are due, and what the topic means for profit and
future viability. Answer the five questions of the basic form (topic, three most important statements with
quote, overlooked risks/opportunities, next questions, first step).

Transcript:
{{TRANSCRIPT_CLEAN}}
```

### CTO / IT

```text
{{CONTEXT}}

Act as CTO. Read the transcript with a view to: systems in use, media breaks (paper, email, Excel, Word),
duplicate data, interfaces, data protection and IT security, maintainability.
Answer the five questions of the basic form and additionally sketch today's system landscape as a list.

Transcript:
{{TRANSCRIPT_CLEAN}}
```

### Marketing (CMO)

```text
{{CONTEXT}}

Act as head of marketing. Read the transcript with a view to: how do customers find the company? What
language does the other person use for their offer and their customers? Which messages, positioning and
channels are in it? Answer the five questions of the basic form and additionally collect verbatim phrases
that work well for copy.

Transcript:
{{TRANSCRIPT_CLEAN}}
```

### Sales

```text
{{CONTEXT}}

Act as a B2B head of sales. Read the transcript with a view to: buying signals, need, urgency, decision-makers
and influencers, budget signals (no amounts), objections, next step. Answer the five questions of the basic
form and close with an assessment: how warm is this opportunity (cold/lukewarm/hot) and why?

Transcript:
{{TRANSCRIPT_CLEAN}}
```

### Customer service

```text
{{CONTEXT}}

Act as head of customer service. Read the transcript with a view to: recurring customer questions and
problems, waiting times, hand-overs between people where information gets lost, and what frustrates
customers. Answer the five questions of the basic form.

Transcript:
{{TRANSCRIPT_CLEAN}}
```

### Training / knowledge transfer

For internal trainings (e.g. a CRM training): the transcript becomes a learning picture for colleagues.

```text
{{CONTEXT}}

Act as a trainer in adult education. The transcript comes from a training session.
1. Summarise the most important principles in at most 7 sentences – so that a new colleague understands them.
2. Create the workflow shown as a Mermaid diagram (flowchart TD), step by step, marking where users typically make mistakes (⚠).
3. Write 5 comprehension questions with answers.
4. List questions from the training that remained unanswered.

Transcript:
{{TRANSCRIPT_CLEAN}}
```

### AI consultant

The strongest role for first meetings – see also [step 6](02-phase-2-solution.md).

```text
{{CONTEXT}}

Act as {{e.g. "AI consultant with expertise in AI automation"}}. Give me three proposals, three ideas,
for how we can meet the other person's request. Per proposal: core idea, first step, biggest risk.
Clearly distinguish between fast/lean, balanced and far-reaching.

Transcript:
{{TRANSCRIPT_CLEAN}}
```

### Challenger

For every result you want to show someone – see [step 7](02-phase-2-solution.md).

```text
You are a critical challenger. Find the three biggest weaknesses of the following result before the other
person does: unsupported claims, contradictions with the transcript, overlooked risks.
Suggest a concrete improvement for each weakness. Be strict but fair.

Result:
{{RESULT}}

Transcript for cross-checking:
{{TRANSCRIPT_CLEAN}}
```

## Bringing perspectives together

```text
Here are evaluations of the same conversation from several roles. Create a table:
Topic | Management | IT | Marketing | Sales | Service – and mark where the roles contradict each other.
From this, derive the three topics that must be clarified in the next conversation.

{{ROLE_RESULTS}}
```
