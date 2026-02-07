# 🦅 HawkSentinel AI
### Deriv AI Talent Sprint 2026 - Hackathon Entry

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![License](https://img.shields.io/badge/License-MIT-green)

---

### 1. 📋 PROJECT MANIFEST
* **Project Name:** HawkSentinel AI
* **Tagline:** Autonomous Real-Time Account Security Watchdog
* **Target Track:** Security / Anti-Fraud / Compliance
* **Mission:** To protect Deriv's 2.5M+ users from Account Takeovers (ATOs) and Unauthorized Access using real-time behavioral analysis and AI reasoning.
* **Core Philosophy:** "Speed Wins." Humans cannot review logins fast enough. HawkSentinel detects and blocks hackers in <500ms.

---

### 2. ⚠️ THE PROBLEM (Deriv Use Case)
Deriv operates globally. The biggest threat to user trust is **Account Compromise** (Hackers stealing credentials).

* **Challenge:** Distinguishing between a legitimate user traveling vs. a hacker using a stolen session cookie from a different country.
* **Current Solution:** Static rules (often slow or block real users).
* **HawkSentinel Solution:** A live "Security Stream" that flags **Impossible Travel** (Speed violations) and **Device Anomalies** instantly, using LLMs to generate human-readable incident reports.

---

### 3. 🏗️ TECHNICAL ARCHITECTURE
* **Type:** Full-Stack Data Application
* **Frontend:** Streamlit (Python) - For a high-performance, "Matrix-style" Dark Mode Security Dashboard.
* **Backend API:** FastAPI (Python) - Serves the live log stream.
* **Data Engine:** Synthetic Log Generator (Python) - Simulates 2.5M users and injects specific "Hacker Scenarios."
* **AI Engine:** LLM Integration (Gemini/OpenAI) - Generates "Security Incident Reports" for high-risk events.

---

### 🚀 HOW TO RUN
**Prerequisites:** Python 3.9+

1. **Clone & Setup:**
   ```bash
   git clone https://github.com/yourusername/HawkSentinel.git
   cd HawkSentinel
   pip install -r requirements.txt
   ```

2. **Start the Backend (The Engine):**
   ```bash
   cd backend
   python main.py
   ```

3. **Launch the Dashboard (The Interface):**
   ```bash
   cd frontend
   streamlit run app.py
   ```
