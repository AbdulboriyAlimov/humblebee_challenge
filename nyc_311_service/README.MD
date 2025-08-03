# 📊 NYC 311 Insights Dashboard

An interactive data visualization tool for analyzing 311 service requests in New York City — with forecasting, anomaly detection, and spatial breakdown.

---

## 🚀 Project Overview

## 🎬 Demo Video

[Click here to watch the demo](./demo.webm)

This dashboard was built for the **NYC 311 Insights Challenge**, aiming to:

- 📞 Forecast daily 311 call volume  
- ⚠️ Detect unusual spikes or dips (anomalies)  
- 🗺️ Visualize complaint density across NYC boroughs  
- 📅 Explore complaint trends over time  

All insights are presented in a user-friendly, interactive dashboard using **Streamlit** and **Plotly**.

---

## 📁 File Structure

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit app |
| `daily_features.csv` | Daily aggregated features (calls, complaints, holidays, etc.) |
| `geo_requests.csv` | Geolocated 311 request data |
| `submission.csv` | Forecasted call volume (for competition) |
| `anomalies.csv` | Top anomalies (spikes and dips in call volume) |
| `README.md` | Project documentation (this file) |
| `demo.webm` | Demonstration of our Dashboard |
| `requirements.txt` | Requested libraries to reproduce our results|

---

## 🔧 How to Run the Dashboard

1. Clone the repository and navigate to the folder:
   ```bash
   git clone https://github.com/your-username/nyc-311-dashboard.git
   cd nyc-311-dashboard

2. pip install -r requirements.txt

3. streamlit run app.py


## 📊 Dashboard Features

## ✅ Filters

    Date Range

    Boroughs

## 🗺️ Request Density Map

    Interactive NYC map with spatial complaint density

## 📈 Daily Call Volume

    Line chart showing call trends over time

## 📊 Complaint Type Breakdown

    Bar chart summarizing complaint categories

## 🏙️ Borough-wise Distribution

    Pie chart of request counts per borough

## 📌 Anomalies CSV

    Identifies top 5 spikes and dips in 311 volume

    Flags holidays in the "Note" column automatically

## 📦 Tech Stack

    Python

    Streamlit

    Plotly

    Pandas

    XGBoost

    scikit-learn
