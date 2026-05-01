
import streamlit as st
import google.generativeai as genai

# 1. PAGE SETUP (CLAUDE LOOK)
st.set_page_config(page_title="Faah AI", page_icon="💡", layout="wide")

# 2. VVIP DESIGN CSS
st.markdown("""
    <style>
    .stApp { background-color: #F9F9F8; color: #1A1A1A; }
    header, footer, #MainMenu {visibility: hidden;}
    .main-hero { text-align: center; margin-top: 100px; margin-bottom: 30px; }
    .main-hero h1 { font-size: 48px; font-weight: 500; font-family: serif; }
    .stChatInputContainer {
        position: fixed !important; bottom: 80px !important;
        max-width: 750px !important; left: 50% !important; transform: translateX(-50%) !important;
        background: white !important; border: 1px solid #E2E2E2 !important;
        border-radius: 24px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
    }
    .btn-row { display: flex; justify-content: center; gap: 12px; margin-top: 20px; }
    .q-btn { background: white; border: 1px solid #EAEAEA; padding: 10px 22px; border-radius: 15px; font-size: 14px; color: #555; }
    .founder-tag { position: fixed; bottom: 20px; left: 20px; font-size: 13px; color: #A0A0A0; }
    </style>
    <div class="founder-tag">Founder | Ahsan Ismail</div>
""", unsafe_allow_html=True)

# 3. SECURE AI CONNECTION (LEAK-PROOF)
try:
    # Ab key GitHub par nazar nahi ayegi, sirf Streamlit Secrets mein hogi
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("Setup Incomplete: Please add your NEW API_KEY in Streamlit Secrets.")

# 4. CHAT LOGIC
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown("""
        <div class="main-hero"><h1>Hey there, Ahsan Ismail</h1></div>
        <div class="btn-row">
            <div class="q-btn">📝 Write</div><div class="q-btn">🎓 Learn</div>
            <div class="q-btn">💻 Code</div><div class="q-btn">💡 Life stuff</div>
        </div>
    """, unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
