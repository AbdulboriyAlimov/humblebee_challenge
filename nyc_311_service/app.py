import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NYC 311 Dashboard", layout="wide")

@st.cache_data
def load_data():
    df_summary = pd.read_csv("data/daily_features.csv", parse_dates=["date"])
    df_geo = pd.read_csv("data/geo_requests.csv", parse_dates=["date"])
    return df_summary, df_geo

df_summary, df_geo = load_data()

# -------------------------
# Sidebar Filters
# -------------------------

st.sidebar.title("🔎 Filters")

# Date Range
min_date = df_summary["date"].min()
max_date = df_summary["date"].max()
date_range = st.sidebar.date_input(
    "Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date
)

# Borough Filter
available_boroughs = df_geo["borough"].dropna().unique().tolist()
selected_boroughs = st.sidebar.multiselect(
    "Select Borough(s)", available_boroughs, default=available_boroughs
)

# Complaint Type Filter
available_complaints = df_geo["complaint_type"].dropna().unique().tolist()
selected_complaints = st.sidebar.multiselect(
    "Select Complaint Type(s)", available_complaints, default=available_complaints
)

# -------------------------
# Apply Filters
# -------------------------

# Filter summary data
filtered_summary = df_summary[
    (df_summary["date"] >= pd.to_datetime(date_range[0])) &
    (df_summary["date"] <= pd.to_datetime(date_range[1]))
]

# Filter geo data
filtered_geo = df_geo[
    (df_geo["date"] >= pd.to_datetime(date_range[0])) &
    (df_geo["date"] <= pd.to_datetime(date_range[1])) &
    (df_geo["borough"].isin(selected_boroughs)) &
    (df_geo["complaint_type"].isin(selected_complaints))
]

# -------------------------
# Title
# -------------------------

st.title("📍 NYC 311 Insights Dashboard")
st.markdown("Visualizing request volume, spatial distribution, and complaint trends from 311 service data in New York City.")

# -------------------------
# 1. MAP: Density of Requests
# -------------------------

st.subheader("🗺️ Request Density Map")
if not filtered_geo.empty:
    map_fig = px.density_map(
        filtered_geo,
        lat="latitude",
        lon="longitude",
        radius=15,
        center=dict(lat=40.7128, lon=-74.0060),
        zoom=9,
        map_style="carto-positron",
        hover_data=["borough", "date", "complaint_type"]
    )
    st.plotly_chart(map_fig, use_container_width=True)
else:
    st.info("No geographic request data for the selected filters.")

# -------------------------
# 2. LINE: Daily Call Volume
# -------------------------

st.subheader("📈 Daily 311 Call Volume")
if not filtered_summary.empty:
    daily_calls = filtered_summary.groupby("date")["total_calls"].sum().reset_index()
    line_fig = px.line(daily_calls, x="date", y="total_calls", title="Daily Call Volume")
    st.plotly_chart(line_fig, use_container_width=True)
else:
    st.info("No call volume data available.")

# -------------------------
# 3. BAR: Complaint Type Breakdown (from geo data)
# -------------------------

st.subheader("📊 Complaint Type Breakdown")
if not filtered_geo.empty:
    complaint_counts = filtered_geo["complaint_type"].value_counts().reset_index()
    complaint_counts.columns = ["Complaint Type", "Count"]
    bar_fig = px.bar(complaint_counts, x="Complaint Type", y="Count", title="Most Common Complaints")
    st.plotly_chart(bar_fig, use_container_width=True)
else:
    st.info("Complaint breakdown not available for selected filters.")

# -------------------------
# 4. PIE: Borough Distribution (Geo-based)
# -------------------------

st.subheader("🏙️ Borough-wise Request Share")
borough_counts = filtered_geo["borough"].value_counts().reset_index()
borough_counts.columns = ["borough", "count"]
if not borough_counts.empty:
    pie_fig = px.pie(borough_counts, names="borough", values="count", title="Request Distribution by Borough")
    st.plotly_chart(pie_fig, use_container_width=True)
else:
    st.info("No borough distribution data available.")

# -------------------------
# Footer
# -------------------------

st.markdown("---")
st.markdown("✅ Built for the *NYC 311 Insights Challenge* — powered by Streamlit, Plotly, and Open NYC Data.")
