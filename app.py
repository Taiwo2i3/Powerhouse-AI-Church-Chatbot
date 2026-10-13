from __future__ import annotations

import os
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:  # Allows the placeholder module to be inspected without dependencies.
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
    """Return public church details from local configuration placeholders."""
    return {
        "name": os.getenv("CHURCH_NAME", "Example Church"),
        "timezone": os.getenv("CHURCH_TIMEZONE", "UTC"),
        "status": "placeholder",
    }


def lookup_scripture(reference: str) -> dict[str, str]:
    """Validate a reference without calling an external provider or exposing secrets."""
    cleaned = reference.strip()
    if not cleaned:
        return {"status": "error", "message": "Provide a scripture reference."}
    return {
        "status": "placeholder",
        "reference": cleaned,
        "message": "Connect an approved scripture provider before returning verse text.",
    }


def get_service_schedule() -> list[dict[str, str]]:
    """Return an empty schedule until a trusted church data source is configured."""
    return []


def create_reminder(message: str, when: datetime) -> dict[str, Any]:
    """Describe a reminder without sending messages or storing personal data."""
    if not message.strip():
        return {"status": "error", "message": "A reminder message is required."}
    return {
        "status": "placeholder",
        "message": "Reminder integration is not configured.",
        "scheduled_for": when.isoformat(),
    }


def request_appointment(request: AppointmentRequest) -> dict[str, Any]:
    """Validate an appointment request without transmitting it anywhere."""
    if not request.visitor_name.strip() or not request.contact.strip():
        return {"status": "error", "message": "Name and contact are required."}
    return {
        "status": "pending",
        "message": "Appointment workflow placeholder; no request was sent.",
        "request": asdict(request),
    }


def main() -> None:
    print({
        "church": get_church_info(),
        "schedule": get_service_schedule(),
        "scripture": lookup_scripture("John 3:16"),
    })


if __name__ == "__main__":
    main()
