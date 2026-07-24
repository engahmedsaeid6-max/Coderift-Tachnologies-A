import json
import os

from dotenv import load_dotenv
from groq import Groq

from prompt import SYSTEM_PROMPT
from tools import (
    read_ticket,
    get_possible_teams,
    save_classification
)


# Load environment variables
load_dotenv()


# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def run_agent(ticket):

    # Tool: read ticket
    ticket_info = read_ticket(ticket)


    prompt = f"""
{SYSTEM_PROMPT}


Customer Ticket:

{ticket_info}


Think using ReAct style:

Thought:
Analyze the customer ticket.

Action:
Decide what should happen.

Observation:
Use the available information.

Final Answer:
Return:
- Category
- Responsible Team
- Explanation

"""


    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    result = response.choices[0].message.content

    return result




def main():

    # Get current folder path
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


    # Load test cases
    with open(
        os.path.join(BASE_DIR, "test_cases.json"),
        "r",
        encoding="utf-8"
    ) as file:

        tickets = json.load(file)



    print("=" * 60)
    print("Unconstrained ReAct Agent")
    print("=" * 60)



    for ticket in tickets:

        print("\nTicket ID:", ticket["ticket_id"])

        print(
            "Customer Message:",
            ticket["message"]
        )


        answer = run_agent(ticket)


        print("\nAgent Response:")
        print(answer)

        print("-" * 60)




if __name__ == "__main__":
    main()