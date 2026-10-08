# Regulatory Risk Assessment

A Typeform-style form for the "Upcoming Legal and Systemic Changes" part of the risk management matrix.

Open `index.html` in a browser. A menu next to the title switches between the three versions of the form: `index.html` (Version 02), `alternative-01.html` and `original.html`. It is a single self-contained page (fonts and the PDF library load from public CDNs).

- **Form (version 02):** opens on an intro that explains why people are asked and how the process goes. The start screen has a risk search (also matching synonyms), "Add new risk", "Browse all risk options", and two shortcuts: upload documents or media, or leave an audio recording, both saved as "To be sorted". "Add new risk" lists the risks of the person's own area (set by the link, for example `index.html#cat-main`) with an "Add another risk…" field; other areas can be browsed below. Picking a risk opens a "Risk description" screen with one text box (typing or dictation), attachments and an optional follow-up question. Added items are shown in a table and submitted together, leading to a dashboard of submitted forms with PDF download.
- **Review submissions:** a split screen with every submitted form on the left and a text summary with cited sources on the right. Reviewers can edit answers, regenerate a form for another area of the company, or resend it to a person.
- **Tagging:** tag each answer against the taxonomy and manage the tags. The first three tag groups are the matrix columns, so tags place an answer in the matrix.
- **Labeling:** a Label Studio-style screen for marking phrases in an answer with labels, with hotkeys, a regions panel and Submit / Skip per task.
- A dark mode toggle sits at the top right.

## Demo limits

- Follow-up questions are scripted here. Live AI follow-ups and summaries, and saving to a shared store, only work when the page runs as a Claude artifact.
- Outside Claude, submitted forms, sent forms, tags and labels are kept in the browser's local storage, so each browser sees only its own.
- Attached files are not uploaded anywhere; only their names are recorded.
