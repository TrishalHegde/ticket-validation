
import pytest
from pydantic import ValidationError

from ticket_validator.models import Ticket


def test_valid_ticket():
    ticket = Ticket(
        ticket_id="T001",
        customer="Rahul",
        priority="High",
        date="2026-11-24"
    )

    assert ticket.ticket_id == "T001"
    assert ticket.customer == "Rahul"


def test_missing_field():
    with pytest.raises(ValidationError):
        Ticket(
            ticket_id="T002",
            priority="Low",
            date="2026-11-24"
        )


def test_invalid_date():
    with pytest.raises(ValidationError):
        Ticket(
            ticket_id="T003",
            customer="Amit",
            priority="High",
            date="wrong-date"
        )


def test_invalid_priority():
    with pytest.raises(ValidationError):
        Ticket(
            ticket_id="T004",
            customer="Priya",
            priority="Urgent",
            date="2026-11-24"
        )


def test_empty_customer():
    with pytest.raises(ValidationError):
        Ticket(
            ticket_id="T005",
            customer="",
            priority="High",
            date="2026-11-24"
        )
