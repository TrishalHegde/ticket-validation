
import csv
from ticket_validator.logger import logger
from pydantic import ValidationError
from ticket_validator.models import Ticket


def read_tickets(file_path):
    valid_tickets = []
    invalid_tickets = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                ticket = Ticket(**row)
                valid_tickets.append(ticket)
                logger.info("Ticket %s validated successfully", ticket.ticket_id)
            except ValidationError as error:
                invalid_tickets.append({
                    "row": row,
                    "error": str(error)
                })
                logger.error("Ticket %s failed validation: %s", row.get("ticket_id", "Unknown"), str(error))

    return valid_tickets, invalid_tickets


if __name__ == "__main__":
    valid, invalid = read_tickets("data/tickets.csv")

    print("\nVALID TICKETS:")
    for ticket in valid:
        print(ticket)

    print("\nINVALID TICKETS:")
    for ticket in invalid:
        print("Row:", ticket["row"])
        print("Error:", ticket["error"])
