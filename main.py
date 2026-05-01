import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. PAGE SETUP (CLAUDE STYLE)
# ==========================================
st.set_page_config(page_title="Faah AI", page_icon="💡", layout="wide")

# ==========================================
# 2. VVIP CLAUDE-STYLE CSS (FIXED & CENTERED)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F9F9F8; color: #1A1A1A; font-family: 'Inter', sans-serif; }
    header, footer, #MainMenu {visibility: hidden;}

    /* Top Login Button */
    .login-container { position: fixed; top: 20px; right: 30px; z-index: 1000; }
    .login-btn { 
        background: white; border: 1px solid #E5E5E5; padding: 8px 24px; 
        border-radius: 20px; font-weight: 500; font-size: 14px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    /* Centered Hero Section */
    .main-hero { text-align: center; margin-top: 120px; margin-bottom: 30px; }
    .main-hero h1 { font-size: 45px; color: #1A1A1A; font-weight: 600; letter-spacing: -1px; }

    /* Floating Input Box - EXACT CLAUDE DIMENSIONS */
    .stChatInputContainer {
        position: fixed !important; bottom: 80px !important;
        max-width: 800px !important; left: 50% !important; transform: translateX(-50%) !important;
        background: white !important; border: 1px solid #E2E2E2 !important;
        border-radius: 20px !important; box-shadow: 0 10px 40px rgba(0,0,0,0.06) !important;
    }
    
    /* Quick Action Buttons */
    .btn-row { display: flex; justify-content: center; gap: 12px; margin-top: 15px; }
    .q-btn { 
        background: white; border: 1px solid #E8E8E8; padding: 10px 20px; 
        border-radius: 12px; font-size: 14px; color: #555; cursor: pointer;
    }

    /* Founder Tag */
    .founder-tag {
        position: fixed; bottom: 20px; left: 25px;
        font-size: 13px; color: #999; font-weight: 500;
    }
    </style>
    
    <div class="login-container"><button class="login-btn">Login</button></div>
    <div class="founder-tag">Founder | Ahsan Ismail</div>
""", unsafe_allow_html=True)

# ==========================================
# 3. AI BACKEND (AUTO-RECOVERY LOGIC)
# ==========================================
# --- APNI API KEY YAHAN DALEN ---
API_KEY = API_KEY = st.secrets["AIzaSyBknsDcgODlaRNDQcnfvrug6cGwEeicyag"]
genai.configure(api_key=API_KEY)

def get_ai_response(prompt):
    try:
        # Stable model name jo har jagah chalta hai
        model = genai.GenerativeModel("gemini-2.5-flash") 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Ab ye exact error batayega ke masla kya hai
        return f"Actual Error: {str(e)}"

# ==========================================
# 4. UI COMPONENTS
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show Hero only if no chat
if not st.session_state.messages:
    st.markdown("""
        <div class="main-hero">
            <h1>💡 Advanced Intelligence Model</h1>
        </div>
        <div class="btn-row">
            <div class="q-btn">📝 Write</div>
            <div class="q-btn">🎓 Learn</div>
            <div class="q-btn">💻 Code</div>
            <div class="q-btn">💡 Faah's Choice</div>
        </div>
    """, unsafe_allow_html=True)

# Display Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ==========================================
# 5. INPUT LOGIC (CENTERED BOX)
# ==========================================
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            ans = get_ai_response(prompt)
            st.write(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})
