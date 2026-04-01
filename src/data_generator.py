import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_marketing_data(num_records=5000):
    np.random.seed(42)
    
    channels = ['Google Ads', 'Facebook', 'Email', 'Instagram', 'LinkedIn']
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
    target_audiences = ['Young Adults (18-24)', 'Professionals (25-34)', 'Adults (35-44)', 'Seniors (45+)']
    
    # Generate dates over the past year
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)
    dates = [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(num_records)]
    
    # Generate base metrics
    impressions = np.random.randint(1000, 100000, num_records)
    
    # Clicks are a fraction of impressions (CTR between 1% and 10%)
    ctr_rates = np.random.uniform(0.01, 0.10, num_records)
    clicks = (impressions * ctr_rates).astype(int)
    
    # Conversions are a fraction of clicks (Conv rate between 2% and 15%)
    conv_rates = np.random.uniform(0.02, 0.15, num_records)
    conversions = (clicks * conv_rates).astype(int)
    
    # Cost per click between $0.5 and $5.0
    cpc = np.random.uniform(0.5, 5.0, num_records)
    cost = np.round(clicks * cpc, 2)
    
    # Revenue per conversion between $20 and $200
    rev_per_conv = np.random.uniform(20.0, 200.0, num_records)
    revenue = np.round(conversions * rev_per_conv, 2)
    
    # Assemble dataframe
    df = pd.DataFrame({
        'Campaign_ID': [f'CMP_{i:05d}' for i in range(1, num_records + 1)],
        'Campaign_Name': [f'Campaign_{np.random.choice(["Alpha", "Beta", "Gamma", "Delta", "Echo"])}' for _ in range(num_records)],
        'Channel': np.random.choice(channels, num_records),
        'Date': dates,
        'Impressions': impressions,
        'Clicks': clicks,
        'Conversions': conversions,
        'Cost': cost,
        'Revenue': revenue,
        'Target_Audience': np.random.choice(target_audiences, num_records),
        'Region': np.random.choice(regions, num_records)
    })
    
    # Introduce some missing values (about 5%)
    mask = np.random.rand(num_records) < 0.05
    df.loc[mask, 'Revenue'] = np.nan
    mask2 = np.random.rand(num_records) < 0.02
    df.loc[mask2, 'Target_Audience'] = np.nan
    
    # Introduce some duplicates (about 1%)
    num_dupes = int(num_records * 0.01)
    if num_dupes > 0:
        dupes = df.sample(num_dupes, replace=True)
        df = pd.concat([df, dupes], ignore_index=True)
        
    return df

if __name__ == "__main__":
    df = generate_marketing_data(10000)
    
    # Make directory
    # Assume script is run from project root or src folder
    if os.path.basename(os.getcwd()) == 'src':
        base_dir = '..'
    else:
        base_dir = '.'
        
    os.makedirs(os.path.join(base_dir, 'data', 'raw'), exist_ok=True)
    
    output_path = os.path.join(base_dir, 'data', 'raw', 'marketing_campaign_data.csv')
    df.to_csv(output_path, index=False)
    print(f"Data generated successfully! Saved to {output_path}")
    print(f"Dataset shape: {df.shape}")
