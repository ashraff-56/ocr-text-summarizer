import google.generativeai as genai
import streamlit as st
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def list_available_models():
    try:
        models = []
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                models.append(model.name)
        return models
    except Exception as e:
        st.error(f"Error listing models: {e}")
        return []