# SkriptFlow · Transcripts become workflows

[Deutsch](README.md) · **English** · [Português (Brasil)](README.pt-br.md)

> **Disclaimer:** I accept no responsibility for any results that may be obtained in connection with this playbook. Not legal, data-protection or business advice. Details: [DISCLAIMER.md](DISCLAIMER.md).

A free prompt playbook that turns **a single conversation transcript** into a shared picture, three solution paths and a finished concept in twelve steps – with any AI, no code.

Project page: **https://skriptflow.vercel.app/en/**

---

## Why

Meeting recordings and summaries are probably the most common AI use case in German-speaking countries. That's a good first step. But it's like owning a Ferrari and driving it at 30 km/h.

A transcript isn't minutes for the archive. It's **raw material**:

- **Perspectives:** a CTO perceives a conversation differently from a head of marketing or customer service. You can steer that by giving the AI a role.
- **Pictures:** a first meeting becomes a flow diagram of today's process. You and the other person instantly share one picture – and they can confirm it.
- **Solutions:** give the AI the role of a consultant, e.g. "AI consultant with expertise in AI automation", and have it propose three different solution paths that you work through together with the other person.
- **Work:** the conversation turns into tasks, leads and opportunities in the CRM – as a draft a human approves.

## The method: 3 phases, 12 steps

| Phase | No. | Step | Who |
|---|---|---|---|
| **1 · Current state** | 1 | Create the transcript (with consent, anonymised) | Human |
| | 2 | Check spelling and mishearings | AI |
| | 3 | Current-state analysis and requirements | AI |
| | 4 | Visualise the current process – and have it confirmed | AI → human |
| **2 · Solution** | 5 | 30 ideas for automation and improvement | AI |
| | 6 | Three solutions as flow diagrams (AI as consultant) | AI |
| | 7 | Challenger: rate and improve | AI |
| | 8 | Decide what to pursue | **Human** |
| **3 · Concept** | 9 | Strategy paper with benefit argument | AI |
| | 10 | Flow diagram for implementation | AI |
| | 11 | Content for the presentation | AI |
| | 12 | Build and discuss the presentation | **Human** |

## Contents

| File | Purpose |
|---|---|
| [00 · Preparation](playbook/en/00-prepare.md) | consent, anonymisation, context block |
| [Phase 1 · Current state](playbook/en/01-phase-1-current-state.md) | steps 1–4 |
| [Phase 2 · Solution](playbook/en/02-phase-2-solution.md) | steps 5–8 |
| [Phase 3 · Concept](playbook/en/03-phase-3-concept.md) | steps 9–12 |
| [Roles](playbook/en/roles.md) | management, CTO, marketing, sales, service, training, AI consultant, challenger |
| [CRM draft](playbook/en/crm-draft.md) | tasks, lead, opportunity, CSV – draft, not autopilot |
| [Benefit argument](playbook/en/benefit-argument.md) | feature → advantage → benefit |
| [Checklist](playbook/en/checklist.md) | all steps to tick off |
| [Example](examples/fiktive-tischlerei/README.md) | fictional conversation with sample results (German) |

## Quick start in 10 minutes

1. Read [00 · Preparation](playbook/en/00-prepare.md) and get consent for your next conversation.
2. Fill in the context block.
3. Open a new chat in your AI (Claude, ChatGPT, Gemini, Copilot – any will do).
4. Work through steps 2 to 4 and send the current-state diagram to the other person asking: "Have I understood this correctly?"

Even this first run changes the follow-up conversation.

## Key principles

1. **A transcript is raw material, not an archive.**
2. **Perspective is a role you assign.**
3. **Picture first, then the solution.** A current-state diagram the other person confirms is worth more than any concept.
4. **Three paths instead of one answer.** Fast, balanced, far-reaching – and choose together.
5. **Every draft gets an opponent.** The challenger finds the weaknesses before the customer does.
6. **The AI proposes, the human decides.** Steps 8 and 12 belong to the human.
7. **Consent before recording, anonymisation before AI.**
8. **No made-up evidence.** Better "[to be clarified]" than an invented number.

## How it came about

I tested this method in a conversation with an entrepreneur friend: recorded the first meeting, current-state analysis, current-state diagram, ideas, solution as a diagram, challenger, strategy paper and presentation – all from a single transcript.

As a Salesforce admin I also run trainings regularly. We turned the transcript of a training into a flow diagram with the key principles so colleagues get an overview faster.

Tried myself: role-based evaluation, visualisation, the AI as consultant with three proposals, and linking to the CRM.

## Outlook: the personal highlight podcast

Advanced AI users mark key moments in meetings with a highlight button. At the end of the week they have all highlights turned into a personal, tailor-made podcast and listen to a review of their week at the weekend or on Monday morning. This idea comes from a podcast by Geoff Woods – I haven't implemented it myself yet. It shows where this can go.

## Limits – honestly

- **The AI is convincingly wrong at times.** That's why there is evidence (quotes), confirmation by the other person, a challenger and two human steps.
- **Data protection is your responsibility.** Record only with consent. Check where your tools store data.
- **A diagram is a hypothesis** until the other person confirms it.
- **No substitute for listening.** The playbook makes a good conversation more productive; it won't turn a bad one into a good one.

## Contributing

Improvements, new roles and translations are welcome – via issue or pull request. The tests (`python3 -m pytest -q`) check that all languages have the same steps and that no real names or amounts end up in the repo.

## License

MIT – see [LICENSE](LICENSE). Free to use, including commercially.
