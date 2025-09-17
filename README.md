⚖️ Generative AI for Demystifying Legal Documents

A GenAI Hackathon Project built with Google Gemini API + Streamlit

🚨 Problem Statement

Legal documents — rental agreements, loan contracts, terms of service — are often full of jargon and complexity.
Most people sign without fully understanding the terms, creating risk and confusion.

💡 Our Solution

We built an AI-powered assistant that transforms complex legal documents into clear, plain language.

Users can:

📂 Upload contracts or agreements (PDF/TXT)
📑 Get plain-language summaries of key points
❓ Ask specific questions (e.g., “What’s the penalty clause if I break the lease?”)
⬇️ Export results to TXT/PDF

This helps everyday users make informed decisions and avoid hidden risks.

✨ Core Features

📑 Document Summarizer → Upload PDF/TXT, get simplified summaries
❓ Document Q&A → Ask questions about clauses, receive clear answers
⬇️ Export Options → Save outputs as TXT/PDF

Bonus Features (beyond hackathon scope)

📖 Story Mode
💡 Motivation Mode
🌐 Translate Mode (English ↔ Hindi)
📝 Summarize Any Text
💬 Free Chat Mode

🛠️ Tech Stack

Streamlit → UI framework

Google Gemini API → AI backend

PyPDF2 → PDF text extraction

FPDF → Export to PDF

Python 3.10+

🚀 Run Locally

Clone the repository:

git clone https://github.com/NARAYAN790/genai-multimode-chatbot.git
cd genai-multimode-chatbot


Create & activate virtual environment:

Windows

python -m venv venv
venv\Scripts\activate


Mac/Linux

python -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Add your Gemini API key:
Create/edit .streamlit/secrets.toml

GEMINI_API_KEY = "your-api-key-here"


Run the app:

streamlit run app.py

🌐 Live Demo

👉 Try the App Here

Upload a legal document (PDF/TXT), get a simplified summary, ask questions, and export results as TXT or PDF.
Explore optional modes: Story, Motivation, Translate, Free Chat.

👤 Author

Narayan Gupta
🎓 B.Tech, Electronics & Communication – Dr. A.I.T.D, Kanpur
💡 Interests: AI, NLP, Generative AI

🌐 LinkedIn
 | GitHub
 | Project Repo

🔮 Future Scope

✨ Expand language support to more Indian languages (beyond English & Hindi)
✨ Add speech-to-text for voice-based queries on contracts
✨ Build real-time collaboration for multi-user contract review
✨ Integrate with e-sign platforms for instant contract verification
✨ Create compliance-check mode for startups & businesses

While this project primarily uses Google Gemini API for summarization and Q&A, it can be extended with other Google Cloud AI tools:

Vertex AI → Scale to handle larger datasets and enterprise deployments

Gemma → Lightweight on-device deployment for privacy-sensitive use cases

Gemini Code Assist → Automate contract-related workflows and compliance checks

🏆 Acknowledgements

Hackathon organized by Google & Hack2Skill

Powered by Google Gemini API + Streamlit