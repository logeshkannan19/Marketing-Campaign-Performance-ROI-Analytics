import streamlit as st
import pandas as pd
import plotly.express as px
import os


st.set_page_config(page_title="Marketing Campaign Dashboard", page_icon="📊", layout="wide")


@st.cache_data
def load_data():
    possible_paths = [
        'data/cleaned_data.csv',
        '../data/cleaned_data.csv',
        os.path.join(os.path.dirname(__file__), '..', 'data', 'cleaned_data.csv')
    ]
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['date'] = pd.to_datetime(df['date'])
            return df
    st.error("Data not found. Run the pipeline first:")
    st.code("python main.py all", language="bash")
    return pd.DataFrame()


def get_filtered_data(df, channel_filter, region_filter, date_range):
    mask = pd.Series([True] * len(df))
    if channel_filter:
        mask &= df['channel'].isin(channel_filter)
    if region_filter:
        mask &= df['region'].isin(region_filter)
    if date_range:
        start_date, end_date = date_range
        mask &= (df['date'] >= pd.to_datetime(start_date))
        mask &= (df['date'] <= pd.to_datetime(end_date))
    return df[mask]


def calculate_kpis(df):
    total_spend = df['cost'].sum()
    total_revenue = df['revenue'].sum()
    total_impressions = df['impressions'].sum()
    total_clicks = df['clicks'].sum()
    total_conversions = df['conversions'].sum()
    
    overall_ctr = total_clicks / total_impressions if total_impressions > 0 else 0
    overall_conv_rate = total_conversions / total_clicks if total_clicks > 0 else 0
    overall_roi = (total_revenue - total_spend) / total_spend if total_spend > 0 else 0
    
    return {
        'total_spend': total_spend,
        'total_revenue': total_revenue,
        'overall_ctr': overall_ctr,
        'overall_conv_rate': overall_conv_rate,
        'overall_roi': overall_roi
    }


def plot_roi_by_channel(df):
    channel_summary = df.groupby('channel').agg({'cost': 'sum', 'revenue': 'sum'}).reset_index()
    channel_summary['roi'] = (channel_summary['revenue'] - channel_summary['cost']) / channel_summary['cost']
    fig = px.bar(channel_summary, x='channel', y='roi', title='ROI by Channel', color='roi', color_continuous_scale='RdYlGn', text_auto='.1%')
    fig.update_layout(yaxis_tickformat='.0%', plot_bgcolor='white')
    return fig


def plot_top_campaigns(df, n=10):
    campaign_summary = df.groupby('campaign_name').agg({'cost': 'sum', 'revenue': 'sum'}).reset_index()
    campaign_summary['roi'] = (campaign_summary['revenue'] - campaign_summary['cost']) / campaign_summary['cost']
    top_campaigns = campaign_summary.nlargest(n, 'revenue')
    fig = px.bar(top_campaigns, y='campaign_name', x='revenue', orientation='h', title=f'Top {n} Campaigns by Revenue', color='roi', color_continuous_scale='Viridis')
    fig.update_layout(plot_bgcolor='white', yaxis={'categoryorder': 'total ascending'})
    return fig


def plot_monthly_trends(df):
    df_copy = df.copy()
    df_copy['month'] = df_copy['date'].dt.to_period('M')
    monthly = df_copy.groupby('month').agg({'cost': 'sum', 'revenue': 'sum'}).reset_index()
    monthly['month'] = monthly['month'].dt.to_timestamp()
    fig = px.line(monthly, x='month', y=['cost', 'revenue'], title='Monthly Spend vs Revenue', labels={'month': 'Month', 'value': 'Amount ($)', 'variable': 'Metric'}, color_discrete_map={'cost': '#ff6b6b', 'revenue': '#4ecdc4'})
    fig.update_layout(plot_bgcolor='white', legend_title_text='')
    return fig


def plot_channel_scatter(df):
    channel_summary = df.groupby('channel').agg({'ctr': 'mean', 'conversion_rate': 'mean', 'cost': 'sum', 'revenue': 'sum'}).reset_index()
    fig = px.scatter(channel_summary, x='ctr', y='conversion_rate', size='cost', color='channel', title='Channel Performance: CTR vs Conversion Rate', labels={'ctr': 'Click-Through Rate', 'conversion_rate': 'Conversion Rate', 'cost': 'Total Spend'}, hover_data=['revenue'])
    fig.update_layout(plot_bgcolor='white', xaxis_tickformat='.1%', yaxis_tickformat='.1%')
    return fig


def main():
    df = load_data()
    if df.empty:
        st.stop()
    
    st.sidebar.header("Filters")
    available_channels = sorted(df['channel'].unique().tolist())
    channel_filter = st.sidebar.multiselect("Channel", options=available_channels, default=available_channels)
    available_regions = sorted(df['region'].unique().tolist())
    region_filter = st.sidebar.multiselect("Region", options=available_regions, default=available_regions)
    
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    date_range = st.sidebar.date_input("Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    
    filtered_df = get_filtered_data(df, channel_filter, region_filter, date_range)
    
    st.title("📊 Marketing Campaign Performance Dashboard")
    st.markdown("Track ROI, analyze channel performance, and identify optimization opportunities.")
    
    st.sidebar.markdown("---")
    st.sidebar.caption(f"Data: {len(filtered_df):,} of {len(df):,} records")
    
    kpis = calculate_kpis(filtered_df)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Spend", f"${kpis['total_spend']:,.0f}")
    col2.metric("Total Revenue", f"${kpis['total_revenue']:,.0f}")
    col3.metric("Overall ROI", f"{kpis['overall_roi']:.1%}")
    col4.metric("Avg CTR", f"{kpis['overall_ctr']:.2%}")
    col5.metric("Avg Conv Rate", f"{kpis['overall_conv_rate']:.2%}")
    
    st.markdown("---")
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.plotly_chart(plot_roi_by_channel(filtered_df), use_container_width=True)
    with col_chart2:
        st.plotly_chart(plot_top_campaigns(filtered_df), use_container_width=True)
    
    col_chart3, col_chart4 = st.columns(2)
    with col_chart3:
        st.plotly_chart(plot_monthly_trends(filtered_df), use_container_width=True)
    with col_chart4:
        st.plotly_chart(plot_channel_scatter(filtered_df), use_container_width=True)
    
    st.markdown("---")
    st.subheader("📋 Campaign Data")
    display_cols = ['campaign_name', 'channel', 'region', 'date', 'impressions', 'clicks', 'conversions', 'cost', 'revenue', 'roi']
    table_df = filtered_df[display_cols].copy()
    table_df['roi'] = table_df['roi'].apply(lambda x: f"{x:.1%}")
    table_df['date'] = table_df['date'].dt.strftime('%Y-%m-%d')
    st.dataframe(table_df.head(100), use_container_width=True, height=400)
    
    st.markdown("---")
    st.caption(f"Data period: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")


if __name__ == "__main__":
    main()