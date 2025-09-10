# ⚖️ GenAI Legal Document Assistant

*A Generative AI Hackathon Project built with Google Gemini API + Streamlit*

---

## 🚨 Problem
Legal documents — rental agreements, loan contracts, terms of service — are often **full of jargon and complexity**.  
Most people sign without fully understanding the terms, creating **risk and confusion**.

---

## 💡 Solution
We built an **AI-powered assistant** that transforms complex legal documents into **clear, plain language**.  

With our app, users can:  
- Upload contracts or agreements (PDF/TXT)  
- Get plain-language summaries of key points  
- Ask specific questions (e.g., “What’s the penalty clause if I break the lease?”)  
- Export results to TXT/PDF for easy reference  

This empowers individuals and small businesses to make informed decisions and avoid hidden risks.

---

## ✨ Core Features
- **Document Summarizer** → Upload PDF/TXT, get simplified summaries  
- **Document Q&A** → Ask questions about clauses, receive clear answers  
- **Export Options** → Save outputs as TXT/PDF  

### Bonus Features (beyond hackathon scope)
- Story Mode  
- Motivation Mode  
- Translate Mode (English ↔ Hindi)  
- Summarize Any Text  
- Free Chat Mode  

---

## 🛠️ Tech Stack
- **Python 3.10+**  
- **Streamlit** → UI framework  
- **Google Gemini API** → AI backend  
- **PyPDF2** → PDF text extraction  
- **FPDF** → Export to PDF  

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
```

Add your Gemini API key in `.streamlit/secrets.toml`:
```
GEMINI_API_KEY = "your-api-key-here"
```

Run the app:
```bash
streamlit run app.py
```

---

## 🌐 Live Demo
[Try the App Here](https://pranay-ai-assistant.streamlit.app/)  

---

## 🏆 Judge Walkthrough
1. Upload a rental agreement (PDF/TXT)  
2. View the simplified summary  
3. Ask: “What is the penalty clause?” → Receive a clear explanation  
4. Export results as TXT/PDF  
5. (Optional) Explore Story, Motivation, or Translate modes  

---

## 🖼️ Screenshots
- Document Summarizer  
- Q&A Mode  

> Ensure the `screenshots/` folder exists in your repo and filenames match exactly (case-sensitive).

---

## 👤 Author
**Narayan Gupta**  
🎓 B.Tech, Electronics & Communication – Dr. A.I.T.D, Kanpur  
💡 Interests: AI, NLP, Generative AI  

[LinkedIn](https://www.linkedin.com/in/narayan-gupta-19903028b) | [GitHub](https://github.com/NARAYAN790) | [Project Repo](https://github.com/NARAYAN790/genai-multimode-chatbot)  

---

## 🙏 Acknowledgements
- Hackathon by Google & Hack2Skill  
- Powered by Gemini API + Streamlit  
