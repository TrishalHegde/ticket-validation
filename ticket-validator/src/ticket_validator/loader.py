
import csv

def read_tickets(file_path):

    with open(file_path, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            print(row)


if __name__ == "__main__":
    read_tickets("data/tickets.csv")
