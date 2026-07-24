# Unconstrained ReAct Agent

## Description

This implementation represents an **Unconstrained ReAct Agent** developed for **Coderift Technologies**.

Unlike the Reactive Agent, this implementation relies on a Large Language Model (LLM) to analyze customer support tickets.

The model is free to decide how to reason about the problem and generate the final response without any predefined rules, schema validation, or execution limits.

---

## Categories

The agent classifies customer tickets into one of the following categories:

- Bug Report
- Feature Request
- General Question

The response also includes the responsible team and a short explanation.

---

## Architecture

Characteristics of this implementation:

- Uses an LLM (Groq / Llama 3.1)
- Free-form reasoning
- No fixed decision rules
- No output schema validation
- No allow-list for tools
- No reasoning step limit (MAX_STEPS)

---

## Project Structure

```
unconstrained_react/
│── main.py
│── prompt.py
│── tools.py
│── test_cases.json
│── README.md
│── requirements.txt
```

---

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Create a `.env` file

```
GROQ_API_KEY=your_api_key
```

3. Run

```bash
python main.py
```

---

## Advantages

- Can understand natural language.
- Handles different writing styles.
- Better than keyword matching.

---

## Limitations

- Output format is not guaranteed.
- May generate inconsistent responses.
- Reasoning is unrestricted.
- Higher latency and API cost than the Reactive Agent.
