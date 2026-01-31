import streamlit as st
import requests

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

# -----------------------------
# CSS for Modern Card + Bars
# -----------------------------
st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#0f2027,#203a43,#2c5364); color:#fff;}
.card {background: rgba(255,255,255,0.1); backdrop-filter: blur(15px); padding:30px; border-radius:20px; max-width:700px; margin:20px auto; text-align:center; box-shadow:0 15px 30px rgba(0,0,0,0.5);}
.stButton>button {background: linear-gradient(135deg,#ff6a00,#ee0979); color:#fff; font-weight:bold; padding:10px 20px; border-radius:12px; border:none;}
.stButton>button:hover {transform: translateY(-2px);}
.bar {height:12px; border-radius:6px; background: linear-gradient(90deg,#ff6a00,#ee0979); margin-left:10px; flex-grow:1;}
.rank-item {display:flex; align-items:center; margin:5px 0; padding:5px; background: rgba(255,255,255,0.05); border-radius:8px;}
.arrow-up {color:#00ff00; font-weight:bold;}
.arrow-down {color:#ff0000; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("## Currency Converter")

# -----------------------------
# Fetch Live Rates
# -----------------------------
@st.cache_data(ttl=300)
def fetch_rates(base="USD"):
    try:
        data = requests.get(f"https://open.er-api.com/v6/latest/{base}", timeout=10).json()
        if data.get("result")=="success":
            return data.get("rates",{}), data.get("time_last_update_utc")
        return None,None
    except:
        return None,None

rates, last_update = fetch_rates("USD")  # Base USD for simplicity
if not rates:
    st.error("❌ Failed to fetch rates.")
    st.stop()

# -----------------------------
# Session state for previous rates
# -----------------------------
if "prev_rates" not in st.session_state:
    st.session_state.prev_rates = rates.copy()

# -----------------------------
# Dropdowns
# -----------------------------
from_currency = st.selectbox(
    "From Currency:",
    sorted(rates.keys()),
    index=list(sorted(rates.keys())).index("USD")
)

to_currency = st.selectbox(
    "To Currency:",
    sorted(rates.keys()),
    index=list(sorted(rates.keys())).index("PKR")
)

# -----------------------------
# Dynamic placeholder for any currency
# -----------------------------
if from_currency == to_currency:
    placeholder_text = "Enter Amount"
else:
    placeholder_text = f"Enter Amount (1 {from_currency} = {round(rates[to_currency]/rates[from_currency],2)} {to_currency})"

amount = st.number_input(
    "Enter Amount:",
    min_value=0.0,
    step=1.0,
    key="amount_input",
    format="%.2f",
    placeholder=placeholder_text
)

# -----------------------------
# Conversion
# -----------------------------
if st.button("Convert"):
    if from_currency == to_currency:
        result = amount
    else:
        result = amount * rates[to_currency] / rates[from_currency]
    st.success(f"{amount} {from_currency} = {round(result,2)} {to_currency}")

# -----------------------------
# Currency Ranking with Bars + Arrows
# -----------------------------
st.markdown("---")
st.subheader("Currency Ranking (Compared to USD)")

sorted_rates = sorted(rates.items(), key=lambda x: x[1], reverse=True)
max_val = sorted_rates[0][1]

for idx, (curr, val) in enumerate(sorted_rates, start=1):
    prev_val = st.session_state.prev_rates.get(curr, val)
    arrow = ""
    if val > prev_val: arrow = '<span class="arrow-up">↑</span>'
    elif val < prev_val: arrow = '<span class="arrow-down">↓</span>'
    bar_width = (val/max_val)*100
    st.markdown(f'''
    <div class="rank-item">
        {idx}. {curr}: {round(val,2)} {from_currency} {arrow}
        <div class="bar" style="width:{bar_width}%"></div>
    </div>
    ''', unsafe_allow_html=True)

# Save current rates for next comparison
st.session_state.prev_rates = rates.copy()

if last_update:
    st.caption(f"Last updated (UTC): {last_update}")
st.markdown('</div>', unsafe_allow_html=True)
