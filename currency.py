
import streamlit as st

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title("25 💱 Currency to PKR Converter")
st.write("Convert any of these currencies into Pakistani Rupees (PKR).")

# --- Currency Rates to PKR (example rates, update as needed) ---
rates = {
    "USD": 285,    # US Dollar
    "EUR": 310,    # Euro
    "GBP": 360,    # British Pound
    "JPY": 2.1,    # Japanese Yen
    "CAD": 215,    # Canadian Dollar
    "AUD": 200,    # Australian Dollar
    "CHF": 320,    # Swiss Franc
    "CNY": 40,     # Chinese Yuan
    "INR": 3.5,    # Indian Rupee
    "PKR": 1,      # Pakistani Rupee
    "SGD": 210,    # Singapore Dollar
    "NZD": 190,    # New Zealand Dollar
    "SEK": 28,     # Swedish Krona
    "NOK": 27,     # Norwegian Krone
    "KRW": 0.21,   # South Korean Won
    "TRY": 16,     # Turkish Lira
    "RUB": 3.5,    # Russian Ruble
    "BRL": 55,     # Brazilian Real
    "MXN": 16,     # Mexican Peso
    "ZAR": 15,      # South African Rand
    "ILS": 85,     # Israeli Shekel
    "Indonesian Rupiah": 0.019, # Indonesian Rupiah
    "INR": 3.5,    # Indian Rupee
    "Riyal": 76,    # Saudi Riyal
    "Dirham": 78     # UAE Dirham
}

# --- User Input ---
amount = st.number_input("Enter Amount:", min_value=0.0, step=1.0)

currency = st.selectbox(
    "Select Currency:",
    list(rates.keys())
)

# --- Conversion ---
if st.button("Convert"):
    rate = rates[currency]
    result = amount * rate
    st.success(f"{amount} {currency} = {result} PKR")
