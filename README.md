



\# 🤖 GenAI Multi-Mode Chatbot



A \*\*GenAI Hackathon Project\*\* built with \*\*Google Gemini API + Streamlit\*\*.  

This chatbot provides \*\*multi-mode AI interactions\*\* such as \*\*Document Summarization, Q\&A, Storytelling, Motivation, Translation, and Free Chat Mode\*\*.  

It is designed to help users quickly analyze PDF/TXT documents and interact with them using natural language.



---



\## ✨ Features



\- 📑 \*\*Document Summarizer\*\* → Upload PDF/TXT files, get AI-generated summaries.  

\- ❓ \*\*Document Q\&A\*\* → Ask specific questions about uploaded documents.  

\- 📖 \*\*Story Mode\*\* → Generate creative AI-powered stories.  

\- 💡 \*\*Motivation Mode\*\* → Get motivational messages based on your topic.  

\- 🌐 \*\*Translate Mode\*\* → Translate between \*\*English ↔ Hindi\*\*.  

\- 📝 \*\*Summarize Any Text\*\* → Paste any text and get an instant summary.  

\- 💬 \*\*Chat Mode\*\* → General AI assistant chat.  

\- ⬇️ \*\*Export Options\*\* → Download results in \*\*TXT/PDF\*\* formats.



---



\## 🛠️ Tech Stack



\- \[Streamlit](https://streamlit.io/) → UI Framework  

\- \[Google Gemini API](https://ai.google.dev/) → AI/LLM backend  

\- \[PyPDF2](https://pypi.org/project/PyPDF2/) → PDF text extraction  

\- \[FPDF](https://pyfpdf.readthedocs.io/) → Export summaries to PDF  

\- Python 3.10+  



---



\## 📂 Project Structure







Pranay\_Project/

│-- app.py # Main Streamlit app

│-- requirements.txt # Dependencies

│-- README.md # Documentation

│-- .gitignore # Git ignore rules

│-- .streamlit/

│ └── secrets.toml # API Key (Not committed to GitHub)





---



\## 🚀 How to Run Locally



1\. Clone the repo:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/your-username/genai-multimode-chatbot.git

&nbsp;  cd genai-multimode-chatbot





Create \& activate virtual environment:



python -m venv venv

venv\\Scripts\\activate   # On Windows

source venv/bin/activate   # On Mac/Linux





Install dependencies:



pip install -r requirements.txt





Add your Gemini API key in .streamlit/secrets.toml:



GEMINI\_API\_KEY = "your-api-key-here"





Run the app:



streamlit run app.py



🌐 Deployment (Streamlit Cloud)



Push your repo to GitHub.



Go to Streamlit Cloud

&nbsp;→ Deploy new app.



Connect GitHub repo → Select app.py.



In Secrets Manager, add:



GEMINI\_API\_KEY = "your-api-key-here"





Deploy 🚀



📸 Screenshots

🔹 Document Summarizer



🔹 Chat Mode



👨‍💻 Author



Narayan Gupta



🎓 B.Tech in Electronics \& Communication, Dr. A.I.T.D Kanpur



💡 Interests: AI, NLP, Data Science, Generative AI



🌐 LinkedIn

&nbsp;| GitHub



🏆 Acknowledgements



Hackathon by Google \& Hack2Skill



Powered by Gemini API + Streamlit





---





