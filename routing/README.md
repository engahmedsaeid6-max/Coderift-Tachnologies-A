# Deterministic Routing Agent

## Description

This implementation represents a **Deterministic Routing Agent** for **Coderift Technologies**.

Unlike the Reactive Agent, this implementation uses a Large Language Model (LLM) only once to classify the customer's support ticket.

The LLM does **not** decide what action to take after classification.

Instead, the Python application performs all routing decisions using deterministic code.

---

## Categories

The model must classify every ticket into exactly one category:

- BUG
- FEATURE
- QUESTION

---

## How It Works

1. Receive a customer ticket.
2. Send the ticket to the LLM.
3. The LLM returns one category only.
4. Python routes the ticket to the appropriate team.

Routing rules:

| Category | Assigned Team |
|----------|----------------|
| BUG | Development Team |
| FEATURE | Product Team |
| QUESTION | Support Team |

---

## Architecture

Characteristics of this implementation:

- One LLM call per request
- Deterministic routing logic
- No reasoning loop
- No tool calling
- No schema validation
- Fast and inexpensive

---

## Project Structure

```
routing/
│── main.py
│── prompts.py
│── test_cases.json
│── README.md
│── requirements.txt
```

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
```

Run:

```bash
python main.py
```

---

## Advantages

- Simple architecture
- Low latency
- Low API cost
- Predictable routing
- Easy to test

---

## Limitations

- Depends entirely on the classification result.
- Cannot perform multi-step reasoning.
- Cannot use external tools.
- Cannot request additional information.
