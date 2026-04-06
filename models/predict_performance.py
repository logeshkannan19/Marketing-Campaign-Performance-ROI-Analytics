"""
Marketing Campaign Performance Prediction Module

Machine learning pipeline for predicting campaign revenue using Random Forest.
Provides model training, evaluation, and feature importance analysis.
"""

import json
import os
from typing import Dict, Tuple

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


MODEL_CONFIG = {
    "test_size": 0.2,
    "random_state": 42,
    "n_estimators": 100,
    "max_depth": 10,
}


def load_cleaned_data(filepath: str = "data/cleaned_data.csv") -> pd.DataFrame:
    """Load preprocessed campaign data."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Cleaned data not found at {filepath}. Run preprocessing first."
        )
    return pd.read_csv(filepath)


def prepare_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """Prepare features for ML model training."""
    numeric_features = [
        "impressions",
        "clicks",
        "cost",
        "ctr",
        "conversion_rate",
        "cpc",
    ]
    categorical_features = ["channel", "region", "target_audience"]

    X = df[numeric_features].copy()

    for col in categorical_features:
        dummies = pd.get_dummies(df[col], prefix=col, drop_first=True)
        X = pd.concat([X, dummies], axis=1)

    y = df["revenue"]
    return X, y


def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = None,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into training and test sets."""
    if test_size is None:
        test_size = MODEL_CONFIG["test_size"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=MODEL_CONFIG["random_state"]
    )

    print(f"Training set: {len(X_train):,} records")
    print(f"Test set: {len(X_test):,} records")

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestRegressor:
    """Train Random Forest regression model."""
    model = RandomForestRegressor(
        n_estimators=MODEL_CONFIG["n_estimators"],
        max_depth=MODEL_CONFIG["max_depth"],
        random_state=MODEL_CONFIG["random_state"],
        n_jobs=-1,
    )

    print("\nTraining Random Forest model...")
    model.fit(X_train, y_train)
    print("Training complete")

    return model


def evaluate_model(
    model: RandomForestRegressor,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Tuple[Dict[str, float], np.ndarray]:
    """Evaluate model performance on test data."""
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    metrics = {
        "mse": float(mse),
        "rmse": float(rmse),
        "mae": float(mae),
        "r2": float(r2),
    }

    print("\n" + "=" * 50)
    print("Model Evaluation Metrics")
    print("=" * 50)
    print(f"R² Score:              {r2:.4f}")
    print(f"Root Mean Squared Err: ${rmse:,.2f}")
    print(f"Mean Absolute Error:   ${mae:,.2f}")
    print("=" * 50 + "\n")

    return metrics, y_pred


def get_feature_importance(
    model: RandomForestRegressor,
    feature_names: list,
) -> pd.DataFrame:
    """Extract and display feature importance rankings."""
    importances = model.feature_importances_

    feat_imp = pd.DataFrame({
        "feature": feature_names,
        "importance": importances,
    }).sort_values("importance", ascending=False)

    print("\nTop 10 Most Important Features:")
    for _, row in feat_imp.head(10).iterrows():
        print(f"  {row['feature']:30s} {row['importance']:.4f}")

    return feat_imp


def save_outputs(
    metrics: Dict[str, float],
    feature_importance: pd.DataFrame,
    output_dir: str = "outputs/reports",
) -> None:
    """Save model metrics and feature importance to files."""
    os.makedirs(output_dir, exist_ok=True)

    metrics_path = os.path.join(output_dir, "model_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)

    importance_path = os.path.join(output_dir, "feature_importance.csv")
    feature_importance.to_csv(importance_path, index=False)

    print(f"Saved metrics to: {metrics_path}")
    print(f"Saved feature importance to: {importance_path}")


def run_pipeline() -> None:
    """Execute the complete ML pipeline."""
    print("\n" + "=" * 60)
    print("Revenue Prediction Pipeline")
    print("=" * 60 + "\n")

    print("Loading cleaned data...")
    df = load_cleaned_data()

    print("\nPreparing features...")
    X, y = prepare_features(df)

    print("\nSplitting data...")
    X_train, X_test, y_train, y_test = split_data(X, y)

    model = train_model(X_train, y_train)
    metrics, predictions = evaluate_model(model, X_test, y_test)
    feature_importance = get_feature_importance(model, X.columns.tolist())

    print("\nSaving outputs...")
    save_outputs(metrics, feature_importance)

    print("\n✓ Pipeline complete!")


if __name__ == "__main__":
    run_pipeline()
