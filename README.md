# Regulatory Risk Assessment

A Typeform-style form for the "Upcoming Legal and Systemic Changes" part of the risk management matrix.

Open `index.html` in a browser. It is a single self-contained page (fonts and the PDF library load from public CDNs).

- **Form:** one question per screen: name, work email, then eight risks (seven regulatory, one systemic). Each risk takes an optional description, drivers, opportunities and source, plus file attachments and a short follow-up chat. A summary step with edit-and-return leads to a dashboard of your submitted forms with PDF download.
- **Review submissions:** a split screen with every submitted form on the left and a text summary with cited sources on the right. Reviewers can edit answers, regenerate a form for another area of the company, or resend it to a person.
- **Tagging:** tag each answer against the taxonomy and manage the tags. The first three tag groups are the matrix columns, so tags place an answer in the matrix.
- **Labeling:** a Label Studio-style screen for marking phrases in an answer with labels, with hotkeys, a regions panel and Submit / Skip per task.
- A dark mode toggle sits at the top right.

## Demo limits

- Follow-up questions are scripted here. Live AI follow-ups and summaries, and saving to a shared store, only work when the page runs as a Claude artifact.
- Outside Claude, submitted forms, sent forms, tags and labels are kept in the browser's local storage, so each browser sees only its own.
- Attached files are not uploaded anywhere; only their names are recorded.
