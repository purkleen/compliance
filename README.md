# Regulatory Risk Assessment

A Typeform-style form for the "Upcoming Legal and Systemic Changes" part of the risk management matrix.

Open `index.html` in a browser. A menu next to the title switches between the three versions of the form: `index.html` (Free hand, the default), `version-03.html` (Choose risks first) and `questions-first.html` (Questions first). Two earlier versions, `alternative-01.html` and `original.html`, are kept but no longer linked, and `version-02.html` redirects to the front page.

- **Form (Free hand, `index.html`):** after an intro, the start screen offers a risk search (also matching synonyms), "Add new risk" with the risks of the person's own area (set by the link, for example `index.html#cat-main`), "Browse all risk options", and two shortcuts: upload documents or leave an audio recording. Picking a risk opens a "Risk description" screen with one text box, attachments and an optional follow-up question from the assistant. Each added risk appears in a list at the bottom of the start screen, with "Submit risks" under it.
- **Form (Choose risks first, `version-03.html`):** opens on an intro that explains why people are asked and how the process goes, then goes step by step: choose risks from a multi-select list (the person's own area first, set by the link, for example `version-03.html#cat-main`; search also matches synonyms and can add an own risk), describe any other risks in free text, review the selection, add documents or an audio recording, then describe each selected risk on its own screen, where the assistant may ask a follow-up question. A summary table at the end can be edited before submitting, which leads to a dashboard of submitted forms with PDF download.
- **Form (questions first):** `questions-first.html` starts with five questionnaire-style questions, one per screen (a rating, yes/no and multiple choice, each with an optional box for details, usable from the keyboard). The answers are matched to risks: detected risks are put on the person's list and others are offered as suggestions. The person can then describe other risks in free text, add documents or an audio recording, and describe each risk on its own screen, where the assistant may ask a follow-up question. A summary of the answers and the risks closes the flow.
- **Review submissions:** a split screen with every submitted form on the left and a text summary with cited sources on the right. Reviewers can edit answers, regenerate a form for another area of the company, or resend it to a person.
- **Tagging:** tag each answer against the taxonomy and manage the tags. The first three tag groups are the matrix columns, so tags place an answer in the matrix.
- **Labeling:** a Label Studio-style screen for marking phrases in an answer with labels, with hotkeys, a regions panel and Submit / Skip per task.
- A dark mode toggle sits at the top right.

## Demo limits

- Follow-up questions are scripted here. Live AI follow-ups and summaries, and saving to a shared store, only work when the page runs as a Claude artifact.
- Outside Claude, submitted forms, sent forms, tags and labels are kept in the browser's local storage, so each browser sees only its own.
- Attached files are not uploaded anywhere; only their names are recorded.
