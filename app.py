import sys
import os
import time
import random
import streamlit as st
import pandas as pd
import json


# ---------------- FIX IMPORT PATH ----------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from bot.account import get_balance, get_position
from bot.ai_model import predict_volatility
from bot.risk_engine import calculate_risk
from bot.decision import risk_action

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="WXT Risk Shield",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- HEADER ----------------
st.markdown("## 🛡️ WXT Risk Shield – WEEX AI Trading")
st.caption("AI-powered capital protection layer for WEEX traders")
st.divider()

# ---------------- FETCH DATA ----------------
balance_status, balance_raw = get_balance()
positions_status, positions_raw = get_position()

balance = 0.0

if balance_raw:
    if isinstance(balance_raw, str):
        balance_list = json.loads(balance_raw)
    else:
        balance_list = balance_raw

    if len(balance_list) > 0:
        balance = float(balance_list[0].get("available", 0))


volatility = predict_volatility()
risk_score = calculate_risk(volatility)
decision = risk_action(risk_score)

# ---------------- METRICS ----------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Balance (USDT)", f"{balance:.2f}")
c2.metric("📉 Risk Score", f"{risk_score:.4f}")
c3.metric("⚡ Volatility (AI)", f"{volatility:.5f}")
c4.metric("🧠 AI Status", "ACTIVE" if decision == "SAFE" else "BLOCKED")

# ---------------- RISK MONITOR ----------------
st.divider()
st.subheader("📈 AI Risk Monitor")

risk_data = pd.DataFrame({
    "Time": list(range(20)),
    "Risk": [max(0, risk_score + random.uniform(-0.002, 0.002)) for _ in range(20)]
})

st.line_chart(risk_data.set_index("Time"))

# ---------------- PROTECTION SIMULATION ----------------
st.divider()
st.subheader("🛡️ Protection Simulation")

simulated_loss = balance * risk_score * 3

left, right = st.columns(2)

with left:
    st.error("❌ Without AI Protection")
    st.write(f"**Expected Loss:** {simulated_loss:.2f} USDT")
    st.write("**Trade Allowed:** Yes")
    st.write("**Liquidation Risk:** High")

with right:
    st.success("✅ With WXT Risk Shield")
    st.write("**Expected Loss:** 0 USDT")
    st.write("**Trade Allowed:** No")
    st.write(f"**Capital Saved:** {simulated_loss:.2f} USDT")

# ---------------- DECISION LOG ----------------
st.divider()
st.subheader("🧠 AI Decision Log")

logs = [
    "Market volatility detected",
    "AI risk model evaluated conditions",
    f"Risk score computed: {risk_score:.4f}",
    f"Decision taken: {decision}",
    "Capital protection enforced"
]

for log in logs:
    st.write(f"• {log}")
    time.sleep(0.05)

# ---------------- FINAL STATUS ----------------
st.divider()

if decision == "SAFE":
    st.success("🟢 System Status: SAFE — Trading Allowed")
else:
    st.warning("🛑 System Status: HIGH RISK — Trading Blocked")

# ---------------- TRADE ATTEMPT SIMULATION ----------------
st.divider()
st.subheader("🚀 Simulated Trade Attempt")

st.caption("Demonstrates how AI actively blocks risky trades in real time")

trade_amount = st.slider(
    "Select Trade Size (USDT)",
    min_value=50,
    max_value=500,
    value=200,
    step=50
)

if st.button("⚠️ Attempt Trade"):
    st.markdown("### 🔍 AI Pre-Trade Risk Check")

    estimated_loss = trade_amount * risk_score * 3

    if decision == "BLOCK":
        st.error("🛑 Trade Blocked by AI Risk Engine")

        st.write(f"**Reason:** Market volatility too high")
        st.write(f"**Risk Score:** {risk_score:.4f}")
        st.write(f"**Potential Loss Prevented:** {estimated_loss:.2f} USDT")

        st.success("🛡️ Capital successfully protected by WXT Risk Shield")

    else:
        st.success("✅ Trade Approved by AI")
        st.write("**Risk Level:** Acceptable")
        st.write("**Trade Executed Successfully (Simulated)**")

# ---------------- WXT UTILITY SECTION ----------------
st.divider()
st.subheader("🪙 WXT Utility – Powering Risk Shield")

st.markdown("""
### Why WXT Matters in This System

**WXT Risk Shield** is designed as a **premium protection layer** inside the WEEX ecosystem.

Holding or staking **WXT tokens** unlocks advanced AI-driven safeguards that protect traders from high-risk market conditions.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
#### 🔐 WXT-Powered Features
- 🛡️ **AI Capital Protection**  
  Automatically blocks trades during extreme volatility  

- 💸 **Reduced Trading Fees**  
  Risk-protected trades receive fee discounts  

- ⚡ **Faster Risk Evaluation**  
  Priority AI execution for WXT holders  
""")

with col2:
    st.markdown("""
#### 🚀 Benefits for WEEX Ecosystem
- 📉 Lower user liquidation rates  
- 📈 Higher user trust & retention  
- 🔄 Increased WXT utility & demand  
- 🏦 Safer trading environment  
""")

st.info(
    "🔑 Concept: Users who stake WXT receive stronger AI protection thresholds, "
    "while non-stakers operate with basic risk limits."
)
