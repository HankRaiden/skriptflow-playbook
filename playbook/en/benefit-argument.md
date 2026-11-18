# Benefit argument · Feature → advantage → benefit

People don't buy features. They buy what a feature changes in their everyday life. The benefit argument translates in three steps:

| Step | Question | Example |
|---|---|---|
| **Feature** | What is it? | The first meeting is shown as a flow diagram. |
| **Advantage** | What can it do? | Both sides see the same process in one picture. |
| **Benefit** | What's in it for **you**? | Misunderstandings surface before a proposal is written – not in the middle of the project. |

The benefit is always **personal** and phrased **in the other person's everyday life**. A good test: can you add "… and therefore …" to the benefit sentence without it sounding silly? Then it's still an advantage.

## The prompt

```text
{{CONTEXT}}

For each building block of the chosen solution, write a three-step benefit argument:
feature (what it is) → advantage (what it can do) → benefit (what the other person gets in THEIR everyday life).

Rules:
- The benefit refers to a concrete pain point from the current-state analysis; give the quote as evidence.
- Use the other person's language, not our jargon.
- NO made-up numbers, percentages, studies or testimonials. If a benefit only convinces with a number we
  don't have, write instead how we could measure it together.
- At the end: the one benefit that weighs most for this person – in one sentence.

Chosen solution:
{{DECISION}}
Current-state analysis:
{{CURRENT_STATE}}
```

## Benefit per role

The same building block has different benefits for different people. Combine the benefit argument with the [roles](roles.md):

```text
Write the benefit argument for the same building block three times: for management, for the employees who
work with it every day, and for the company's customers. One benefit sentence each.

Building block:
{{BUILDING_BLOCK}}
```

## Common mistakes

- **Benefit without context:** "Saves time" – whose time, doing what, freed up for what?
- **Made-up proof:** an invented percentage destroys more trust than it creates.
- **Feature lists:** ten functions convince less than one benefit that hits exactly the pain the other person named themselves.
