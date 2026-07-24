from pydantic import BaseModel
from typing import Literal, Optional


class AgentResponse(BaseModel):
    thought: str

    action: Literal[
        "read_ticket",
        "get_possible_team",
        "save_classification",
        "FINAL_ANSWER",
        "ESCALATE"
    ]

    category: Optional[Literal[
        "BUG",
        "FEATURE",
        "QUESTION"
    ]] = None
    
    explanation: str