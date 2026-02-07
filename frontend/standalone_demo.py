import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# ==========================================
# 1. INTERNAL GENERATOR (No Backend Needed)
# ==========================================

# Fake Locations
LOCATIONS = [
    {"country": "India", "city": "Kanpur", "ip": "103.211.55."},
    {"country": "India", "city": "Mumbai", "ip": "103.211.60."},
    {"country": "USA", "city": "New York", "ip": "45.76.12."},
    {"country": "Russia", "city": "Moscow", "ip": "185.17.44."},  # Hacker Node
    {"country": "China", "city": "Beijing", "ip": "202.108.33."}  # Hacker Node
]

DEVICES = ["Windows 11", "MacBook Pro", "iPhone 15", "Linux (Kali)", "Unknown Android"]

# Session State for History
if 'history' not in st.session_state:
    st.session_state.history = []

def generate_internal_log():
    # 85% Safe, 15% Hacker Attack
    is_threat = random.random() > 0.85
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    if is_threat:
        # THE ATTACK SCENARIO
        user_id = "User_9982_VIP" 
        loc = LOCATIONS[3] # Moscow
        device = "Linux (Kali)" 
        action = "CRITICAL_ALERT"
        risk_score = random.randint(90, 99)
        desc = "Impossible Travel: Mumbai -> Moscow in 5s"
    else:
        # NORMAL USER
        user_id = f"User_{random.randint(1000, 1050)}"
        loc = LOCATIONS[random.randint(0, 1)] 
        device = DEVICES[random.randint(0, 2)]
        action = "LOGIN_SUCCESS"
        risk_score = random.randint(5, 20)
        desc = "Biometric verified"

    log = {
        "id": f"evt_{random.randint(10000,99999)}",
        "time": timestamp,
        "user": user_id,
        "location": f"{loc['city']}, {loc['country']}",
        "device": device,
        "status": action,
        "risk_score": risk_score,
        "details": desc
    }
    
    # Update History
    st.session_state.history.insert(0, log)
    if len(st.session_state.history) > 50:
        st.session_state.history.pop()
        
    return log

def get_ai_analysis(log):
    return f"""
    ⚠️ **HAWKSENTINEL FORENSIC REPORT**
    
    **Target:** {log['user']}
    **Threat Detected:** Account Takeover Attempt (Level 5)
    
    **AI Evidence:** 
    1. **Impossible Travel:** User session jumped 4,000km to {log['location']} in < 5 seconds.
    2. **Device Fingerprint:** Device fingerprint is inconsistent with the user’s historical devices and matches a high-risk configuration profile.
    3. **Behavioral Anomaly:** Login pattern deviates 99.8% from user baseline.
    
    **Autonomous Action:** 
    ✅ Account **Auto-Frozen**. 
    ✅ 2FA Reset Link sent to verified email.
    """

# ==========================================
# 2. UI & DASHBOARD
# ==========================================

# ==========================================
# 2. UI & DASHBOARD
# ==========================================

st.set_page_config(
    page_title="HawkSentinel AI", 
    page_icon="🦅", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# SIDEBAR CONTROLS
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.header("🦅 HawkSentinel")

    st.write("---")
    st.success("● SYSTEM ONLINE")
    st.info("Autopilot: ENABLED")
    st.write("Active Nodes: **5 (Global)**")
    
    st.write("---")
    st.write("**AI Diagnostics**")
    st.progress(100, text="Model Integrity")
    st.progress(42, text="Threat Load")

# TOP LAYOUT: Logo | Title | Theme Toggle
col_logo, col_title, col_toggle = st.columns([1.2, 6.8, 2])

with col_logo:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.header("🛡️")

with col_title:
    st.title("HawkSentinel AI")
    st.caption("⚡ Autonomous Real-Time Account Security Watchdog")

with col_toggle:
    # THEME TOGGLE (Moved to Top Right)
    theme_mode = st.radio("UI Mode", ["Dark Ops", "Light (Day)"], horizontal=True, label_visibility="collapsed")

# DYNAMIC CSS BASED ON THEME
if theme_mode == "Dark Ops":
    bg_color = "#050505"
    card_color = "#111"
    text_color = "#f0f0f0"
    metric_label_color = "#888"
    metric_value_color = "#fff"
    border_color = "#333"
else:
    bg_color = "#ffffff"       # Pure White Background
    card_color = "#f8f9fa"     # Light Grey Cards
    text_color = "#000000"     # Pitch Black Text
    metric_label_color = "#333"
    metric_value_color = "#000"
    border_color = "#ddd"

st.markdown(f"""
    <style>
    .stApp {{background-color: {bg_color}; color: {text_color};}}
    
    /* Force Text Colors for Metrics (Crucial for Light Mode) */
    [data-testid="stMetricLabel"] {{ color: {metric_label_color} !important; }}
    [data-testid="stMetricValue"] {{ color: {metric_value_color} !important; }}
    
    /* Card Container Styling */
    div[data-testid="metric-container"] {{
        background-color: {card_color};
        border: 1px solid {border_color};
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }}
    
    /* Headers */
    h1, h2, h3, p {{ color: {text_color} !important; }}
    
    /* Custom Red Alert */
    .stAlert {{
        background-color: #2a0a0a !important;
        border: 1px solid #ff0000 !important;
        color: #ffcccc !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# METRICS ROW
m1, m2, m3, m4 = st.columns(4)
m1.metric("Active Sessions", "2,401,922", "+1.2%")
m2.metric("Threats Neutralized", "42", "+4 this hour", delta_color="inverse")
m3.metric("System Latency", "38ms", "-12ms", delta_color="normal")
m4.metric("AI Confidence", "99.9%", "Stable")

st.divider()

# LIVE FEED AREA
st.subheader("📡 Live Global Traffic Stream")
placeholder = st.empty()

# RUN LOOP
if "running" not in st.session_state:
    st.session_state.running = True

while st.session_state.running:
    # Generate Data Internal (No API)
    new_log = generate_internal_log()
    df = pd.DataFrame(st.session_state.history)

    with placeholder.container():
        # 🚨 THREAT ALERT LOGIC
        if new_log['risk_score'] > 90:
            st.error(f"🚨 CRITICAL SECURITY ALERT: {new_log['user']} | {new_log['details']}")
            
            # The "AI Explanation" Dropdown
            with st.expander("🤖 READ AI FORENSIC REPORT", expanded=True):
                st.markdown(get_ai_analysis(new_log))
        
        # SHOW TABLE
        # We handle styling differently for Light/Dark
        if theme_mode == "Dark Ops":
            highlight = 'background-color: #2a0a0a; color: #ffeb3b; font-weight: bold'
        else:
            highlight = 'background-color: #ffcccc; color: #ff0000; font-weight: bold'

        styled_df = df[['time', 'user', 'location', 'device', 'status', 'risk_score']].style.apply(
            lambda x: [highlight if x['risk_score'] > 90 else '' for i in x], 
            axis=1
        )
        
        st.dataframe(
            styled_df,
            column_config={
                "risk_score": st.column_config.ProgressColumn(
                    "Risk Level",
                    format="%d",
                    min_value=0,
                    max_value=100,
                ),
            },
            use_container_width=True,
            hide_index=True
        )
        
    time.sleep(1) # Refresh rate
