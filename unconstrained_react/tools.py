"""
Utility functions available to the application.

In this unconstrained implementation, the language model is free to reason without enforced tool execution.
These functions simulate services that could be available in a production environment.
"""


def read_ticket(ticket):
    """
    Returns the ticket information.
    """
    return {
        "ticket_id": ticket["ticket_id"],
        "message": ticket["message"]
    }


def get_possible_teams(category):
    """
    Returns the responsible team based on the predicted category.
    """

    teams = {
        "Bug Report": "Software Engineering Team",
        "Feature Request": "Product Development Team",
        "General Question": "Customer Support Team"
    }

    return teams.get(category, "Customer Support Team")


def save_classification(ticket_id, category):
    """
    Simulates saving the final classification result.
    """

    return {
        "ticket_id": ticket_id,
        "saved_category": category,
        "status": "Classification saved successfully"
    }
