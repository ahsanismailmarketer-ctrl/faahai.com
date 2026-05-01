
import streamlit as st
import google.generativeai as genai

# 1. DESIGN SETUP
st.set_page_config(page_title="Faah AI", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F9F9F8; }
    header, footer, #MainMenu {visibility: hidden;}
    .main-hero { text-align: center; margin-top: 100px; }
    .main-hero h1 { font-size: 48px; font-weight: 500; font-family: serif; }
    .stChatInputContainer {
        position: fixed !important; bottom: 80px !important;
        max-width: 750px !important; left: 50% !important; transform: translateX(-50%) !important;
    }
    .founder-tag { position: fixed; bottom: 20px; left: 20px; font-size: 13px; color: #A0A0A0; }
    </style>
    <div class="founder-tag">Founder | Ahsan Ismail</div>
""", unsafe_allow_html=True)

# 2. SECURE CONNECTION (KEY YAHAN NAHI HOGI)
try:
    # Ye line Streamlit ke "Secrets" se key uthayegi, GitHub se nahi
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("Setup Incomplete: Please add your API_KEY in Streamlit Secrets.")

# 3. CHAT UI
if "messages" not in st.session_state: st.session_state.messages = []

if not st.session_state.messages:
    st.markdown('<div class="main-hero"><h1>Hey there, Ahsan Ismail</h1></div>', unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]): st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
