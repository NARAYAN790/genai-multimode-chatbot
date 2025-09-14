import streamlit as st
import google.generativeai as genai
import PyPDF2
import io
import os
from fpdf import FPDF

# ---------------------------
# 0) API config
# ---------------------------
API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY", ""))
genai.configure(api_key=API_KEY)

# Debug info (sidebar pe show hoga)
st.sidebar.text(f"API Key Loaded: {bool(API_KEY)}")

# ---------------------------
# 1) Page Config + Header
# ---------------------------
st.set_page_config(page_title="GenAI Hackathon – Multi-Mode Chatbot", layout="wide")
st.title("🤖 GenAI Hackathon – Multi-Mode Chatbot")

st.markdown("""
Welcome to *Pranay's Multi-Mode AI Chatbot* 🎉  

Here’s what you can do:
1. 📑 **Document Summarizer** – Upload a **PDF or TXT** file → Get instant AI-generated summary.  
2. ❓ **Document Q&A** – Ask focused questions about the uploaded document.  
3. 🧠 **Other Modes** – Story, Motivation, Translate, and Summarize any text.  

👉 Powered by **Google Gemini + Streamlit**, deployed on **Streamlit Cloud** 🚀
""")
st.divider()

# ---------------------------
# 2) Sidebar
# ---------------------------
mode = st.sidebar.selectbox(
    "Select Mode",
    [
        "Document Summarizer",
        "Chat Mode",
        "Story Mode",
        "Motivation Mode",
        "Translate Mode",
        "Summarize Mode"
    ]
)

lang = st.sidebar.selectbox("Output language", ["English", "Hindi"])
tone_note = "Answer in simple {}.".format("English" if lang == "English" else "Hindi")

st.sidebar.header("📂 Document Summarizer")
uploaded_file = st.sidebar.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])

# Session state
if "doc_text" not in st.session_state:
    st.session_state.doc_text = ""
if "last_summary" not in st.session_state:
    st.session_state.last_summary = ""

# ---------------------------
# 3) Helpers
# ---------------------------
def extract_text_from_upload(file) -> str:
    if file is None:
        return ""
    try:
        if file.type == "text/plain":
            return file.read().decode("utf-8", errors="ignore")
        elif file.type == "application/pdf":
            reader = PyPDF2.PdfReader(file)
            text = []
            for i, page in enumerate(reader.pages):
                try:
                    text.append(page.extract_text() or "")
                except Exception:
                    text.append(f"[⚠️ Could not extract text from page {i+1}]")
            return "\n".join(text)
        else:
            return "⚠️ Unsupported file format."
    except Exception as e:
        return f"⚠️ Error reading file: {e}"

def gemini_text(prompt: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")  # ✅ updated model
        resp = model.generate_content(prompt)
        if not resp.text:
            return "⚠️ No response from Gemini (check API key or model access)."
        return resp.text.strip()
    except Exception as e:
        return f"⚠️ Gemini error: {e}"

def make_pdf_bytes(title: str, content: str) -> bytes:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    if title:
        pdf.set_font("Arial", style="B", size=14)
        safe_title = title.encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(0, 8, safe_title)
        pdf.ln(2)
        pdf.set_font("Arial", size=12)
    for line in content.splitlines():
        safe_line = line.encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(0, 6, safe_line)
    return pdf.output(dest="S").encode("latin-1")

# ---------------------------
# Rest of your app code continues (Document Summarizer, Q&A, Other Modes, etc.)
# ---------------------------


