
from datetime import date
from enum import Enum

from pydantic import BaseModel, field_validator


class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Ticket(BaseModel):
    ticket_id: str
    customer: str
    priority: Priority
    date: date

    @field_validator("customer")
    @classmethod
    def validate_customer(cls, value):
        if not value.strip():
            raise ValueError("Customer name cannot be empty")

        return value
