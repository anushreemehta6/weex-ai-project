# WXT Risk Shield – WEEX AI Trading Protection

WXT Risk Shield is an AI-powered risk management and capital protection layer built using WEEX Exchange APIs.  
The project demonstrates how AI can proactively prevent high-risk trades and protect user funds before losses occur.

---

## Problem Statement

Most crypto traders lose money due to:
- High market volatility
- Over-leveraged or emotional trading
- No real-time risk checks before order execution

Current exchanges execute trades instantly, even during extreme risk conditions.

---

## Solution

WXT Risk Shield acts as a pre-trade AI guardian that:
- Monitors market volatility
- Calculates a real-time risk score
- Blocks trades when risk exceeds a safe threshold
- Clearly shows capital saved due to AI intervention

This improves user safety and trust on the WEEX platform.

---

## How AI Is Used

### Volatility Prediction
- Recent price movements are analyzed
- Statistical volatility is calculated
- Output feeds into the risk engine

### Risk Engine
- Inputs:
  - Market volatility
  - User exposure
- Output:
  - Risk score (0–1)

### Decision Engine
- SAFE → Trade allowed
- BLOCKED → Trade prevented to protect capital

---

## Project Flow

1. Fetch real balance and positions using WEEX API  
2. Predict market volatility using AI logic  
3. Calculate risk score  
4. Decide whether trading should be allowed  
5. Display results on an interactive dashboard  

---

## Features

- WEEX API integration (Balance & Positions)
- AI-based volatility analysis
- Real-time risk scoring
- Trade blocking simulation
- Capital protection visualization
- Streamlit-based dashboard

---

## Dashboard Highlights

- Live USDT balance
- AI volatility score
- Risk score indicator
- System decision (SAFE / BLOCKED)
- Risk trend graph
- Capital saved simulation

---

## Tech Stack

- Python
- WEEX Exchange APIs
- Streamlit
- Pandas, NumPy
- HMAC API authentication

---

## WEEX APIs Used

- Account Balance API  
- Position API  
- Market Data API  

Authenticated using:
- API Key
- Secret Key
- Passphrase

---

## Role of WXT Token (Future Scope)

- Advanced AI protection unlocked via WXT staking
- Fee discounts for protected trades
- WXT-based incentives for safe trading behavior

This increases WXT utility within the WEEX ecosystem.

---

## Hackathon Demo Explanation

- Show expected loss without AI protection

- Show zero loss with WXT Risk Shield enabled

- Explain how the AI blocked risky trades

- Highlight capital saved in USDT

# Run dashboard
streamlit run dashboard/app.py
