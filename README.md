Zaroor Sobia! Neeche tumhare assignment ke liye `README.md` ka **professional aur clear documentation** likha gaya hai, jismein explain kiya gaya hai:

* Swarm agents ka use
* `uv`, `LiteLLM`, `OpenRouter` ka role
* Dono code snippets ka detail explanation

---

## 📘 README.md

# 🤖 Agentic AI - Multimodal Language Agent with LiteLLM & OpenRouter

This project demonstrates how to create AI agents using the `agentic` framework with support for multiple LLM backends like **Gemini (via LiteLLM)** and **DeepSeek (via OpenRouter)**. It also uses `uv` to run the app efficiently.

---

## 📌 Features

* ✨ Intelligent agents with custom instructions
* 🔁 Input/output handled synchronously
* 🔐 API key management via `.env`
* 🔄 Uses both **LiteLLM** and **OpenRouter** providers
* 📚 Educational purpose — built for English learning & Islamic values

---

## 📁 Project Structure

```
agentic_ai/
│
├── .env                      # Contains API keys
├── main.py                  # LiteLLM-based agent
├── openrouter.py            # OpenRouter-based agent
├── README.md                # Project documentation (this file)
├── agents/                  # Core agent logic
└── ...
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agentic_ai.git
cd agentic_ai
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Environment

* Windows: `.\.venv\Scripts\activate`
* Mac/Linux: `source .venv/bin/activate`

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Add `.env` File

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key
ROUTING_API_KEY=your_openrouter_api_key
```

---

## 🧠 Agent 1 – Gemini Model with LiteLLM

### 🔗 File: `litllm.py`

This agent uses **LiteLLM** to connect to **Gemini 2.0 Flash model**. Its job is to respond to greetings with an Islamic reply.

### ✅ Behavior

If user types: `"hi"` or `"hello"`
Agent replies: `"Assalam o Alaikum, I am a Muslim agent, how can I help you?"`

### 💡 Key Concepts:

* **LiteLLM**: A wrapper that helps connect to different LLM providers easily.
* **Agent Instructions**: Define how the model should behave.
* **Runner**: Runs the agent synchronously to get the output.

---

## 🤖 Agent 2 – English Teacher via OpenRouter

### 🔗 File: `routing.py`

This agent is built using **DeepSeek Qwen3-8B** model served via **OpenRouter**.

### ✅ Behavior

Answers any question related to the English language such as:

* Grammar
* Verbs, Modal Verbs
* Vocabulary & Urdu meanings
* Sentence formation and paragraphs

### 💡 Key Concepts:

* **OpenRouter**: A router to access multiple open-source models.
* **AsyncOpenAI**: Async client for connecting to OpenRouter using OpenAI-like interface.
* **RunConfig**: Used to define the specific model and its configuration.

---

## 🚀 How to Run

### Using uvicorn / uv

> uv is a lightning-fast Python web app runner. Here we use it for CLI scripts as well.

```bash
uv run main.py          # For LiteLLM - Gemini Agent
uv run openrouter.py    # For OpenRouter - English Agent
```

---

## 🧬 What is Swarm?

`Swarm` in the `agentic` framework refers to **multiple agents working together**, sharing memory or context to solve a complex task. Though not explicitly shown here, this project is built on top of a swarm-capable structure. In future, agents can:

* Collaborate on tasks
* Pass data between each other
* Use shared long-term memory or goals

---

## 🔍 Key Libraries Used

| Library         | Purpose                                             |
| --------------- | --------------------------------------------------- |
| `agentic`       | Base agent framework (Agent, Runner, memory, etc.)  |
| `litellm`       | Middleware to access Gemini and other models easily |
| `openrouter`    | Connects to models like DeepSeek through one API    |
| `python-dotenv` | Loads secret keys from `.env`                       |
| `uv`            | Runs Python scripts quickly and efficiently         |

---

## 📌 Example Use Cases

* ✅ Language learning tutor
* 🕌 Islamic digital assistant
* 🧠 AI-based English grammar guide
* 🤝 Agent collaboration system (future Swarm usage)

---

## ✍️ Author

**Sobia Mehak** 
