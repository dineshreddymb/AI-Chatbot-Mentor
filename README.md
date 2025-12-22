# 🤖 AI Chatbot Mentor

An interactive, module-specific AI mentoring application designed to provide focused, distraction-free learning across multiple technical domains.

Unlike generic chatbots, AI Chatbot Mentor strictly responds only within the selected module, ensuring accurate, relevant, and reliable guidance for learners.

## 🚀 Project Overview

* AI Chatbot Mentor is an AI-powered mentoring system built using Streamlit and LangChain, offering structured and domain-restricted learning support.

* Each mentoring session is module-based, meaning the AI mentor:

* Responds only to questions related to the selected module

* Rejects irrelevant questions with a fixed response

* Maintains conversation history during the session

* Allows users to download the entire chat for revision or offline learning

## 👋 Welcome Flow

When the application starts, users see:

Welcome to AI Chatbot Mentor
Your personalized AI learning assistant.
Please select a learning module to begin your mentoring session.

## 📌 Available Modules

Users can choose one module per session:

* Pythoh
 SQL

* Power BI

* Exploratory Data Analysis (EDA)

* Machine Learning (ML)

* Deep Learning (DL)

* Generative AI (Gen AI)

* Agentic AI

* Once selected, the system opens a dedicated mentor interface for that module.

## 🎯 Module-Specific Mentor Interface

Example for Python:

Welcome to Python AI Mentor 🐍
I am your dedicated mentor for Python.
How can I help you today?

✔ The same structure applies to all modules.

## ❓ Question Handling Logic
## ✅ Relevant Questions

Answered clearly and educationally

Structured explanations

Context-aware responses using chat history

## ❌ Irrelevant Questions

If the user asks a question outside the selected module, the chatbot strictly replies:
### Sorry, I don’t know about this question. Please ask something related to the selected module.
This ensures domain control and prevents hallucinated answers.

## 💬 Conversation Flow

* Maintains full chat history during the session

* Preserves context for coherent mentoring

* Displays messages in a ChatGPT-style UI

    * User messages → Right side

    * AI messages → Left side


## 📥 Download Conversation (Key Feature)

At any point during the session, users can download the entire conversation.

✔ Features:

* Includes all user questions and AI responses

* Downloadable as a .txt file

** Useful for:

  * Revision

  * Notes

Portfolio documentation

Offline learning

### ⚠️ This is a mandatory and highlighted feature of the project

## 🧠 Technical Architecture
### Backend

* LangChain

* Prompt templates per module

* Strict domain restriction logic

* Conversation memory management

### Frontend

* Streamlit

* Module selection interface

* Chat-based UI

* Download button for conversation history

### Tech Stack
| Component        | Technology                |
| ---------------- | ------------------------- |
| Frontend         | Streamlit                 |
| AI Orchestration | LangChain                 |
| LLM              | Gemini API (configurable) |
| File Export      | Text (.txt)               |
| Language         | Python                    |


### 📂 Project Structure
AI-Chatbot-Mentor/
│
├── app.py
├── pages/
│   └── chat_page.py
│
├── .gitignore
├── .env.example
├── requirements.txt
└── README.md

## 🎓 Learning Outcomes

* By building this project, you will understand:

* How to build domain-restricted AI chatbots

* Prompt engineering for controlled AI responses

* Using LangChain with conversation memory

* Designing interactive Streamlit applications

* Implementing secure chat export functionality

* Structuring real-world AI mentor systems


## 🔐 Security Note

* API keys are stored securely using environment variables

* .env files are excluded from version control

* A sample .env.example file is provided

## 🏁 Conclusion

AI Chatbot Mentor demonstrates how AI systems can deliver focused, reliable, and learner-centric mentorship.

By enforcing strict domain control and providing practical features like conversation download, this project bridges the gap between generic chatbots and real-world educational AI assistants.

## 📌 Future Enhancements (Optional)

* Quiz-based learning

* Multi-agent mentors

* User authentication

* Session summaries

* Deployment to Streamlit Cloud

### ⭐ If you find this project useful, feel free to star the repository!
