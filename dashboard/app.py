import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Marketing ROI Dashboard", page_icon="📈", layout="wide")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', 'data', 'processed', 'cleaned_marketing_data.csv')
    try:
        df = pd.read_csv(data_path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        st.error(f"Cannot find data at {data_path}. Please run data generation scripts first.")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Data")
channel_filter = st.sidebar.multiselect(
    "Select Channel:",
    options=df["Channel"].unique(),
    default=df["Channel"].unique()
)

region_filter = st.sidebar.multiselect(
    "Select Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

# Date filter
min_date = df["Date"].min().date()
max_date = df["Date"].max().date()
date_range = st.sidebar.date_input(
    "Select Date Range:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Apply filters
if len(date_range) == 2:
    start_date, end_date = date_range
    # convert date_range items to datetime to compare
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    mask = (
        (df["Channel"].isin(channel_filter)) &
        (df["Region"].isin(region_filter)) &
        (df["Date"] >= start_date) &
        (df["Date"] <= end_date)
    )
    filtered_df = df[mask]
else:
    filtered_df = df

st.title("📊 Marketing Campaign Performance & ROI Analytics")
st.markdown("Monitor campaign effectiveness, ROI, and core metrics across multiple channels.")

# --- KPIs ---
total_spend = filtered_df["Cost"].sum()
total_revenue = filtered_df["Revenue"].sum()
roi = ((total_revenue - total_spend) / total_spend) * 100 if total_spend > 0 else 0
avg_ctr = filtered_df["CTR"].mean() * 100
avg_conv_rate = filtered_df["Conversion_Rate"].mean() * 100

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Spend", f"${total_spend:,.2f}")
col2.metric("Total Revenue", f"${total_revenue:,.2f}")
col3.metric("Overall ROI", f"{roi:.2f}%")
col4.metric("Avg CTR", f"{avg_ctr:.2f}%")
col5.metric("Avg Conv. Rate", f"{avg_conv_rate:.2f}%")

st.markdown("---")

# --- VISUALIZATIONS ---
col_charts1, col_charts2 = st.columns(2)

with col_charts1:
    # ROI by Channel
    channel_perf = filtered_df.groupby("Channel")[["Cost", "Revenue"]].sum().reset_index()
    # Avoid div by zero
    channel_perf["Cost"] = channel_perf["Cost"].replace(0, 0.01)
    channel_perf["ROI"] = ((channel_perf["Revenue"] - channel_perf["Cost"]) / channel_perf["Cost"]) * 100
    fig_roi = px.bar(
        channel_perf,
        x="Channel",
        y="ROI",
        title="ROI by Channel (%)",
        color="Channel",
        text=channel_perf['ROI'].apply(lambda x: f'{x:.1f}%')
    )
    fig_roi.update_traces(textposition='outside')
    st.plotly_chart(fig_roi, use_container_width=True)

with col_charts2:
    # Top Campaigns
    top_campaigns = filtered_df.groupby("Campaign_Name")[["Cost", "Revenue"]].sum().reset_index()
    top_campaigns["Cost"] = top_campaigns["Cost"].replace(0, 0.01)
    top_campaigns["ROI"] = ((top_campaigns["Revenue"] - top_campaigns["Cost"]) / top_campaigns["Cost"]) * 100
    top_campaigns = top_campaigns.sort_values(by="Revenue", ascending=False).head(10)
    fig_camp = px.bar(
        top_campaigns,
        x="Revenue",
        y="Campaign_Name",
        orientation='h',
        title="Top 10 Campaigns by Revenue",
        color="ROI",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_camp, use_container_width=True)

col_charts3, col_charts4 = st.columns(2)

with col_charts3:
    # Spend vs Revenue Time Series
    trend_df = filtered_df.groupby(filtered_df["Date"].dt.to_period("M"))[["Cost", "Revenue"]].sum().reset_index()
    trend_df["Date"] = trend_df["Date"].dt.to_timestamp()
    fig_trend = px.line(
        trend_df,
        x="Date",
        y=["Cost", "Revenue"],
        title="Monthly Spend vs Revenue Trends",
        labels={"value": "Amount ($)", "variable": "Metric"}
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col_charts4:
    # Channel CTR vs Conversion Rate Scatter
    scatter_df = filtered_df.groupby("Channel")[["CTR", "Conversion_Rate", "Cost"]].mean().reset_index()
    fig_scatter = px.scatter(
        scatter_df,
        x="CTR",
        y="Conversion_Rate",
        size="Cost",
        color="Channel",
        title="Avg CTR vs Conversion Rate (Bubble Size = Avg Spend)",
        labels={"CTR": "Click-Through Rate", "Conversion_Rate": "Conversion Rate"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Datatable
st.markdown("### Campaign Level Datatable")
st.dataframe(filtered_df.head(100), use_container_width=True)
