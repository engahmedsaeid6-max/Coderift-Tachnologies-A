# Constrained ReAct Agent

## Description

This implementation represents a **Constrained ReAct Agent** for Coderift Technologies.

Unlike the Unconstrained ReAct Agent, this version enforces several safety and reliability constraints.

The agent must:

- Produce valid JSON responses.
- Follow a predefined schema.
- Use only approved tools.
- Stop after a limited number of reasoning steps.
- End with either a FINAL_ANSWER or ESCALATE.

---

## Constraints

### Output Schema

Every model response is validated using Pydantic.

### Allowed Tools

- read_ticket
- get_possible_team
- save_classification

### Maximum Steps

MAX_STEPS = 5

---

## Project Structure

```
constrained_react/

│── main.py
│── prompts.py
│── schema.py
│── tools.py
│── config.py
│── test_cases.json
│── README.md
│── requirements.txt
```

---

## Run

```bash
pip install -r requirements.txt
python main.py
```

---

## Advantages

- Structured output
- Predictable behavior
- Safer execution
- Easy validation
- Better for production

---

## Limitations

- Less flexible than an unconstrained agent.
- Cannot use unknown tools.
- Stops after MAX_STEPS.
