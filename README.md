# Coderift Technologies A

## About the Company

Coderift Technologies A is a software development company that builds software solutions for businesses and customers.

As the company grows, it receives many customer support tickets every day. These tickets must be classified before they can be handled by the appropriate team.

---

# Project Overview

This project demonstrates four different AI agent architectures by solving the same real-world problem.

Instead of comparing different problems, all four agents solve the exact same task so their behavior, strengths, and limitations can be compared fairly.

---

# Problem

## Support Ticket Classification

Customers submit support tickets describing different issues using their own writing style.

Each ticket must be classified into one of the following categories:

- **Bug Report** – The customer is reporting a software bug or malfunction.
- **Feature Request** – The customer is requesting a new feature or enhancement.
- **General Question** – The customer is asking for information or technical assistance.

After classification, the ticket is routed to the appropriate team, reducing manual work and improving response time.

---

# Why an Agent?

This problem requires understanding natural language written in many different ways.

Simple keyword matching is often unreliable because customers may describe the same issue using different words.

By implementing multiple agent architectures, we can compare how different levels of intelligence and control affect the quality, flexibility, and reliability of the classification process.

---

# Project Structure

```
Coderift-Tachnologies-A/
├── README.md/
├── reactive/
├── unconstrained_react/
├── routing/
└── constrained_react/
```

Each folder contains an independent implementation of the same problem using a different agent architecture.

---

# Agent Architectures

### 1. Reactive Agent
A rule-based implementation using predefined if/else conditions without any language model.

### 2. Unconstrained ReAct Agent
An LLM-powered agent that freely reasons, chooses tools, and decides when to stop.

### 3. Routing Agent
A deterministic routing approach where the model first classifies the ticket, then fixed program logic handles the result.

### 4. Constrained ReAct Agent
A controlled reasoning agent that uses schema validation, restricted tool usage, and a maximum number of reasoning steps.

---

# Team Goal

Our objective is not to determine the best architecture, but to understand how each architecture behaves when solving the exact same real-world problem.

This allows us to compare their flexibility, predictability, cost, latency, and robustness using the same set of test cases.
