# Powerhouse AI Church Chatbot

A Python starter for a church information assistant with a Telegram interface and local command-line fallback.

## Features

- Telegram commands: `/start`, `/info`, `/schedule`, `/bible`, `/appointment`, and `/help`
- Local menu for church information, service schedules, and Bible references
- Environment-based church details
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

Copy `.env.example` to `.env`. To use Telegram, create a bot through Telegram's official BotFather and put its token in `TELEGRAM_BOT_TOKEN`. Add only church-approved public details to the other settings. Then run:

```bash
python app.py
```

If `TELEGRAM_BOT_TOKEN` is empty, the local menu starts. If a token is configured, the Telegram bot starts.

## Important limitations

This is not yet a generative-AI system. Scripture lookup accepts a reference but does not retrieve verse text. Appointment requests are not automatically booked or stored, and reminders are not scheduled or sent. Service times marked “Confirm locally” must be verified by church leadership.

Before connecting a language model, appointment calendar, reminder provider, or scripture API, add access controls, consent, privacy safeguards, rate limits, monitoring, and tests. Do not collect confidential pastoral or member information in this public repository.

## Structure

- `app.py` — Telegram handlers and local menu
- `.env.example` — safe configuration template
- `requirements.txt` — Python dependencies
