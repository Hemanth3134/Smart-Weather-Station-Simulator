# 🌦️ Smart Weather Station Simulator

A full-featured weather station simulator that generates synthetic weather data, detects anomalies, forecasts future conditions, and provides automated reports and alerts.

---

## 🔧 Features

- 🌡️ Simulates **temperature**, **humidity**, and **windspeed**
- 🌪️ Injects **heatwaves** and **storms** on demand
- 🧠 Detects anomalies using **Isolation Forest**
- ⏱️ Forecasts next 24 hours with **ARIMA**
- 📝 Auto-generates **PDF weather reports**
- 📬 Sends **Telegram alerts** on anomalies
- 🗃️ Stores historical data in **SQLite**
- 📊 Interactive **Streamlit dashboard**

---

## 📁 Project Structure

smart-weather-station

├── main.py # Entry point for Streamlit UI

├── test.py # Telegram alert test script

├── app

│ └── ui.py # Streamlit UI rendering logic (expected)

├── weather_report.pdf # Sample generated weather report

├── requirements.txt # Python dependencies


---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-weather-station.git
cd smart-weather-station
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run main.py
```


---

## 🧪 Telegram Bot Test

Ensure your Telegram BOT_TOKEN and CHAT_ID are correctly set in test.py, then run:
```bash
python test.py
```


---

## 📄 Sample Output

**weather_report.pdf** contains:

Detected anomalies

Maximum recorded temperature

Timestamped anomaly data

Example excerpt:

| Timestamp           | Temp (°C) | Windspeed | Anomaly |
| ------------------- | --------- | --------- | ------- |
| 2024-01-07 02:00:00 | 21.29     | 35.37     | ✅       |
| 2024-01-07 06:00:00 | 46.58     | 10.34     | ✅       |
| 2024-01-09 20:00:00 | 27.86     | 30.68     | ✅       |


---

## 📦 Dependencies

See requirements.txt. Major libraries include:

streamlit

numpy, pandas

scikit-learn, statsmodels

matplotlib

fpdf

python-telegram-bot

