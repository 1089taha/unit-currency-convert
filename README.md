# 🌍 Unit & Currency Converter

## 📌 Project Description
A simple and interactive web application built with Streamlit that allows users to convert currencies, length, weight, and time effortlessly. The app fetches real-time exchange rates and also maintains a conversion history with graphical representation.

## ✨ Features
- 🔄 **Currency Conversion** using real-time exchange rates.
- 📏 **Unit Conversion** for length, weight, and time.
- 📊 **Conversion History** with graphical visualization.
- 🎨 **User-friendly Interface** powered by Streamlit.
- 🔒 **Secure API Key Management** using Streamlit Secrets.

## 🛠️ Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/1089taha/unit-currency-convert.git
   cd unit-currency-converter

2. **Create a Virtual Environment & Activate**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables**
   ```bash
   [api]
   API_KEY = "your_exchange_rate_api_key_here"

# Unit & Currency Converter 🌍💱

This is a web-based unit and currency converter built using **Python** and **Streamlit**. It supports multiple conversion categories such as currency, length, weight, and temperature.

---

## 📌 Features
✔️ Convert between different units (Currency, Length, Weight, Temperature).  
✔️ Live currency conversion using **ExchangeRate-API**.  
✔️ View **conversion history** with interactive graphs.  
✔️ Clean and user-friendly interface with **Streamlit**.  

---

## 🚀 Usage Guide

1️⃣ **Select a Conversion Category** from the sidebar (Currency, Temperature, Length, etc.).  
2️⃣ **Enter a Value & Choose Units** for conversion.  
3️⃣ Click **"Convert"** to see results instantly.  
4️⃣ View **Conversion History** and generate **interactive graphs**.  

---

## 🔧 Technologies Used

- **Python 🐍** → Core logic and calculations  
- **Streamlit 🎈** → Web app interface  
- **Requests 🌐** → API calls to ExchangeRate-API  
- **Matplotlib 📊** → Graph visualization for conversion history  
- **Pandas 📈** → Data handling for historical records  

---

## 🔑 API Key Setup

This app requires an API key from **ExchangeRate-API** for live currency conversion.  

🔗 [Get a Free API Key Here](https://www.exchangerate-api.com/)  

Once you have the API key, add it to your environment variables.

---

## ▶️ Run the Application

```bash
streamlit run app.py


## 📞 Contact

For questions, issues, or feature requests:
📧 Email: tahakhalid317@gmail.com
