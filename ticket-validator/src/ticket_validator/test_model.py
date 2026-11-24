
from ticket_validator.models import Ticket

ticket = Ticket(
    ticket_id="T001",
    customer="Rahul",
    priority="High",
    date="2026-11-24"
)

print(ticket)
print("Ticket is valid!")

