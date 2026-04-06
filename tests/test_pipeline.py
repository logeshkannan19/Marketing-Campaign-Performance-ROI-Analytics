import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_generator import (
    generate_dataset,
    get_marketing_channels,
    get_regions,
    get_target_audiences,
)
from src.data_preprocessing import preprocess_data


class TestDataGenerator:
    """Tests for data generator module."""

    def test_get_marketing_channels(self):
        """Test marketing channels list."""
        channels = get_marketing_channels()
        assert isinstance(channels, list)
        assert len(channels) > 0
        assert "Google Ads" in channels
        assert "Facebook" in channels

    def test_get_regions(self):
        """Test regions list."""
        regions = get_regions()
        assert isinstance(regions, list)
        assert len(regions) > 0

    def test_get_target_audiences(self):
        """Test target audiences list."""
        audiences = get_target_audiences()
        assert isinstance(audiences, list)
        assert len(audiences) > 0

    def test_generate_dataset_shape(self):
        """Test generated dataset has correct shape."""
        df = generate_dataset(num_records=100)
        assert len(df) == 100

    def test_generate_dataset_columns(self):
        """Test generated dataset has required columns."""
        df = generate_dataset(num_records=50)
        required_columns = [
            "campaign_id",
            "campaign_name",
            "channel",
            "date",
            "impressions",
            "clicks",
            "conversions",
            "cost",
            "revenue",
            "target_audience",
            "region",
        ]
        for col in required_columns:
            assert col in df.columns

    def test_generate_dataset_types(self):
        """Test generated dataset has correct data types."""
        df = generate_dataset(num_records=50)
        assert pd.api.types.is_datetime64_any_dtype(df["date"])
        assert pd.api.types.is_numeric_dtype(df["impressions"])
        assert pd.api.types.is_numeric_dtype(df["clicks"])

    def test_no_negative_values(self):
        """Test generated data has no negative values."""
        df = generate_dataset(num_records=100)
        numeric_cols = ["impressions", "clicks", "conversions", "cost", "revenue"]
        for col in numeric_cols:
            assert (df[col] >= 0).all(), f"Negative values found in {col}"


class TestDataPreprocessing:
    """Tests for data preprocessing module."""

    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing."""
        dates = [datetime.now() - timedelta(days=i) for i in range(10)]
        return pd.DataFrame({
            "campaign_id": [f"CMP_{i:06d}" for i in range(1, 11)],
            "campaign_name": ["Test Campaign"] * 10,
            "channel": ["Google Ads"] * 10,
            "date": dates,
            "impressions": np.random.randint(1000, 10000, 10),
            "clicks": np.random.randint(50, 500, 10),
            "conversions": np.random.randint(5, 50, 10),
            "cost": np.random.uniform(100, 1000, 10),
            "revenue": np.random.uniform(500, 5000, 10),
            "target_audience": ["Professionals (25-34)"] * 10,
            "region": ["North America"] * 10,
        })

    def test_preprocess_adds_ctr(self, sample_data, tmp_path):
        """Test preprocessing adds CTR column."""
        input_file = tmp_path / "input.csv"
        output_file = tmp_path / "output.csv"
        sample_data.to_csv(input_file, index=False)

        result = preprocess_data(
            input_path=str(input_file),
            output_path=str(output_file)
        )

        assert "ctr" in result.columns

    def test_preprocess_adds_roi(self, sample_data, tmp_path):
        """Test preprocessing adds ROI column."""
        input_file = tmp_path / "input.csv"
        output_file = tmp_path / "output.csv"
        sample_data.to_csv(input_file, index=False)

        result = preprocess_data(
            input_path=str(input_file),
            output_path=str(output_file)
        )

        assert "roi" in result.columns

    def test_preprocess_adds_cac(self, sample_data, tmp_path):
        """Test preprocessing adds CAC column."""
        input_file = tmp_path / "input.csv"
        output_file = tmp_path / "output.csv"
        sample_data.to_csv(input_file, index=False)

        result = preprocess_data(
            input_path=str(input_file),
            output_path=str(output_file)
        )

        assert "cac" in result.columns


class TestMLModel:
    """Tests for ML model module."""

    def test_model_imports(self):
        """Test model module can be imported."""
        from models import predict_performance
        assert hasattr(predict_performance, "run_pipeline")
