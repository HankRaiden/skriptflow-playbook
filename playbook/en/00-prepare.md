# 00 · Preparation: consent, anonymisation, context

Before a single word goes to an AI, three things come first. Together they take ten minutes and protect you, the person you talked to, and the result.

## 1. Consent before recording

In Germany, secretly recording words not spoken in public is a criminal offence (§ 201 StGB), and many other countries have similar rules. Conversation content is almost always personal data (GDPR, LGPD and similar laws). So:

- **Ask before, not after.** Ideally in the meeting invitation, and once more out loud at the start of the call.
- **State the purpose.** "I'd like to record so I don't miss anything and can send you a summary and a process diagram afterwards."
- **No means no.** Then take notes and use them as your "transcript". The method still works, just coarser.
- **Check your tool.** Where does the recording tool store data? Is there a data processing agreement? That is a question for your data protection officer, not for this playbook.

Invitation template:

```text
A quick note about our meeting: I'd like to record and transcribe our conversation so I can fully
focus on you and nothing gets lost. Afterwards you'll get a summary from me and a picture of your
current process to confirm. I'll use the recording only for this purpose and delete it when we're done.
If you'd rather I didn't, just let me know – then I'll take notes the classic way.
```

> Not legal advice. Check the rules of your country, your company and your tool yourself.

## 2. Anonymise before the AI sees it

Replace names, companies, places, phone numbers, email addresses, prices and anything that identifies a person with roles and placeholders. The AI does not need real names for the analysis. You can keep the mapping to yourself.

```text
You are a careful data-protection assistant.

Task: anonymise the following transcript before it is processed further.
- Replace personal names with roles in square brackets, e.g. [Managing director], [Head of sales], [Me].
- Replace company names with [Company A], [Customer B], [Supplier C] etc. The same name always gets the same placeholder.
- Replace places, phone numbers, email addresses, websites, customer and order numbers with [Place], [Phone], [Email] etc.
- Replace concrete amounts of money with [Amount].
- Change NOTHING else: no shortening, no rewording, no corrections.
- At the end, output a table "original → placeholder" that I keep locally and do NOT share.

Transcript:
{{TRANSCRIPT}}
```

> Important: if you give even this step to a cloud AI, the cloud AI has seen the original data. For sensitive conversations, anonymise by hand (find & replace) or with a locally running model.

## 3. The context block

Every prompt in this playbook starts with the same context block. Fill it in once and always copy it along. That way the AI knows in every step what this is about.

```text
CONTEXT
- Who I am: {{your role, e.g. "process automation consultant", "head of sales", "Salesforce admin"}}
- Who the conversation was with: {{role of the other person, industry, size – no names}}
- Type of conversation: {{first meeting / strategy meeting / training / internal meeting}}
- The other person's goal: {{in one sentence, the way they said it}}
- My goal: {{e.g. "understand their problem and propose three solution paths"}}
- Language and tone of the results: {{e.g. English, informal, simple words, no jargon without explanation}}
```

## Way of working

- **One conversation = one chat** (or one project in your AI). That keeps earlier results in context and you don't have to paste them again every time.
- **Check every step** before you start the next. The AI keeps building on its own mistakes if you don't stop it.
- **Save the results** – one Markdown file per step. At the end you have a traceable record.

Next: [Phase 1 · Current state](01-phase-1-current-state.md)
