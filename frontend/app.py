import streamlit as st
import pandas as pd
import requests
import time

# CONFIG
API_URL = "http://localhost:8001"
st.set_page_config(
    page_title="HawkSentinel AI", 
    page_icon="🦅", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# HACKER STYLE CSS
st.markdown("""
    <style>
    .stApp {background-color: #050505;}
    
    /* Cool Metrics Styling */
    div[data-testid="metric-container"] {
        background-color: #111;
        border: 1px solid #222;
        padding: 15px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    div[data-testid="metric-container"]:hover {
        border-color: #4CAF50;
        box-shadow: 0 0 15px rgba(76, 175, 80, 0.3);
    }
    
    /* Headers */
    h1, h2, h3 { color: #f0f0f0; }
    
    /* Custom Red Alert for Hackers */
    .stAlert {
        background-color: #2a0a0a !important;
        border: 1px solid #ff0000 !important;
        color: #ffcccc !important;
    }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR CONTROLS
with st.sidebar:
    # Logo in Sidebar
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

# MAIN HEADER
col_logo, col_title = st.columns([1.5, 8.5])
with col_logo:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.header("🛡️")
with col_title:
    st.title("HawkSentinel AI")
    st.caption("⚡ Autonomous Real-Time Account Security Watchdog")

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

while True:
    try:
        # Get Data
        new_log = requests.get(f"{API_URL}/stream").json()
        history = requests.get(f"{API_URL}/history").json()
        df = pd.DataFrame(history)

        with placeholder.container():
            # 🚨 THREAT ALERT LOGIC
            if new_log['risk_score'] > 90:
                st.error(f"🚨 CRITICAL SECURITY ALERT: {new_log['user']} | {new_log['details']}")
                
                # The "AI Explanation" Dropdown
                with st.expander("🤖 READ AI FORENSIC REPORT", expanded=True):
                    analysis = requests.get(f"{API_URL}/analyze?log_id={new_log['id']}").json()
                    st.markdown(analysis['analysis'])
            
            # SHOW TABLE (SINGLE INSTANCE)
            styled_df = df[['time', 'user', 'location', 'device', 'status', 'risk_score']].style.apply(
                lambda x: ['background-color: #2a0a0a; color: #ffeb3b; font-weight: bold' if x['risk_score'] > 90 else '' for i in x], 
                axis=1
            )
            
            st.dataframe(
                styled_df,
                column_config={
                    "risk_score": st.column_config.ProgressColumn(
                        "Risk Level",
                        help="AI Risk Assessment (0-100)",
                        format="%d%%",
                        min_value=0,
                        max_value=100,
                    ),
                    "status": st.column_config.TextColumn("Status"),
                    "device": st.column_config.TextColumn("Device Type"),
                    "location": st.column_config.TextColumn("Geo-Location"),
                },
                use_container_width=True,
                hide_index=True
            )
            
        time.sleep(1) # Refresh rate

    except Exception as e:
        st.warning(f"Connecting to Neural Backend... ({e})")
        time.sleep(3)
