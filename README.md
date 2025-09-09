# ⚖️ GenAI Legal Document Assistant

*A Generative AI Hackathon Project built with Google Gemini API + Streamlit*

---

## 🚨 Problem
Legal documents — rental agreements, loan contracts, terms of service — are full of jargon and complexity.  
Most people sign without fully understanding the terms, creating **risk and confusion**.

---

## 💡 Our Solution
We built an **AI-powered assistant** that transforms complex legal documents into plain, accessible language.

With our app, users can:  
- 📂 Upload contracts or agreements (PDF/TXT)  
- 📑 Get plain-language summaries of key points  
- ❓ Ask specific questions (e.g., *“What’s the penalty clause?”*)  
- ⬇️ Export results to TXT/PDF for easy reference  

👉 This empowers individuals and small businesses to make **informed decisions** and avoid hidden risks.

---

## ✨ Core Features
- 📑 **Document Summarizer** — Upload PDF/TXT, get simplified summaries.  
- ❓ **Document Q&A** — Ask questions about clauses, receive clear answers.  
- ⬇️ **Export Options** — Save outputs as TXT/PDF.  

**Bonus Modes (beyond hackathon scope):**  
- 📖 Story Mode  
- 💡 Motivation Mode  
- 🌐 Translate (English ↔ Hindi)  
- 📝 Summarize Any Text  
- 💬 Free Chat Mode  

---

## 🛠️ Tech Stack
- Streamlit → UI framework  
- Google Gemini API → AI backend  
- PyPDF2 → PDF text extraction  
- FPDF → Export to PDF  
- Python 3.10+  

---

## 🚀 Run Locally
```bash
git clone https://github.com/NARAYAN790/genai-multimode-chatbot.git
cd genai-multimode-chatbot

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
Add your Gemini API key in .streamlit/secrets.toml

toml
Copy code
GEMINI_API_KEY = "your-api-key-here"
Run the app:

bash
Copy code
streamlit run app.py
🌐 Live Demo
👉 Try the App Here

🧭 Judge Walkthrough
Upload a rental agreement (PDF/TXT).

View the simplified summary.

Ask: “What is the penalty clause?” — Get a clear explanation.

Export results as TXT/PDF.

(Optional) Explore Story, Motivation, or Translate modes.

📸 Screenshots
🔹 Document Summarizer

🔹 Q&A Mode

(Replace with actual screenshots before submission)

👨‍💻 Author
Narayan Gupta
🎓 B.Tech, Electronics & Communication – Dr. A.I.T.D, Kanpur
💡 Interests: AI, NLP, Generative AI

🌐 LinkedIn | GitHub

🏆 Acknowledgements
Hackathon by Google & Hack2Skill

Powered by Gemini API + Streamlit