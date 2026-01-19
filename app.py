
import streamlit as st
import pandas as pd

# =========================
# Page title
# =========================
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("🚲 Bike Sharing Dashboard")
st.markdown("### MY DASHBOARD TEST ✅")

# =========================
# Load dataset
# =========================
df = pd.read_csv("train.csv")

# Convert datetime
df["datetime"] = pd.to_datetime(df["datetime"])

# Create new time columns
df["hour"] = df["datetime"].dt.hour
df["month"] = df["datetime"].dt.month

# =========================
# Sidebar filters (INTERACTIVE WIDGETS)
# =========================
st.sidebar.header("Filters")

season = st.sidebar.selectbox(
    "Select Season",
    options=sorted(df["season"].unique())
)

workingday = st.sidebar.selectbox(
    "Working Day",
    options=["All", 0, 1]
)

weather = st.sidebar.selectbox(
    "Weather",
    options=["All"] + sorted(df["weather"].unique().tolist())
)

# Apply filters
filtered_df = df[df["season"] == season]

if workingday != "All":
    filtered_df = filtered_df[filtered_df["workingday"] == workingday]

if weather != "All":
    filtered_df = filtered_df[filtered_df["weather"] == weather]

# =========================
# Dataset Preview
# =========================
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

# =========================
# Basic Statistics
# =========================
st.subheader("Basic Statistics")
st.dataframe(filtered_df.describe())

# =========================
# PLOT 1: Average Bike Rentals by Hour
# =========================
st.subheader("📈 Average Bike Rentals by Hour")

avg_by_hour = filtered_df.groupby("hour")["count"].mean()
st.line_chart(avg_by_hour)

# =========================
# PLOT 2: Average Rentals by Season
# =========================
st.subheader("📊 Average Rentals by Season")

season_avg = df.groupby("season")["count"].mean()
st.bar_chart(season_avg)

# =========================
# PLOT 3: Average Rentals by Working Day
# =========================
st.subheader("📊 Average Rentals by Working Day")

workingday_avg = df.groupby("workingday")["count"].mean()
st.bar_chart(workingday_avg)

# =========================
# PLOT 4: Average Rentals by Weather
# =========================
st.subheader("📊 Average Rentals by Weather")

weather_avg = df.groupby("weather")["count"].mean()
st.bar_chart(weather_avg)

# =========================
# PLOT 5: Average Rentals by Month
# =========================
st.subheader("📈 Average Rentals by Month")

month_avg = df.groupby("month")["count"].mean()
st.line_chart(month_avg)

# =========================
# Conclusion
# =========================
st.markdown("### ✅ Dashboard Completed Successfully")
st.markdown(
    """
    This interactive dashboard analyzes bike-sharing demand using:
    - Multiple visualizations
    - Interactive filters
    - Summary statistics
    """
)