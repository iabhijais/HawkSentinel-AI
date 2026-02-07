import streamlit as st
import pandas as pd
import time
import random
import os
from datetime import datetime

# ==========================================
# 1. SETUP & UTILS
# ==========================================

# Robust Image Loader
def get_image_path(filename):
    if os.path.exists(filename):
        return filename
    if os.path.exists(f"frontend/{filename}"):
        return f"frontend/{filename}"
    return None

logo_path = get_image_path("logo.png")

# Page Config
if logo_path:
    st.set_page_config(page_title="HawkSentinel AI", page_icon=logo_path, layout="wide")
else:
    st.set_page_config(page_title="HawkSentinel AI", page_icon="🦅", layout="wide")

# ==========================================
# 2. SESSION STATE & METRICS (The "Brain")
# ==========================================

if 'history' not in st.session_state:
    st.session_state.history = []

if 'metrics' not in st.session_state:
    st.session_state.metrics = {
        "active_sessions": 2401922,
        "threats": 42,
        "latency": 38,
        "latency_delta": -12
    }

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
    # 15% Chance of Threat
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
    return "⚠️ **HAWKSENTINEL AI FORENSIC REPORT**\n\n**Threat Identified:** Account Takeover Attempt.\n**Evidence:** User session jumped 4,000km (India to Russia) in <1 minute. Device fingerprint is inconsistent with the user’s historical devices and matches a high-risk configuration profile.\n**Action Taken:** Account Auto-Frozen. 2FA Reset Link sent to verified email."

# --- LOGIC UPDATE CYCLE ---
new_log = generate_log_internal()
st.session_state.history.insert(0, new_log)
if len(st.session_state.history) > 50:
    st.session_state.history.pop()

# Dynamic Metrics Calculation
session_jitter = random.randint(-400, 800) # Mostly up, sometimes down
st.session_state.metrics['active_sessions'] += session_jitter

new_latency = random.randint(32, 45)
st.session_state.metrics['latency_delta'] = new_latency - st.session_state.metrics['latency']
st.session_state.metrics['latency'] = new_latency

threat_delta = 0
is_alert_mode = False
if new_log['risk_score'] > 90:
    st.session_state.metrics['threats'] += 1
    threat_delta = 1
    is_alert_mode = True

# ==========================================
# 3. DASHBOARD UI
# ==========================================

# HACKER STYLE CSS
st.markdown("""
    <style>
    .stApp {background-color: #0E1117;}
    div[data-testid="metric-container"] {
        background-color: #1E1E1E;
        border: 1px solid #333;
        padding: 10px;
        border-radius: 5px;
        transition: all 0.5s ease;
    }
    
    /* Custom Red Alert for Hackers */
    .stAlert {
        background-color: #2a0a0a !important;
        border: 1px solid #ff0000 !important;
        color: #ffcccc !important;
    }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR
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

# METRICS ROW (Now Dynamic)
m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Active Sessions", 
    f"{st.session_state.metrics['active_sessions']:,}", 
    f"{session_jitter:+d}"
)

m2.metric(
    "Threats Neutralized", 
    f"{st.session_state.metrics['threats']}", 
    f"+{threat_delta} Just Now" if threat_delta > 0 else "Stable",
    delta_color="off" if threat_delta == 0 else "inverse"
)

m3.metric(
    "System Latency", 
    f"{st.session_state.metrics['latency']}ms", 
    f"{st.session_state.metrics['latency_delta']}ms",
    delta_color="inverse"
)

m4.metric("AI Confidence", "99.9%", "Stable")

st.write("") # Spacer

# LIVE FEED
st.subheader("📡 Live Global Traffic Stream")

# 🚨 THREAT ALERT LOGIC
if is_alert_mode:
    st.error(f"🚨 CRITICAL_ALERT: {new_log['user']} | {new_log['details']}")
    
    # The "AI Explanation" Dropdown - Expanded by default on alert
    with st.expander("💀 READ AI FORENSIC REPORT", expanded=True):
        st.warning(get_ai_analysis_internal(new_log['id']))

# DATA TABLE
df = pd.DataFrame(st.session_state.history)

# Visual Configuration
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

# ==========================================
# 4. INTELLIGENT REFRESH (The Fix)
# ==========================================

if is_alert_mode:
    # FREEZE FOR 8 SECONDS if there is an alert
    # This gives you time to explain the alert in the video
    time.sleep(8)
else:
    # Fast refresh for normal traffic
    time.sleep(0.8)

st.rerun()
