# Task 1: Customer Service Ticket Tracker

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(tickets_dict, ticket_id, customer_name, issue):
    if ticket_id not in tickets_dict:
        tickets_dict[ticket_id] = {"Customer": customer_name, "Issue": issue, "Status": open}
        print(f"Ticket ID {ticket_id} for customer {customer_name} with issue {issue} has been added.")
    else:
        print(f"Ticket ID {ticket_id} already exists. Please choose a different ID.")

def update_status(tickets_dict, ticket_id, status):
    if ticket_id not in tickets_dict:
        print(f"Ticket {ticket_id} not found.")
    else:
        tickets_dict[ticket_id]["Status"] = status
        print(f"Status of ticket {ticket_id}: {status}")

def display_tickets(tickets_dict):
    for ticket in tickets_dict:
        print(tickets_dict)



open_ticket(service_tickets, "Ticket003", "Patches", "Incorrect password")
update_status(service_tickets, "Ticket003", "closed")
display_tickets(service_tickets)
