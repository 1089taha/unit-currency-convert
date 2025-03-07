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
   git clone https://github.com/yourusername/unit-currency-converter.git
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

4. **Run the Application**
  ```bash
  streamlit run app.py


## 🔑 Environment Variables / API Keys

The app uses ExchangeRate-API for live currency conversion.

🆓 Get a free API key: ExchangeRate-API Signup

## 🚀 Usage

1. Select a Conversion Category from the sidebar (currency, temperature, length, etc.).

2. Enter Values & Choose Units for conversion.

3. Click "Convert" to see results instantly.

4. View Conversion History and generate interactive graphs.


## 🛠️ Technologies Used

1. **Python 🐍**: Core logic and calculations

2. **Streamlit 🎈**: Web app interface

3. **Requests 🌐**: API calls to ExchangeRate-API

4. **Matplotlib 📊**: Graph visualization for conversion history

5. **Pandas** 📈: Data handling for historical records


## 📞 Contact

For questions, issues, or feature requests:
📧 Email: tahakhalid317@gmail.com
