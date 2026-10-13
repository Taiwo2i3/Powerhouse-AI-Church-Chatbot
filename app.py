from __future__ import annotations

import os
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv() -> None:
        return None

load_dotenv()


@dataclass(frozen=True)
class AppointmentRequest:
    visitor_name: str
    contact: str
    preferred_time: str
    notes: str = ""


def get_church_info() -> dict[str, str]:
    """Return church details from environment configuration."""
    return {
        "name": os.getenv("CHURCH_NAME", "Powerhouse Parish"),
        "timezone": os.getenv("CHURCH_TIMEZONE", "Africa/Lagos"),
        "address": os.getenv("CHURCH_ADDRESS", "Add the approved church address in .env"),
        "pastor": os.getenv("CHURCH_PASTOR", "Add the approved pastor name in .env"),
    }


def get_service_schedule() -> list[dict[str, str]]:
    """Return a sample schedule; replace these entries with church-approved details."""
    return [
        {"day": "Monday", "time": "Confirm locally", "service": "Prayer Band"},
        {"day": "Tuesday", "time": "Confirm locally", "service": "Digging Deep"},
        {"day": "Thursday", "time": "Confirm locally", "service": "Faith Clinic"},
        {"day": "Sunday", "time": "8:00 AM", "service": "Sunday School"},
        {"day": "Sunday", "time": "9:00 AM", "service": "Family Worship"},
        {"day": "Sunday", "time": "5:30 PM", "service": "Evening Service"},
    ]


def lookup_scripture(reference: str) -> dict[str, str]:
    """Validate a scripture reference; does not fetch or invent verse text."""
    cleaned = reference.strip()
    if not cleaned:
        return {"status": "error", "message": "Provide a scripture reference."}
    return {
        "status": "reference_received",
        "reference": cleaned,
        "message": "Please read this reference in your preferred Bible translation.",
    }


def create_reminder(message: str, when: datetime) -> dict[str, Any]:
    """Validate a reminder request; scheduling and message delivery are not connected."""
    if not message.strip():
        return {"status": "error", "message": "A reminder message is required."}
    return {
        "status": "not_scheduled",
        "message": "Reminder delivery is not connected yet.",
        "reminder": message.strip(),
        "scheduled_for": when.isoformat(),
    }


def request_appointment(request: AppointmentRequest) -> dict[str, Any]:
    """Validate an appointment request without sending or storing personal information."""
    if not request.visitor_name.strip() or not request.contact.strip():
        return {"status": "error", "message": "Name and contact are required."}
    if not request.preferred_time.strip():
        return {"status": "error", "message": "Please provide a preferred time."}
    return {
        "status": "not_submitted",
        "message": "Appointment submission is not connected. Contact the church office directly.",
        "request": asdict(request),
    }


def print_schedule() -> None:
    print("\nService schedule (confirm times with the church):")
    for item in get_service_schedule():
        print(f"- {item['day']} | {item['time']} | {item['service']}")


def main() -> None:
    print(f"Welcome to {get_church_info()['name']} assistant")
    while True:
        print("\n1. Church information\n2. Service schedule\n3. Scripture reference\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            for key, value in get_church_info().items():
                print(f"{key.title()}: {value}")
        elif choice == "2":
            print_schedule()
        elif choice == "3":
            reference = input("Enter a Bible reference (e.g. John 3:16): ")
            result = lookup_scripture(reference)
            print(f"{result.get('reference', '')} — {result['message']}")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
