# 📊 NYC 311 Insights Dashboard

An interactive data visualization tool for analyzing 311 service requests in New York City — with forecasting, anomaly detection, and spatial breakdown.

---

## 🚀 Project Overview

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

---

## 🔧 How to Run the Dashboard

1. Clone the repository and navigate to the folder:
   ```bash
   git clone https://github.com/your-username/nyc-311-dashboard.git
   cd nyc-311-dashboard
