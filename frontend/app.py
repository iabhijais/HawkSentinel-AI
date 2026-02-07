import streamlit as st
import pandas as pd
import time
import random
import os
from datetime import datetime

# ==========================================
# 1. INTERNAL BACKEND ENGINE (Merged for Cloud)
# ==========================================

# Robust Image Loader
def get_image_path(filename):
    # Check current directory
    if os.path.exists(filename):
        return filename
    # Check frontend directory (if running from root)
    if os.path.exists(f"frontend/{filename}"):
        return f"frontend/{filename}"
    return None

logo_path = get_image_path("logo.png")

# Fake Locations & IPs
LOCATIONS = [
    {"country": "India", "city": "Kanpur", "ip": "103.211.55."},
    {"country": "India", "city": "Mumbai", "ip": "103.211.60."},
    {"country": "USA", "city": "New York", "ip": "45.76.12."},
    {"country": "Russia", "city": "Moscow", "ip": "185.17.44."},  # Hacker Node
    {"country": "China", "city": "Beijing", "ip": "202.108.33."}  # Hacker Node
]

DEVICES = ["Windows 11", "MacBook Pro", "iPhone 15", "Linux (Kali)", "Unknown Android"]

def generate_log_internal():
    """Simulates the backend generator logic directly inside Streamlit"""
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
        loc = LOCATIONS[random.randint(0, 1)] # Mostly India
        device = DEVICES[random.randint(0, 2)]
        action = "LOGIN_SUCCESS"
        risk_score = random.randint(5, 20)
        desc = "Biometric verified"

    return {
        "id": f"evt_{random.randint(10000,99999)}",
        "time": timestamp,
        "user": user_id,
        "ip": f"{loc['ip']}{random.randint(10,255)}",
        "location": f"{loc['city']}, {loc['country']}",
        "device": device,
        "status": action,
        "risk_score": risk_score,
        "details": desc
    }

def get_ai_analysis_internal(log_id):
    """Simulates the AI Analysis API"""
    return "⚠️ **HAWKSENTINEL AI FORENSIC REPORT**\n\n**Threat Identified:** Account Takeover Attempt.\n**Evidence:** User session jumped 4,000km (India to Russia) in <1 minute. Device fingerprint is inconsistent with the user’s historical devices and matches a high-risk configuration profile.\n**Action Taken:** Account Auto-Frozen. 2FA Reset Link sent to verified email."

# ==========================================
# 2. STREAMLIT DASHBOARD UI
# ==========================================

# Page Config with Favicon
if logo_path:
    st.set_page_config(page_title="HawkSentinel AI", page_icon=logo_path, layout="wide")
else:
    st.set_page_config(page_title="HawkSentinel AI", page_icon="🦅", layout="wide")


# Initialize Session State (To store history without a database)
if 'history' not in st.session_state:
    st.session_state.history = []

# Generate a new log on every refresh
new_log = generate_log_internal()
st.session_state.history.insert(0, new_log)
if len(st.session_state.history) > 50:
    st.session_state.history.pop()

# HACKER STYLE CSS
st.markdown("""
    <style>
    .stApp {background-color: #0E1117;}
    div[data-testid="metric-container"] {
        background-color: #1E1E1E;
        border: 1px solid #333;
        padding: 10px;
        border-radius: 5px;
    }
    
    /* Custom Red Alert for Hackers */
    .stAlert {
        background-color: #2a0a0a !important;
        border: 1px solid #ff0000 !important;
        color: #ffcccc !important;
    }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR COMMAND CENTER
with st.sidebar:
    if logo_path:
        st.image(logo_path, use_container_width=True)
    else:
        st.header("🦅 Command Center")
        
    st.success("• SYSTEM ONLINE")
    st.info("Autopilot: ENABLED")
    st.metric("Active Nodes", "5 (Global)")
    
    st.divider()
    st.caption("AI Diagnostics")
    st.progress(98, text="Model Integrity")
    st.progress(12, text="Threat Load")

# MAIN HEADER
col1, col2 = st.columns([1.5, 8.5])
with col1:
    if logo_path:
        st.image(logo_path, use_container_width=True)
    else:
        st.header("🛡️")

with col2:
    st.title("HawkSentinel AI")
    st.caption("Autonomous Real-Time Account Security Watchdog")

# METRICS
m1, m2, m3, m4 = st.columns(4)
m1.metric("Active Sessions", "2,401,922", "+1.2%")
m2.metric("Threats Neutralized", "42", "+4 this hour")
m3.metric("System Latency", "38ms", "-12ms")
m4.metric("AI Confidence", "99.9%", "Stable")

st.write("") # Spacer

# LIVE FEED
st.subheader("📡 Live Global Traffic Stream")

# 🚨 THREAT ALERT LOGIC
if new_log['risk_score'] > 90:
    st.error(f"🚨 CRITICAL_ALERT: {new_log['user']} | {new_log['details']}")
    
    # The "AI Explanation" Dropdown
    with st.expander("💀 READ AI FORENSIC REPORT", expanded=True):
        st.warning(get_ai_analysis_internal(new_log['id']))

# DATA TABLE
df = pd.DataFrame(st.session_state.history)

# Visual Configuration for the Table (Conditional Formatting)
def highlight_risk(row):
    return ['background-color: #2a0a0a; color: #ffeb3b; font-weight: bold' if row['risk_score'] > 90 else '' for _ in row]

st.dataframe(
    df[['time', 'user', 'location', 'device', 'status', 'risk_score']].style.apply(highlight_risk, axis=1),
    use_container_width=True,
    hide_index=True,
    column_config={
        "risk_score": st.column_config.ProgressColumn(
            "Risk Level",
            help="Risk Score 0-100",
            format="%d%%",
            min_value=0,
            max_value=100,
        ),
        "status": st.column_config.TextColumn("Status"),
        "device": st.column_config.TextColumn("Device Type"),
        "location": st.column_config.TextColumn("Geo-Location"),
    }
)

# Auto-refresh logic (Trick to keep the stream alive)
time.sleep(1)
st.rerun()
