# Powerhouse AI Church Chatbot

A Python starter for a church information assistant, service schedule, Bible reference lookup, reminders, and appointment workflows.

## Features

- Interactive local menu for church information, schedules, and Bible references
- Environment-based church details
- Appointment and reminder validation helpers
- No API keys or personal information committed to the repository

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, fill in only approved public church information, then run:

```bash
python app.py
```

## Important limitations

This is a starter, not a deployed AI chatbot. Scripture lookup accepts a reference but does not retrieve verse text. Reminders are not scheduled or sent, and appointment requests are not transmitted or stored. Service times marked “Confirm locally” must be verified by church leadership.

Before connecting WhatsApp, Telegram, email, a language model, or a scripture provider, add access controls, consent, privacy safeguards, rate limits, monitoring, and tests. Do not collect confidential pastoral or member information in this public repository.

## Structure

- `app.py` — local assistant menu and workflow helpers
- `.env.example` — safe configuration template
- `requirements.txt` — minimal dependency list
