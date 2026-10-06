# Regulatory Risk Assessment

A Typeform-style form for the "Upcoming Legal and Systemic Changes" part of the risk management matrix.

Open `index.html` in a browser. It is a single self-contained page (fonts and the PDF library load from public CDNs).

- One question per screen: name, work email, area of the company, then eight risks (seven regulatory, one systemic).
- Each risk takes an optional description, drivers, opportunities and source, plus file attachments.
- A summary step with edit-and-return, then a dashboard of submitted forms with PDF download.

## Demo limits

- Follow-up questions are scripted here. Live AI follow-ups, and saving forms to an account, only work when the page runs as a Claude artifact.
- Outside Claude, submitted forms are kept in the browser's local storage.
- Attached files are not uploaded anywhere; only their names are recorded.
