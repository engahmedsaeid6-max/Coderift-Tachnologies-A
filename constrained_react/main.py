import json
import os

from dotenv import load_dotenv
from groq import Groq

from prompt import SYSTEM_PROMPT
from schema import AgentResponse
from tools import (
    read_ticket,
    get_possible_team,
    save_classification
)

from config import (
    MAX_STEPS,
    ALLOWED_TOOLS
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

TOOLS = {
    "read_ticket": read_ticket,
    "get_possible_team": get_possible_team,
    "save_classification": save_classification
}

def run_agent(ticket):
    messages = [
        {
            "role": "system", 
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"Please process this customer ticket:\n{json.dumps(ticket)}"
        }
    ]

    for step in range(MAX_STEPS):
        print(f"\n========== STEP {step+1} ==========")

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0,
            response_format={"type": "json_object"},
            messages=messages
        )

        raw_response = response.choices[0].message.content
        print("\nModel Output:")
        print(raw_response)

        messages.append({
            "role": "assistant",
            "content": raw_response
        })

        try:
            agent_response = AgentResponse.model_validate_json(raw_response)
        except Exception as e:
            return {
                "status": "FAILED",
                "reason": f"Schema Validation Error: {e}"
            }

        if agent_response.action not in ALLOWED_TOOLS:
            return {
                "status": "FAILED",
                "reason": "Action is not allowed."
            }

        if agent_response.action == "FINAL_ANSWER":
            team = get_possible_team(agent_response.category)
            save_classification(ticket["ticket_id"], agent_response.category)
            return {
                "status": "SUCCESS",
                "category": agent_response.category,
                "team": team,
                "explanation": agent_response.explanation
            }

        if agent_response.action == "ESCALATE":
            return {
                "status": "ESCALATED",
                "reason": agent_response.explanation
            }

        observation = ""
        if agent_response.action == "read_ticket":
            observation = TOOLS["read_ticket"](ticket)
            
        elif agent_response.action == "get_possible_team":
            observation = TOOLS["get_possible_team"](agent_response.category)
            
        elif agent_response.action == "save_classification":
            observation = TOOLS["save_classification"](ticket["ticket_id"], agent_response.category)

        messages.append({
            "role": "user",
            "content": f"Observation from {agent_response.action}:\n{json.dumps(observation)}"
        })

    return {
        "status": "FAILED",
        "reason": "Maximum reasoning steps exceeded."
    }

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    with open(
        os.path.join(BASE_DIR, "test_cases.json"),
        "r",
        encoding="utf-8"
    ) as file:
        tickets = json.load(file)

    print("=" * 60)
    print("Constrained ReAct Agent Started")
    print("=" * 60)

    for ticket in tickets:
        print(f"\nTicket ID: {ticket['ticket_id']}")
        print(f"Message: {ticket['message']}")

        result = run_agent(ticket)

        print("\nFinal Result:")
        print(json.dumps(result, indent=2))
        print("-" * 60)

if __name__ == "__main__":
    main()