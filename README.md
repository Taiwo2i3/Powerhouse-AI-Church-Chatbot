# Powerhouse-AI-Church-Chatbot

A Python-based AI assistant for church information, scripture lookup, service schedules, reminders, and appointment workflows.

## What this starter includes

- Safe placeholder functions for church information and scripture lookup
- A service schedule interface ready for a real data source
- Reminder and appointment workflow structures
- Environment-based configuration with no secrets committed

## Quick start

1. Create a virtual environment: python -m venv .venv
2. Activate it and install dependencies: pip install -r requirements.txt
3. Copy .env.example to .env and replace placeholders locally.
4. Run python app.py.

The included functions intentionally return safe placeholder responses. Connect approved church data, a scripture provider, and a messaging channel only after adding authentication, input validation, rate limiting, and privacy controls.

## Project structure

- app.py - starter application and workflow functions
- .env.example - configuration template without credentials
- requirements.txt - minimal Python dependencies

## Safety and privacy

Never commit .env, API keys, tokens, personal appointment details, or production data. Review responses for pastoral sensitivity and obtain consent before storing reminders or appointment information.

## Status

Starter project for iterative development. Replace the placeholders with tested integrations and deployment configuration as requirements become clear.
# Powerhouse-AI-Church-Chatbot
A Python-based AI assistant for church information, scripture lookup, service schedules, reminders, and appointment workflows.
