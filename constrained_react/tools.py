"""
Tools available for the Constrained ReAct Agent.

Only these tools may be executed.
"""


def read_ticket(ticket):
    """
    Returns ticket information.
    """
    return {
        "ticket_id": ticket["ticket_id"],
        "message": ticket["message"]
    }


def get_possible_team(category):
    """
    Returns the responsible team.
    """

    teams = {
        "BUG": "Development Team",
        "FEATURE": "Product Team",
        "QUESTION": "Support Team"
    }

    return teams.get(category, "Manual Review")


def save_classification(ticket_id, category):
    """
    Simulates saving the result.
    """

    return {
        "ticket_id": ticket_id,
        "category": category,
        "status": "Saved Successfully"
    }