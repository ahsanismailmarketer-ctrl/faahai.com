import streamlit as st
import google.generativeai as genai

# 1. SECURITY & UI CONFIG (Icons hide karne ke liye)
st.set_page_config(page_title="Faah AI", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    [data-testid="stToolbar"] {display: none !important;}
    button[title="View source"] {display: none !important;}
    #manage-app-button {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# 2. SECRET KEY CONNECTION
try:
    # Ye line aapki key ko Streamlit ke "Safe" box se uthayegi
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("System is updating... please wait.")

# 3. INTERFACE
st.title("Hey there, Ahsan Ismail")
if prompt := st.chat_input("How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error("Quota full or connection error.")
