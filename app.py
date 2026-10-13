from __future__ import annotations

import os
from datetime import datetime

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()


def get_church_info() -> dict[str, str]:
    return {
        "name": os.getenv("CHURCH_NAME", "Powerhouse Parish"),
        "timezone": os.getenv("CHURCH_TIMEZONE", "Africa/Lagos"),
        "address": os.getenv("CHURCH_ADDRESS", "Please contact the church for directions."),
        "pastor": os.getenv("CHURCH_PASTOR", "Please contact the church office."),
    }


def get_service_schedule() -> list[dict[str, str]]:
    """Sample schedule; leadership should confirm all times before public use."""
    return [
        {"day": "Monday", "time": "Confirm locally", "service": "Prayer Band"},
        {"day": "Tuesday", "time": "Confirm locally", "service": "Digging Deep"},
        {"day": "Thursday", "time": "Confirm locally", "service": "Faith Clinic"},
        {"day": "Sunday", "time": "8:00 AM", "service": "Sunday School"},
        {"day": "Sunday", "time": "9:00 AM", "service": "Family Worship"},
        {"day": "Sunday", "time": "5:30 PM", "service": "Evening Service"},
    ]


def lookup_scripture(reference: str) -> str:
    """Return a reference prompt, not fabricated or unlicensed verse text."""
    cleaned = reference.strip()
    if not cleaned:
        return "Usage: /bible John 3:16"
    return (
        f"Bible reference received: {cleaned}\n"
        "Please read it in your preferred Bible translation. Automatic verse retrieval "
        "is not connected in this version."
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        name = get_church_info()["name"]
        await update.message.reply_text(
            f"Welcome to {name}!\n\n"
            "Use /info for church information, /schedule for service times, "
            "/bible followed by a reference for Bible reading help, or /appointment "
            "for appointment guidance."
        )


async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    info = get_church_info()
    await update.message.reply_text(
        f"{info['name']}\n"
        f"Address: {info['address']}\n"
        f"Pastor: {info['pastor']}\n"
        f"Timezone: {info['timezone']}"
    )


async def schedule_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        return
    lines = ["Service schedule (please confirm any unverified time with church leadership):"]
    lines.extend(
        f"• {item['day']} — {item['time']}: {item['service']}"
        for item in get_service_schedule()
    )
    await update.message.reply_text("\n".join(lines))


async def bible_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(lookup_scripture(" ".join(context.args)))


async def appointment_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Appointment requests are not automatically booked or stored by this bot yet. "
            "Please contact the church office directly to arrange a time. "
            "Avoid sending confidential pastoral details in this chat."
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Available commands:\n"
            "/start — welcome message\n"
            "/info — church information\n"
            "/schedule — service schedule\n"
            "/bible John 3:16 — Bible reference guidance\n"
            "/appointment — appointment guidance\n"
            "/help — command list"
        )


def run_cli() -> None:
    print(f"Welcome to {get_church_info()['name']} assistant")
    while True:
        print("\n1. Church information\n2. Service schedule\n3. Scripture reference\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            for key, value in get_church_info().items():
                print(f"{key.title()}: {value}")
        elif choice == "2":
            print("\nService schedule (confirm unverified times with leadership):")
            for item in get_service_schedule():
                print(f"- {item['day']} | {item['time']} | {item['service']}")
        elif choice == "3":
            print(lookup_scripture(input("Enter a Bible reference (e.g. John 3:16): "))
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        print("TELEGRAM_BOT_TOKEN is not configured; starting local menu.")
        run_cli()
        return
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info_command))
    app.add_handler(CommandHandler("schedule", schedule_command))
    app.add_handler(CommandHandler("bible", bible_command))
    app.add_handler(CommandHandler("appointment", appointment_command))
    app.add_handler(CommandHandler("help", help_command))
    print("Starting Powerhouse church assistant on Telegram.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
