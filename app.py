import streamlit as st
import requests
import matplotlib.pyplot as plt

# API Key for currency conversion
API_KEY = st.secrets["api"]["API_KEY"]

def get_exchange_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"].get(to_currency, None)

# Define unit conversion function
def unit_converter(category, value, unit):
    conversions = {
        "Length": {"Kilometers to Miles": 0.621371, "Miles to Kilometers": 1.60934},
        "Weight": {"Kilograms to Pounds": 2.20462, "Pounds to Kilograms": 0.453592},
        "Time": {
            "Seconds to Minutes": 1/60, "Minutes to Seconds": 60,
            "Minutes to Hours": 1/60, "Hours to Minutes": 60,
            "Hours to Days": 1/24, "Days to Hours": 24
        }
    }
    return value * conversions.get(category, {}).get(unit, 1)

# Set Streamlit theme
st.set_page_config(
    page_title="Unit/Currency Converter",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for category selection
st.sidebar.title("🌍 Conversion Categories")
category = st.sidebar.radio("Select Category", ["Currency", "Length", "Weight", "Time"])

st.title("🌏 Unit & Currency Converter")
st.markdown("### Convert currency, length, weight, and time with ease! 🚀🚀")

# Initialize value and unit
value = 0  
unit = None  

# Initialize history storage if not available
if "history" not in st.session_state:
    st.session_state.history = []

if category == "Currency":
    st.subheader("💰 Currency Converter")
    from_currency = st.selectbox("From Currency", ["USD", "PKR", "INR", "SAR", "AED", "GBP", "EUR", "BDT", "CNY", "JPY"])
    to_currency = st.selectbox("To Currency", ["USD", "PKR", "INR", "SAR", "AED", "GBP", "EUR", "BDT", "CNY", "JPY"])
    amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")

    if st.button("Convert Currency"):
        rate = get_exchange_rate(from_currency, to_currency)
        if rate:
            converted_amount = amount * rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            
            # ✅ Store currency conversion history
            st.session_state.history.append((amount, converted_amount))
        else:
            st.error("Failed to fetch exchange rate")
else:
    if category == "Length":
        st.subheader("📏 Length Converter")
    elif category == "Weight":
        st.subheader("⚖️ Weight Converter")
    elif category == "Time":
        st.subheader("⏳ Time Converter")
    
    value = st.number_input("Enter value to convert")  

    if category == "Length":
        unit = st.selectbox("Select a unit", ["Kilometers to Miles", "Miles to Kilometers"])
    elif category == "Weight":
        unit = st.selectbox("Select a unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
    elif category == "Time":
        unit = st.selectbox("Select a unit", ["Minutes to Seconds", "Seconds to Minutes", "Minutes to Hours", "Hours to Minutes", "Days to Hours", "Hours to Days"])

    if st.button("Convert"):
        result = unit_converter(category, value, unit)
        st.success(f"{value} converted to {result:.2f}")
        
        # ✅ Store unit conversion history
        st.session_state.history.append((value, result))

# 📊 Show Graph for both Currency & Unit Conversions
st.header("📊 Conversion History")

if st.button("Show Graph") and st.session_state.history:
    fig, ax = plt.subplots()
    values = [item[0] for item in st.session_state.history]
    results = [item[1] for item in st.session_state.history]

    ax.plot(values, results, marker="o", linestyle="-", color="#ff4b4b", linewidth=2, markersize=8)  
    ax.set_xlabel("Input Value", fontsize=12, fontweight="bold")
    ax.set_ylabel("Converted Value", fontsize=12, fontweight="bold")
    ax.set_title("Conversion History", fontsize=14, fontweight="bold")

    ax.grid(True, linestyle="--", alpha=0.6)
    plt.style.use("ggplot")

    st.pyplot(fig)
else:
    st.warning("Convert a value first before showing the graph.")
