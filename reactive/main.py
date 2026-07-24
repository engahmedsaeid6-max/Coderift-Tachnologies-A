import json


def classify_ticket(ticket):

    message = ticket["message"].lower()

    bug_keywords = [
         "bug",
        "error",
        "crash",
        "crashes",
        "failed",
        "failure",
        "issue",
        "problem",
        "not working",
        "broken",
        "exception",
        "freeze",
        "freezes",
        "stuck"
    ]

    feature_keywords = [
        "feature",
        "add",
        "new",
        "implement",
        "improve",
        "enhancement",
        "support",
        "request",
        "allow",
        "enable",
        "create"
    ]

    question_keywords = [
       "how",
        "what",
        "why",
        "where",
        "when",
        "can",
        "could",
        "help",
        "guide",
        "?"
    ]

    if any(word in message for word in bug_keywords):
        category = "BUG"

    elif any(word in message for word in feature_keywords):
        category = "FEATURE"

    elif any(word in message for word in question_keywords):
        category = "QUESTION"

    else:
        category = "QUESTION"

    return {
        "ticket_id": ticket["ticket_id"],
        "classification": category
    }


def main():

    with open("test_cases.json", "r", encoding="utf-8") as file:
        tickets = json.load(file)

    print("=" * 60)
    print("Reactive Rule-Based Agent")
    print("=" * 60)

    for ticket in tickets:
        result = classify_ticket(ticket)

        print(f"\nTicket ID : {result['ticket_id']}")
        print(f"Prediction: {result['classification']}")


if __name__ == "__main__":
    main()