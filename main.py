import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Faah AI")

# Simple Setup
try:
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    
    st.title("Faah AI")
    user_input = st.text_input("Kuch likhein:")
    
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
        
except Exception as e:
    st.write(f"Error: {e}")
