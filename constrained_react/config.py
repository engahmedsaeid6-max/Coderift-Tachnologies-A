"""
Configuration for the Constrained ReAct Agent.
"""

# Maximum reasoning steps allowed
MAX_STEPS = 5

# Allowed tool names
ALLOWED_TOOLS = [
    "read_ticket",
    "get_possible_team",
    "save_classification",
    "FINAL_ANSWER",
    "ESCALATE"
]