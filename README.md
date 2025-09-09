⚖️ Generative AI for Demystifying Legal Documents

A GenAI Hackathon Project built with Google Gemini API + Streamlit

🚨 Problem Statement

Legal documents—like rental agreements, loan contracts, or terms of service—are full of complex jargon. Most people agree to these terms without fully understanding them, creating risk and potential legal issues.

💡 Our Solution

We built an AI-powered assistant that transforms legal documents into clear, accessible language. Users can:

Upload contracts or agreements

Get plain-language summaries of key points

Ask specific questions (e.g., “What’s the penalty clause if I break the lease?”)

Export results to PDF or TXT for easy reference

This empowers everyday citizens and small businesses to make informed decisions and avoid hidden risks.

✨ Core Features

📑 Document Summarizer → Upload PDF/TXT, receive simplified summaries.

❓ Document Q&A → Ask questions about clauses and get clear explanations.

⬇️ Export Options → Save outputs as TXT or PDF.

Bonus Features (beyond hackathon scope):

📖 Story Mode

💡 Motivation Mode

🌐 Translate Mode (English ↔ Hindi)

📝 Summarize Any Text

💬 Free Chat Mode

🛠️ Tech Stack

Streamlit → UI Framework

Google Gemini API → AI backend

PyPDF2 → PDF text extraction

FPDF → Export to PDF

Python 3.10+

🚀 How to Run Locally
git clone https://github.com/NARAYAN790/genai-multimode-chatbot.git
cd genai-multimode-chatbot

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt


Add your Gemini API key in .streamlit/secrets.toml:

GEMINI_API_KEY = "your-api-key-here"


Run the app:

streamlit run app.py

🌐 Live Demo

👉 Try the App Here

🧭 Judge Walkthrough

Upload a rental agreement (PDF/TXT).

View a simplified summary in plain language.

Ask: “What is the penalty clause?” → Get a clear explanation.

Export the results as PDF/TXT.

(Bonus) Explore Story, Motivation, or Translate modes to see the app’s extensibility.

📸 Screenshots

Document Summarizer

Q&A Mode

👨‍💻 Author

Narayan Gupta
🎓 B.Tech in Electronics & Communication, Dr. A.I.T.D Kanpur
💡 Interests: AI, NLP, Data Science, Generative AI

LinkedIn

GitHub

🏆 Acknowledgements

Hackathon by Google & Hack2Skill
Powered by Google Gemini API + Streamlit