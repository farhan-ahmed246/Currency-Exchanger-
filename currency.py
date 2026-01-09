import streamlit as st

st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

st.title("💱 25 Currency to PKR Converter")
st.write("Convert 25 international currencies into Pakistani Rupees (PKR)")

# --- Currency Rates to PKR (example static rates) ---
rates = {
    "USD - US Dollar": 285,
    "EUR - Euro": 310,
    "GBP - British Pound": 360,
    "JPY - Japanese Yen": 2.1,
    "CAD - Canadian Dollar": 215,
    "AUD - Australian Dollar": 200,
    "CHF - Swiss Franc": 320,
    "CNY - Chinese Yuan": 40,
    "INR - Indian Rupee": 3.5,
    "SGD - Singapore Dollar": 210,
    "NZD - New Zealand Dollar": 190,
    "SEK - Swedish Krona": 28,
    "NOK - Norwegian Krone": 27,
    "KRW - South Korean Won": 0.21,
    "TRY - Turkish Lira": 16,
    "RUB - Russian Ruble": 3.5,
    "BRL - Brazilian Real": 55,
    "MXN - Mexican Peso": 16,
    "ZAR - South African Rand": 15,
    "ILS - Israeli Shekel": 85,
    "IDR - Indonesian Rupiah": 0.019,
    "SAR - Saudi Riyal": 76,
    "AED - UAE Dirham": 78,
    "MYR - Malaysian Ringgit": 65,
    "THB - Thai Baht": 8
}

# --- User Input ---
amount = st.number_input("Enter Amount", min_value=0.0, step=1.0)

currency = st.selectbox(
    "Select Currency",
    list(rates.keys())
)

# --- Conversion ---
if st.button("Convert 💰"):
    rate = rates[currency]
    result = amount * rate
    st.success(f"{amount} → {result:.2f} PKR")
