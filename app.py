import streamlit as st
from google import genai
import PyPDF2
import io

# Setup API key
client = genai.Client(api_key="AIzaSyBykDv7nKmISwSbFE8a9Gh3sxMLjGigkkk")

# Streamlit Page Config
st.set_page_config(page_title="GenAI Multi-Mode Chatbot", layout="centered")

st.title("🤖 GenAI Hackathon - Multi-Mode Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar mode selection
mode = st.sidebar.selectbox(
    "Select Mode",
    ["Chat Mode", "Story Mode", "Motivation Mode", "Translate Mode", "Summarize Mode"]
)

# -------------------- Document Summarizer --------------------
st.sidebar.header("📂 Document Summarizer")

uploaded_file = st.sidebar.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        # If TXT file
        text = uploaded_file.read().decode("utf-8")
    else:
        # If PDF file
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

    if st.sidebar.button("Generate Summary"):
        with st.spinner("Summarizing document... ⏳"):
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=f"Summarize this legal/complex document in very simple terms:\n{text}"
            )
            summary = response.text if response else "⚠️ No summary generated!"
            st.subheader("📑 Document Summary")
            st.write(summary)

            # Download option
            st.download_button(
                label="⬇️ Download Summary as TXT",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

# -------------------- Image + Text Section --------------------
st.sidebar.header("🖼️ Image + Text Input")

image_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
image_prompt = st.sidebar.text_input("Enter your question about the image")

if st.sidebar.button("Analyze Image") and image_file is not None:
    with st.spinner("Analyzing image... ⏳"):
        # Gemini multimodal input → [text, image]
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[
                {"parts": [{"text": image_prompt}]},
                {"parts": [{"inline_data": {"mime_type": image_file.type, "data": image_file.getvalue()}}]}
            ]
        )
        answer = response.text if response else "⚠️ No response generated!"
        st.subheader("🖼️ Image Analysis Result")
        st.write(answer)

# -------------------- Chat Function --------------------
def get_response(user_input, mode):
    if mode == "Story Mode":
        prompt = f"Write a short, creative story about: {user_input}"
    elif mode == "Motivation Mode":
        prompt = f"Give a motivational message about: {user_input}"
    elif mode == "Translate Mode":
        prompt = f"Translate this text between English and Hindi: {user_input}"
    elif mode == "Summarize Mode":
        prompt = f"Summarize this text in simple words: {user_input}"
    else:
        prompt = user_input  # default chat

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    return response.text if response else "⚠️ No response received!"

# -------------------- Chat Input --------------------
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    bot_response = get_response(user_input, mode)
    st.session_state.messages.append(("bot", bot_response))

# -------------------- Display Chat History --------------------
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)


