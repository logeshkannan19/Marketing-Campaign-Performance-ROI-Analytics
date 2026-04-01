# System Architecture: Marketing Campaign Performance & ROI Analytics

## High-Level Architecture
This project implements a modular, end-to-end data pipeline moving from raw data generation to interactive visualization and predictive machine learning. The architecture is designed for clarity, reproducibility, and potential scaling into cloud environments.

## Component Breakdown

### 1. Data Ingestion & Storage (`data/`)
- **Raw Data (`data/raw/`)**: Currently mocking 10,000 records of synthetic data using `src/data_generator.py`. In a production environment, this layer would ingest CSV exports from ad platforms (Google Ads, Meta Ads) or connect to API streams.
- **Processed Data (`data/processed/`)**: The source of truth for downstream tools. All SQL aggregations, EDA, ML models, and the Dashboard read strictly from the processed output to ensure data consistency.

### 2. Data Engineering (`src/`)
- **`data_preprocessing.py`**: The ETL engine of the application.
  - **Responsibilities**: Data cleaning (handling `NaN` values via category medians), deduplication, datatype normalization, and business logic engineering (calculating CTR, CPI, ROI).
  - **Design Pattern**: Functional pipelines focused on idempotent outputs. Running this script sequentially on the raw data always yields the exact same clean dataset.

### 3. Analytics Layer
- **SQL (`sql/analysis_queries.sql`)**: Structured aggregation queries designed to mirror a Data Warehouse environment (e.g. Snowflake, BigQuery). These queries provide the macro-level KPI reporting logic.
- **Exploratory Data Analysis (`notebooks/`)**: Interactive Jupyter notebooks utilizing Matplotlib and Seaborn to visually profile data distributions, anomalies, and correlations prior to machine learning.

### 4. Machine Learning (`models/`)
- **`predict_performance.py`**: A supervised regression pipeline using `RandomForestRegressor` from `scikit-learn`.
  - **Inputs**: Encoded categorical dimensions (Region, Channel) and numerical metrics (Spend, Impressions, CTR).
  - **Outputs**: Revenue predictions, R^2 evaluation metrics, and feature importance mappings saved to `reports/` for budget optimization.

### 5. Presentation Layer (`dashboard/`)
- **`app.py`**: A low-latency Streamlit application serving as the UI.
  - Generates real-time, cross-filtered metrics utilizing `@st.cache_data` for memory efficiency.
  - Employs Plotly Express for rendering responsive, interactive charts (ROI, trends, distributions).

## Scalability & Future State
While currently running robustly on local environments, the architecture effortlessly supports migration:
- **Cloud Storage**: Transition local `data/` directories to AWS S3 or GCP Cloud Storage.
- **Orchestration**: Incorporate Apache Airflow or Prefect to schedule the daily extraction and preprocessing scripts.
- **Database Backend**: Migrate from static CSV reading to a robust PostgreSQL or Snowflake backend using SQLAlchemy.
