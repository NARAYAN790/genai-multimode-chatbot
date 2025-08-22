

# ⚖️ Generative AI for Demystifying Legal Documents

A GenAI Hackathon Project built with Google Gemini API + Streamlit

## 🚨 Problem Statement

Legal documents—like rental agreements, loan contracts, or terms of service—are packed with jargon that’s hard to understand. This creates risk: people often agree to terms they don’t fully grasp.

## 💡 Our Solution

We built an AI-powered assistant that simplifies legal documents into clear, accessible language. Users can:

- Upload contracts or agreements.
- Get plain-language summaries of key points.
- Ask specific questions (e.g., “What’s the penalty clause if I break the lease?”).
- Export results to PDF/TXT for easy reference.

This empowers everyday citizens and small businesses to make informed decisions and avoid hidden risks.

## ✨ Core Features

- 📑 **Document Summarizer** → Upload PDF/TXT, get simplified summaries.
- ❓ **Document Q&A** → Ask questions about clauses, receive clear explanations.
- ⬇️ **Export Options** → Save outputs as TXT/PDF.

### Bonus Features (beyond hackathon scope)
- 📖 Story Mode
- 💡 Motivation Mode
- 🌐 Translate Mode (English ↔ Hindi)
- 📝 Summarize Any Text
- 💬 Free Chat Mode

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) → UI Framework
- [Google Gemini API](https://ai.google.dev/) → AI backend
- [PyPDF2](https://pypi.org/project/PyPDF2/) → PDF text extraction
- [FPDF](https://pyfpdf.readthedocs.io/) → Export to PDF
- Python 3.10+

## 🚀 How to Run Locally
```bash
git clone https://github.com/NARAYAN790/genai-multimode-chatbot.git
cd genai-multimode-chatbot

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

Add your Gemini API key in `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-api-key-here"
```

Run the app:
```bash
streamlit run app.py
```

## 🌐 Live Demo

👉 [Try the App Here](https://pranay-ai-assistant.streamlit.app/)

## 🧭 Judge Walkthrough

1. **Upload** a rental agreement (PDF/TXT).
2. **View** a simplified summary in plain language.
3. **Ask**: “What is the penalty clause?” → Get clear explanation.
4. **Export** the results as PDF/TXT.

*(Bonus: Try Story, Motivation, or Translate modes to see extensibility.)*

## 📸 Screenshots

- 🔹 Document Summarizer
- 🔹 Q&A Mode

## 👨‍💻 Author

**Narayan Gupta**  
🎓 B.Tech in Electronics & Communication, Dr. A.I.T.D Kanpur  
💡 Interests: AI, NLP, Data Science, Generative AI  

🌐 LinkedIn | GitHub

## 🏆 Acknowledgements

Hackathon by Google & Hack2Skill  
Powered by **Gemini API + Streamlit**
