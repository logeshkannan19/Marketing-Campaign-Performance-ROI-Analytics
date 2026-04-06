# System Architecture: Marketing Campaign Performance & ROI Analytics

## Overview

This project implements a modular, end-to-end data pipeline moving from raw data generation to interactive visualization and predictive machine learning. The architecture is designed for clarity, reproducibility, and scalability into cloud environments.

---

## High-Level Architecture

```
┌──────────────────┐    ┌───────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│     Data Gen     │───▶│  Preprocessing    │───▶│   ML Pipeline    │───▶│    Dashboard     │
│  (8,000+ recs)   │    │  (KPIs + Clean)   │    │ (Random Forest)  │    │   (Streamlit)    │
└──────────────────┘    └───────────────────┘    └──────────────────┘    └──────────────────┘
```

---

## Component Breakdown

### 1. Data Ingestion & Storage (`data/`)

| Directory | Purpose |
|-----------|---------|
| `raw_data.csv` | Synthetic marketing campaign data (8,000+ records) |
| `cleaned_data.csv` | Preprocessed data with derived KPIs |

In production, this layer would ingest data from ad platforms (Google Ads, Meta Ads) via API or CSV exports.

---

### 2. Data Engineering (`src/`)

#### `data_generator.py`
- Generates realistic synthetic marketing data
- Simulates impressions, clicks, conversions, cost, and revenue
- Introduces realistic data quality issues (missing values, duplicates)

#### `data_preprocessing.py`
- **ETL Engine** of the application
- **Responsibilities**:
  - Data cleaning (handling missing values via channel medians)
  - Deduplication by campaign ID
  - Datatype normalization
  - Business logic engineering (CTR, CPC, ROI, CAC calculations)
- **Design Pattern**: Idempotent functional pipelines

---

### 3. Analytics Layer

#### SQL (`sql/analysis_queries.sql`)
- Structured aggregation queries mirroring a Data Warehouse environment (Snowflake, BigQuery)
- Provides macro-level KPI reporting logic

#### Exploratory Data Analysis (`notebooks/`)
- Interactive Jupyter notebooks using Matplotlib and Seaborn
- Data distribution profiling, anomaly detection, correlation analysis

---

### 4. Machine Learning (`models/predict_performance.py`)

A supervised regression pipeline using `RandomForestRegressor`:

- **Inputs**: Encoded categorical dimensions (Region, Channel) + numerical metrics (Spend, Impressions, CTR)
- **Outputs**: 
  - Revenue predictions
  - R² evaluation metrics
  - Feature importance rankings

---

### 5. Presentation Layer (`dashboard/app.py`)

- **Streamlit** application serving as the UI
- **Features**:
  - Real-time cross-filtered metrics
  - `@st.cache_data` for memory efficiency
  - Plotly Express for interactive charts
  - Multi-dimensional filtering (channel, region, date range)

---

## Data Flow

```
1. Generation → 2. Preprocessing → 3. ML Training → 4. Dashboard
     │               │                    │               │
  8,000+         Derived KPIs         R² = 0.70      Interactive
  Records        CTR, CPC,           Revenue         Visualizations
                 ROI, CAC            Prediction
```

---

## Scalability & Future State

The architecture supports migration to production environments:

| Component | Current State | Future State |
|-----------|--------------|--------------|
| **Storage** | Local CSV files | AWS S3 / GCP Cloud Storage |
| **Orchestration** | Manual CLI | Apache Airflow / Prefect |
| **Database** | Static CSV | PostgreSQL / Snowflake |
| **ML Training** | Local training | MLOps pipeline (MLflow, Kubeflow) |

---

## Technology Decisions

| Decision | Rationale |
|----------|-----------|
| **Random Forest** | Robust to overfitting, handles mixed data types, provides feature importance |
| **Streamlit** | Rapid UI development, Python-native, excellent Plotly integration |
| **Pandas/NumPy** | Industry-standard data processing, memory efficient |
| **Plotly** | Interactive visualizations, web-ready rendering |
