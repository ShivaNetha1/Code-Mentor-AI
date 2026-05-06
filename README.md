# 💻 AI Code Assistant & Explainer

An AI-powered Code Assistant built using Python, Streamlit, and the Groq API.  
This application helps developers and learners understand programming code with detailed AI-generated explanations, bug analysis, optimization suggestions, and complexity insights.

---

## 🚀 Live Demo

🔗 [Live Demo](https://code-mentor-agent.streamlit.app/)

---

## 📌 Features

- ✅ **Multi-language support:** Python, MySQL, Java, JavaScript, C++, C.
- ✅ **Tailored Explanations:** Choose between Beginner & Advanced explanation modes.
- ✅ **Deep Code Analysis:** AI-generated step-by-step explanations and time complexity insights.
- ✅ **Bug Detection:** Dedicated bug analysis, identifying bad practices and inefficiencies.
- ✅ **Optimization Suggestions:** Actionable feedback to improve your code.
- ✅ **Syntax Highlighting:** Live code preview before generating analysis.
- ✅ **Session History:** Keeps track of your previously analyzed code during the session.
- ✅ **Clean UI:** Built with Streamlit for a fast, responsive, and interactive experience.

---

## 🛠 Tech Stack

- **Frontend & Backend:** [Streamlit](https://streamlit.io/) (Python)
- **LLM Provider:** [Groq API](https://groq.com/) (Llama-3 models)
- **Environment Management:** `python-dotenv`

---

## ⚙️ Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.8 or higher installed on your machine.
* A valid Groq API Key.

---

## � Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ShivaNetha1/Code-Mentor-AI.git
cd ai-code-explainer
```

### 2. Set up a virtual environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
*(Note: Ensure your `requirements.txt` contains `streamlit`, `groq`, and `python-dotenv`)*

### 4. Configure environment variables

Create a `.env` file in the root directory of the project and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## �📂 Project Structure

```text
ai-code-explainer/
│
├── app.py             # Main Streamlit application
├── requirements.txt   # Python dependencies
├── .gitignore         # Files and directories to ignore in Git
├── README.md          # Project documentation
└── .env               # Environment variables (Do not commit this file)


