import os
import json

from groq import Groq
from dotenv import load_dotenv

from prompt import CLASSIFICATION_PROMPT as classification_prompt

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def classify_ticket(ticket):

    prompt = classification_prompt.format(
        ticket=ticket
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


def route_ticket(category):

    if category == "BUG":
        return "Development Team"

    elif category == "FEATURE":
        return "Product Team"

    elif category == "QUESTION":
        return "Support Team"

    return "Manual Review"


def run_tests():

    with open("test_cases.json", "r") as file:
        test_cases = json.load(file)

    print("\n========== TEST RESULTS ==========\n")

    for index, test in enumerate(test_cases, start=1):

        ticket = test["ticket"]
        expected = test["expected"]

        predicted = classify_ticket(ticket)

        team = route_ticket(predicted)

        print(f"Test #{index}")
        print("Ticket:", ticket)
        print("Expected:", expected)
        print("Predicted:", predicted)
        print("Assigned Team:", team)

        if expected == predicted:
            print("Result: PASS")
        else:
            print("Result: FAIL")

        print("-" * 50)


if __name__ == "__main__":

    run_tests()

    print("\n******* CUSTOM TEST *******\n")

    ticket = input("Enter a ticket:\n")

    category = classify_ticket(ticket)

    team = route_ticket(category)

    print("\nClassification:", category)
    print("Assigned Team:", team)