import streamlit as st
import google.generativeai as genai

# 1. SECURITY & UI CONFIG (Icons hide karne ke liye)
st.set_page_config(page_title="Faah AI", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* 1. Header, Footer aur Main Menu ko bilkul khatam karne ke liye */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 2. 'Hosted with Streamlit' aur 'Created by' ko dhone ke liye */
    .viewerBadge_container__1QS1n {display: none !important;}
    .viewerBadge_link__1S137 {display: none !important;}
    footer {display: none !important;}
    
    /* 3. Right side wala deploy button aur toolbar hide karne ke liye */
    .stAppDeployButton {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    
    /* 4. Background aur gap theek karne ke liye */
    .stApp {
        bottom: 0px !important;
    }
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
