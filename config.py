import streamlit as st

# Retrieve API key from Streamlit secrets
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "default-api-key-if-not-set")

def set_page_config():
    st.set_page_config(
        page_title="OCR Text Summarizer",
        page_icon="🔥",
        layout="wide"
    )