import pandas as pd
import numpy as np
import os

def preprocess_data(input_path, output_path):
    print(f"Loading data from {input_path}...")
    df = pd.read_csv(input_path)
    
    print(f"Initial shape: {df.shape}")
    
    # 1. Handle missing values
    # Fill missing revenue with median revenue of that channel
    df['Revenue'] = df.groupby('Channel')['Revenue'].transform(lambda x: x.fillna(x.median()))
    df['Target_Audience'] = df['Target_Audience'].fillna('Unknown')
    
    # 2. Handle duplicates
    # Sort by Date so that we keep the latest if there's any logic, or just first
    df = df.drop_duplicates(subset=['Campaign_ID'], keep='first')
    
    # 3. Convert date column (from string/datetime to just date)
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    
    # 4. Create calculated metrics
    # CTR = Clicks / Impressions
    df['CTR'] = (df['Clicks'] / df['Impressions']).fillna(0)
    
    # Conversion Rate = Conversions / Clicks
    df['Conversion_Rate'] = (df['Conversions'] / df['Clicks']).fillna(0)
    df.replace([np.inf, -np.inf], 0, inplace=True)
    
    # CPC = Cost / Clicks
    df['CPC'] = (df['Cost'] / df['Clicks']).fillna(0)
    
    # ROI = (Revenue - Cost) / Cost
    df['ROI'] = ((df['Revenue'] - df['Cost']) / df['Cost']).fillna(0)
    df.replace([np.inf, -np.inf], 0, inplace=True)
    
    print(f"Processed shape: {df.shape}")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")
    
    return df

if __name__ == "__main__":
    if os.path.basename(os.getcwd()) == 'src':
        base_dir = '..'
    else:
        base_dir = '.'
        
    input_file = os.path.join(base_dir, 'data', 'raw', 'marketing_campaign_data.csv')
    output_file = os.path.join(base_dir, 'data', 'processed', 'cleaned_marketing_data.csv')
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Could not find raw data file at {input_file}. Please run data_generator.py first.")
        
    preprocess_data(input_file, output_file)
