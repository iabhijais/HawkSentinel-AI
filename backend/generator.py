import random
import time
from datetime import datetime

# Fake Locations
LOCATIONS = [
    {"country": "India", "city": "Kanpur", "ip": "103.211.55."},
    {"country": "India", "city": "Mumbai", "ip": "103.211.60."},
    {"country": "USA", "city": "New York", "ip": "45.76.12."},
    {"country": "Russia", "city": "Moscow", "ip": "185.17.44."},  # Hacker Node
    {"country": "China", "city": "Beijing", "ip": "202.108.33."}  # Hacker Node
]

DEVICES = ["Windows 11", "MacBook Pro", "iPhone 15", "Linux (Kali)", "Unknown Android"]

def generate_log():
    # 85% Safe, 15% Hacker Attack
    is_threat = random.random() > 0.85
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    if is_threat:
        # THE ATTACK SCENARIO
        user_id = "User_9982_VIP" # High Value Target
        loc = LOCATIONS[3] # Moscow (Suspicious)
        device = "Linux (Kali)" # Hacker OS
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

    log = {
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
    return log
