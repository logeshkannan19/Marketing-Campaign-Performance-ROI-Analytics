import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta


CONFIG = {
    'num_records': 8000,
    'random_seed': 42,
    'missing_revenue_pct': 0.05,
    'missing_audience_pct': 0.02,
    'duplicate_pct': 0.01,
}


def get_marketing_channels():
    return ['Google Ads', 'Facebook', 'Email', 'Instagram', 'LinkedIn']


def get_regions():
    return ['North America', 'Europe', 'Asia Pacific', 'Latin America']


def get_target_audiences():
    return [
        'Young Adults (18-24)',
        'Professionals (25-34)',
        'Adults (35-44)',
        'Seniors (45+)'
    ]


def get_campaign_names():
    prefixes = ['Spring', 'Summer', 'Fall', 'Winter', 'Q1', 'Q2', 'Q3', 'Q4', 'Holiday', 'Back to School']
    suffixes = ['Awareness', 'Retargeting', 'Conversion', 'Promo', 'Launch', 'Sale', 'Retention']
    return [f'{np.random.choice(prefixes)} {np.random.choice(suffixes)}' for _ in range(20)]


def generate_dates(start_date, num_records):
    num_days = 365
    weights = np.exp(np.linspace(0, 1, num_days))
    weights = weights / weights.sum()
    date_choices = [start_date + timedelta(days=i) for i in range(num_days)]
    return np.random.choice(date_choices, size=num_records, p=weights)


def generate_impressions(num_records):
    return np.random.lognormal(mean=9, sigma=1.2, size=num_records).astype(int)


def calculate_clicks_from_impressions(impressions):
    ctr_base = np.random.uniform(0.01, 0.08, len(impressions))
    ctr_with_noise = ctr_base * np.random.uniform(0.8, 1.2, len(impressions))
    ctr_with_noise = np.clip(ctr_with_noise, 0.005, 0.15)
    clicks = (impressions * ctr_with_noise).astype(int)
    clicks = np.maximum(clicks, 1)
    return clicks


def calculate_conversions_from_clicks(clicks):
    conv_rate = np.random.uniform(0.015, 0.12, len(clicks))
    conversions = (clicks * conv_rate).astype(int)
    return conversions


def generate_cost_per_click():
    return np.random.uniform(0.45, 4.50, CONFIG['num_records'])


def introduce_missing_values(df):
    num_revenue_missing = int(len(df) * CONFIG['missing_revenue_pct'])
    revenue_indices = np.random.choice(df.index, num_revenue_missing, replace=False)
    df.loc[revenue_indices, 'revenue'] = np.nan
    
    num_audience_missing = int(len(df) * CONFIG['missing_audience_pct'])
    audience_indices = np.random.choice(df.index, num_audience_missing, replace=False)
    df.loc[audience_indices, 'target_audience'] = np.nan
    
    return df


def introduce_duplicates(df):
    num_duplicates = int(len(df) * CONFIG['duplicate_pct'])
    if num_duplicates > 0:
        duplicate_indices = np.random.choice(df.index, num_duplicates, replace=True)
        duplicates = df.loc[duplicate_indices].copy()
        df = pd.concat([df, duplicates], ignore_index=True)
    return df


def create_dataframe(impressions, clicks, conversions, cpc, dates):
    campaign_names = get_campaign_names()
    
    df = pd.DataFrame({
        'campaign_id': [f'CMP_{i:06d}' for i in range(1, len(impressions) + 1)],
        'campaign_name': np.random.choice(campaign_names, len(impressions)),
        'channel': np.random.choice(get_marketing_channels(), len(impressions)),
        'date': dates,
        'impressions': impressions,
        'clicks': clicks,
        'conversions': conversions,
        'cost': np.round(clicks * cpc, 2),
        'revenue': np.round(conversions * np.random.uniform(25.0, 180.0, len(conversions)), 2),
        'target_audience': np.random.choice(get_target_audiences(), len(impressions)),
        'region': np.random.choice(get_regions(), len(impressions))
    })
    return df


def generate_dataset(num_records=None):
    if num_records is None:
        num_records = CONFIG['num_records']
    
    np.random.seed(CONFIG['random_seed'])
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = generate_dates(start_date, num_records)
    
    impressions = generate_impressions(num_records)
    clicks = calculate_clicks_from_impressions(impressions)
    conversions = calculate_conversions_from_clicks(clicks)
    cpc = generate_cost_per_click()
    
    df = create_dataframe(impressions, clicks, conversions, cpc, dates)
    df = introduce_missing_values(df)
    df = introduce_duplicates(df)
    df = df.sample(frac=1, random_state=CONFIG['random_seed']).reset_index(drop=True)
    
    return df


def save_to_csv(df, output_dir='data'):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'raw_data.csv')
    df.to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    print("Generating marketing campaign data...")
    df = generate_dataset()
    output_path = save_to_csv(df)
    print(f"Generated {len(df)} records -> {output_path}")