# 📊 NYC 311 Insights Dashboard

An interactive data visualization tool for analyzing 311 service requests in New York City — with forecasting, anomaly detection, and spatial breakdown.


## 🎬 Demo Video

[Click here to watch the demo](./demo.webm)
---

## 🚀 Project Overview


This dashboard was built for the **NYC 311 Insights Challenge**, aiming to:

- 📞 Forecast daily 311 call volume  
- ⚠️ Detect unusual spikes or dips (anomalies)  
- 🗺️ Visualize complaint density across NYC boroughs  
- 📅 Explore complaint trends over time  

All insights are presented in a user-friendly, interactive dashboard using **Streamlit** and **Plotly**.
---

## 📄 Project Report

The detailed project report is available online:  
[View the NYC 311 Insights Challenge Report (Google Docs)](https://docs.google.com/document/d/1Q3DLnaxCJmABePq-903lM7xeKP1xCpmExxwm58mK-do/edit?usp=sharing)

---

## 📁 File Structure

To keep the repository size lightweight, all datasets (~2GB) are hosted externally.

📥 **Download the datasets from this Google Drive folder:**

[🔗 NYC 311 Dataset Folder (Google Drive)](https://drive.google.com/drive/folders/1cBQeMNLygLgwZ4s8O_JavRl1dmvwkly0?usp=sharing)

After downloading:

1. Place all CSV files (e.g., `daily_features.csv`, `geo_requests.csv`, etc.) into the `nyc_311_service/` directory.
2. Ensure file names and formats are not changed.

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
   git clone https://github.com/AbdulboriyAlimov/humblebee_challenge.git
   cd humblebee_challenge/nyc_311_service

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
