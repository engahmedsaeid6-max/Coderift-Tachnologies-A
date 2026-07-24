# Reactive (Rule-Based) Agent

## Description

This implementation represents a purely rule-based support ticket classifier for **Coderift Technologies**.

The agent does **not** use any Large Language Model (LLM) or AI service.

Instead, it classifies customer tickets using predefined keyword matching rules.

The ticket is classified into one of three categories:

- BUG
- FEATURE
- QUESTION

---

## How It Works

1. Read a customer ticket.
2. Convert the text to lowercase.
3. Search for predefined keywords.
4. Return the first matching category.
5. If no keywords match, classify the ticket as QUESTION.

---

## Advantages

- Very fast
- No API cost
- Easy to understand
- Deterministic output

---

## Limitations

- Cannot understand context.
- Relies only on keywords.
- Fails when customers describe the same issue using different wording.

Example:

Supported:

The app crashes after login.

May Fail:

The application suddenly closes after authentication.

Although both describe the same problem, the second message does not contain any predefined keyword.

---

## Project Structure

```
reactive/
│── main.py
│── test_cases.json
│── README.md
│── requirements.txt
```

---

## Run

```bash
python main.py
```
