
import streamlit as st
import google.generativeai as genai

# 1. PAGE SETUP
st.set_page_config(page_title="Faah AI", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F9F9F8; }
    header, footer, #MainMenu {visibility: hidden;}
    .main-hero { text-align: center; margin-top: 80px; }
    .main-hero h1 { font-size: 48px; font-weight: 500; font-family: serif; color: #1A1A1A; }
    .stChatInputContainer {
        position: fixed !important; bottom: 80px !important;
        max-width: 750px !important; left: 50% !important; transform: translateX(-50%) !important;
    }
    .founder-tag { position: fixed; bottom: 20px; left: 20px; font-size: 13px; color: #A0A0A0; }
    </style>
    <div class="founder-tag">Founder | Ahsan Ismail</div>
""", unsafe_allow_html=True)

# 2. API CONNECTION (STABLE VERSION)
try:
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
    # 1.5-flash sab se naya aur stable model hai
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error(f"Setup Error: {e}")

# 3. CHAT LOGIC
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown('<div class="main-hero"><h1>Hey there, Ahsan Ismail</h1></div>', unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Simple content generation
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"AI Error: {e}")
