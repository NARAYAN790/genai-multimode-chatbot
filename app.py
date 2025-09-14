import streamlit as st
import google.generativeai as genai
import PyPDF2
import os
from fpdf import FPDF

# ---------------------------
# 0) API config
# ---------------------------
API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY", ""))
genai.configure(api_key=API_KEY)

# Debug: Show if API key loaded correctly
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

# ---------------------------
# 3) Session state
# ---------------------------
if "doc_text" not in st.session_state:
    st.session_state.doc_text = ""
if "last_summary" not in st.session_state:
    st.session_state.last_summary = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# 4) Helpers
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
        model = genai.GenerativeModel("gemini-2.5-flash-lite")  # ✅ updated stable model
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

def split_text_into_chunks(text, chunk_size=1200, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ---------------------------
# 5) Document Summarizer + Q&A
# ---------------------------
if mode == "Document Summarizer":
    st.subheader("📑 Document Summarizer")

    if uploaded_file is not None:
        st.session_state.doc_text = extract_text_from_upload(uploaded_file)

    if st.session_state.doc_text:
        with st.expander("📜 Preview extracted text (optional)", expanded=False):
            st.text_area("Extracted text", st.session_state.doc_text[:8000], height=220)

        col1, col2, _ = st.columns([1,1,1])

        # Hybrid summary: small docs (single call) vs large docs (chunk)
        if col1.button("✨ Generate Summary"):
            with st.spinner("Summarizing document… ⏳"):
                doc_text = st.session_state.doc_text
                if len(doc_text) < 5000:  # small docs → direct summary
                    prompt = f"Summarize this in 5–7 bullet points. {tone_note}\n\n{doc_text}"
                    st.session_state.last_summary = gemini_text(prompt)
                else:  # large docs → chunking
                    chunks = split_text_into_chunks(doc_text, chunk_size=1200, overlap=200)
                    partial_summaries = [gemini_text(f"Summarize briefly:\n\n{ch}") for ch in chunks]
                    combined_text = "\n".join(partial_summaries)
                    st.session_state.last_summary = gemini_text(f"Combine into a crisp overall summary:\n\n{combined_text}")

        if st.session_state.last_summary:
            st.subheader("📄 AI Summary")
            st.write(st.session_state.last_summary)

            txt_bytes = st.session_state.last_summary.encode("utf-8")
            st.download_button("⬇️ Download Summary (TXT)", data=txt_bytes, file_name="summary.txt", mime="text/plain")
            pdf_bytes = make_pdf_bytes("Document Summary", st.session_state.last_summary)
            st.download_button("⬇️ Download Summary (PDF)", data=pdf_bytes, file_name="summary.pdf", mime="application/pdf")

        st.markdown("---")

        # Optimized Q&A: chunk relevance
        st.subheader("❓ Ask Questions about this Document")
        q = st.text_input("Type your question (e.g., 'Is there a penalty clause?')", key="doc_q")
        ask_cols = st.columns([1,1])
        if ask_cols[0].button("🔎 Get Answer"):
            if q.strip():
                with st.spinner("Searching document and answering…"):
                    chunks = split_text_into_chunks(st.session_state.doc_text)
                    relevant_chunk = max(chunks, key=lambda c: sum(1 for word in q.lower().split() if word in c.lower()))
                    qa_prompt = (
                        f"You are a helpful assistant. {tone_note}\n"
                        "Answer **only** from the document chunk below. "
                        "If not present, say: 'I cannot find this in the document.'\n"
                        f"Question: {q}\n\nDocument Chunk:\n{relevant_chunk}"
                    )
                    answer = gemini_text(qa_prompt)
                st.markdown("**Answer:**")
                st.write(answer)
            else:
                st.warning("Please type a question.")

        if ask_cols[1].button("🧹 Reset Document"):
            st.session_state.doc_text = ""
            st.session_state.last_summary = ""
            st.success("Cleared. Upload a new file from the sidebar.")
    else:
        st.info("⬅️ Upload a **PDF or TXT** from the sidebar to start.")

# ---------------------------
# 6) Other Modes
# ---------------------------
elif mode == "Story Mode":
    st.subheader("📖 Story Mode")
    user_input = st.text_area("Enter a topic for your story:")
    if st.button("✨ Generate Story"):
        with st.spinner("Writing story…"):
            story = gemini_text(f"Write a creative story about: {user_input}. {tone_note}")
        st.write(story)

elif mode == "Motivation Mode":
    st.subheader("💡 Motivation Mode")
    user_input = st.text_area("Enter a topic for motivation:")
    if st.button("⚡ Inspire Me"):
        with st.spinner("Generating motivation…"):
            motivation = gemini_text(f"Give a motivational message about: {user_input}. {tone_note}")
        st.write(motivation)

elif mode == "Translate Mode":
    st.subheader("🌐 Translate Mode")
    user_input = st.text_area("Enter text to translate:")
    if st.button("🌍 Translate"):
        with st.spinner("Translating…"):
            translate = gemini_text(
                "Translate the following text between English and Hindi. "
                "If it's English, translate to Hindi; if it's Hindi, translate to English.\n\n"
                f"{user_input}"
            )
        st.write(translate)

elif mode == "Summarize Mode":
    st.subheader("📝 Summarize Mode")
    uploaded_file = st.file_uploader("Upload PDF or TXT file to summarize", type=["pdf", "txt"])
    input_text = st.text_area("Or paste text here", height=180)

    text_to_summarize = ""
    if uploaded_file:
        st.info("📂 File uploaded. Extracting text…")
        text_to_summarize = extract_text_from_upload(uploaded_file)
        with st.expander("📜 Preview extracted text (optional)", expanded=False):
            st.text_area("Extracted text", text_to_summarize[:8000], height=220)
    elif input_text.strip():
        text_to_summarize = input_text.strip()

    if text_to_summarize:
        if st.button("✨ Summarize Now"):
            with st.spinner("Summarizing… ⏳"):
                if len(text_to_summarize) < 5000:
                    summary_prompt = f"Summarize this content in 5–7 bullet points. {tone_note}\n\n{text_to_summarize}"
                    summary = gemini_text(summary_prompt)
                else:
                    chunks = split_text_into_chunks(text_to_summarize, chunk_size=1200, overlap=200)
                    partial_summaries = [gemini_text(f"Summarize briefly:\n\n{ch}") for ch in chunks]
                    combined = "\n".join(partial_summaries)
                    summary = gemini_text(f"Combine into a crisp summary:\n\n{combined}")
            st.subheader("📄 AI Summary")
            st.write(summary)
            txt_bytes = summary.encode("utf-8")
            st.download_button("⬇️ Download Summary (TXT)", data=txt_bytes, file_name="summarize_mode_summary.txt", mime="text/plain")
            pdf_bytes = make_pdf_bytes("Summarize Mode Summary", summary)
            st.download_button("⬇️ Download Summary (PDF)", data=pdf_bytes, file_name="summarize_mode_summary.pdf", mime="application/pdf")
    else:
        st.info("⬅️ Upload a file OR paste some text to start summarizing.")

# ---------------------------
# 7) Chat Mode (fixed with normal input)
# ---------------------------
else:  # Chat Mode
    st.subheader("💬 Chat Mode")
    user_input = st.text_input("Type your message here:")
    if st.button("Send") and user_input:
        st.session_state.messages.append(("user", user_input))
        bot_response = gemini_text(f"{user_input}\n\n{tone_note}")
        st.session_state.messages.append(("bot", bot_response))

    for sender, msg in st.session_state.messages:
        if sender == "user":
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)

