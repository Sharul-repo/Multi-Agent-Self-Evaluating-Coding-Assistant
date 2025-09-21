# 🤖 I've Built a Multi-Agent Self-Evaluating Coding Assistant  

A LangGraph-powered system where multiple AI agents **plan, code, and evaluate** programs in a feedback loop until the solution is correct.  

This project demonstrates how AI can act as a **self-correcting coding assistant** by combining specialized agents with structured prompts.  

---

## ✨ Features
- **Planner Agent** → Converts user request into a clear coding plan.  
- **Coder Agent** → Writes code based on the plan (and fixes based on feedback).  
- **Evaluator Agent** → Reviews code for bugs, edge cases, and best practices.  
- **Feedback Loop** → Automatically retries until a correct solution is reached.  

---
User: write a simple factorial program in any language

Planner Agent → Creates step-by-step instructions  
Coder Agent   → Writes Python code for factorial  
Evaluator     → Reviews correctness & edge cases  
               - Accepts ✅ if correct  
               - Rejects ❌ with feedback if issues found  
Feedback Loop → Coder retries with evaluator feedback  

Final Output: ✅ Correct factorial program
---

## 🧩 Tech Stack
- **[LangChain](https://python.langchain.com/)** → Agent orchestration & LLM interfaces.  
- **[LangGraph](https://github.com/langchain-ai/langgraph)** → State graph for planner → coder → evaluator flow.  
- **[Pydantic](https://docs.pydantic.dev/)** → Structured outputs for evaluations.  
- **[dotenv](https://pypi.org/project/python-dotenv/)** → Load environment variables.  
- **[uv](https://github.com/astral-sh/uv)** → Fast Python package manager for dependencies & execution.  

---


## ⚡ Quick Start  

### 1️⃣ Clone the repo  

```bash
git clone https://github.com/your-username/multi-agent-coding-assistant.git
cd Multi-Agent

# Install dependencies using uv (reads pyproject.toml + uv.lock)
uv sync

# Run your app
uv run main.py
