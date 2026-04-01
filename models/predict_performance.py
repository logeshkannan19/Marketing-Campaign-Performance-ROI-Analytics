import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os

def train_model():
    print("Loading preprocessed data...")
    if os.path.basename(os.getcwd()) == 'models':
        base_dir = '..'
    else:
        base_dir = '.'
        
    data_path = os.path.join(base_dir, 'data', 'processed', 'cleaned_marketing_data.csv')
    df = pd.read_csv(data_path)
    
    # We want to predict Revenue based on Spend, CT, Impressions, Channel, Region
    # Encode categorical variables
    df_encoded = pd.get_dummies(df, columns=['Channel', 'Region', 'Target_Audience'], drop_first=True)
    
    # Features & Target
    # Predicting Revenue
    features = ['Impressions', 'Clicks', 'Cost', 'CTR', 'CPC'] + [col for col in df_encoded.columns if col.startswith(('Channel_', 'Region_', 'Target_Audience_'))]
    X = df_encoded[features]
    y = df_encoded['Revenue']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Regressor...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Evaluation:\n MSE: {mse:.2f}\n R-squared: {r2:.3f}")
    
    # Feature importance
    importances = model.feature_importances_
    feat_impl_df = pd.DataFrame({'Feature': features, 'Importance': importances}).sort_values(by='Importance', ascending=False)
    
    print("\nTop 5 Important Features for Revenue:")
    print(feat_impl_df.head())
    
    print("\nInsights for Budget Optimization:")
    print("Consider allocating more budget to channels and regions with higher feature importance for predicting revenue.")
    
    # Save feature importance to reports
    os.makedirs(os.path.join(base_dir, 'reports'), exist_ok=True)
    feat_impl_df.to_csv(os.path.join(base_dir, 'reports', 'feature_importances.csv'), index=False)
    print("\nFeature importances saved to reports/feature_importances.csv")

if __name__ == "__main__":
    train_model()
