"""
Data Preprocessing Module

ETL pipeline for cleaning and transforming raw marketing campaign data.
Handles missing values, duplicates, and calculates derived KPIs.
"""

import os
from typing import Optional

import numpy as np
import pandas as pd


def load_raw_data(filepath: str) -> pd.DataFrame:
    """Load raw campaign data from CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Raw data file not found: {filepath}")

    df = pd.read_csv(filepath)

    if df.empty:
        raise ValueError("Raw data file is empty")

    print(f"Loaded {len(df):,} records from {filepath}")
    return df


def handle_missing_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Impute missing revenue values using channel medians."""
    channel_medians = df.groupby("channel")["revenue"].median()

    df["revenue"] = df.apply(
        lambda row: channel_medians.get(row["channel"], df["revenue"].median())
        if pd.isna(row["revenue"])
        else row["revenue"],
        axis=1
    )

    missing_count = df["revenue"].isna().sum()
    if missing_count > 0:
        df["revenue"] = df["revenue"].fillna(df["revenue"].median())

    return df


def handle_missing_audience(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing target audience values."""
    df["target_audience"] = df["target_audience"].fillna("Unknown")
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate campaign records."""
    initial_count = len(df)
    df = df.drop_duplicates(subset=["campaign_id"], keep="first")
    duplicates_removed = initial_count - len(df)

    if duplicates_removed > 0:
        print(f"Removed {duplicates_removed:,} duplicate records")

    return df


def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Parse and validate date columns."""
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    null_dates = df["date"].isna().sum()

    if null_dates > 0:
        print(f"Warning: {null_dates:,} records have invalid dates, removing them")
        df = df.dropna(subset=["date"])

    return df


def calculate_ctr(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate Click-Through Rate (CTR)."""
    df["ctr"] = np.where(
        df["impressions"] > 0,
        df["clicks"] / df["impressions"],
        0
    )
    df["ctr"] = df["ctr"].clip(upper=1.0)
    return df


def calculate_conversion_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate Conversion Rate."""
    df["conversion_rate"] = np.where(
        df["clicks"] > 0,
        df["conversions"] / df["clicks"],
        0
    )
    df["conversion_rate"] = df["conversion_rate"].clip(upper=1.0)
    return df


def calculate_cpc(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate Cost Per Click (CPC)."""
    df["cpc"] = np.where(
        df["clicks"] > 0,
        df["cost"] / df["clicks"],
        0
    )
    return df


def calculate_roi(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate Return on Investment (ROI)."""
    df["roi"] = np.where(
        df["cost"] > 0,
        (df["revenue"] - df["cost"]) / df["cost"],
        0
    )
    return df


def calculate_cac(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate Customer Acquisition Cost (CAC)."""
    df["cac"] = np.where(
        df["conversions"] > 0,
        df["cost"] / df["conversions"],
        0
    )
    return df


def add_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add all derived KPI features."""
    df = calculate_ctr(df)
    df = calculate_conversion_rate(df)
    df = calculate_cpc(df)
    df = calculate_roi(df)
    df = calculate_cac(df)
    return df


def validate_data_quality(df: pd.DataFrame) -> dict:
    """Validate data quality and identify potential issues."""
    issues = {}

    if (df[["impressions", "clicks", "conversions", "cost", "revenue"]] < 0).any().any():
        issues["negative_values"] = "Found negative values in numeric fields"

    high_ctr = (df["ctr"] > 0.5).sum()
    if high_ctr > 0:
        issues["high_ctr"] = f"{high_ctr:,} records have CTR > 50%"

    high_cpc = (df["cpc"] > 50).sum()
    if high_cpc > 0:
        issues["high_cpc"] = f"{high_cpc:,} records have CPC > $50"

    return issues


def preprocess_data(
    input_path: str = "data/raw_data.csv",
    output_path: str = "data/cleaned_data.csv",
) -> pd.DataFrame:
    """Execute complete preprocessing pipeline."""
    print("\n" + "=" * 60)
    print("Data Preprocessing Pipeline")
    print("=" * 60 + "\n")

    print("Step 1: Loading raw data...")
    df = load_raw_data(input_path)
    print(f"  Initial records: {len(df):,}")

    print("\nStep 2: Handling missing values...")
    df = handle_missing_revenue(df)
    df = handle_missing_audience(df)

    print("\nStep 3: Removing duplicates...")
    df = remove_duplicates(df)

    print("\nStep 4: Parsing dates...")
    df = parse_dates(df)

    print("\nStep 5: Calculating derived metrics...")
    df = add_derived_features(df)

    print("\nStep 6: Validating data quality...")
    issues = validate_data_quality(df)

    if issues:
        for issue_type, message in issues.items():
            print(f"  Warning: {message}")
    else:
        print("  No major data quality issues found")

    print("\n" + "=" * 60)
    print(f"Final record count: {len(df):,}")
    print("=" * 60 + "\n")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to: {output_path}")

    return df


if __name__ == "__main__":
    import sys

    input_file = sys.argv[1] if len(sys.argv) > 1 else "data/raw_data.csv"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "data/cleaned_data.csv"

    preprocess_data(input_file, output_file)
