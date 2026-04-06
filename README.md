# Marketing Campaign Performance & ROI Analytics

> Enterprise-grade analytics platform for tracking, analyzing, and optimizing marketing campaign performance across digital channels.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Tech Stack](#tech-stack)
5. [Project Structure](#project-structure)
6. [Quick Start](#quick-start)
7. [Key Metrics](#key-metrics)
8. [Model Performance](#model-performance)
9. [Dashboard](#dashboard)
10. [Business Impact](#business-impact)
11. [Use Cases](#use-cases)
12. [Limitations](#limitations)
13. [Future Enhancements](#future-enhancements)
14. [Contributing](#contributing)
15. [License](#license)

---

## Overview

Marketing teams often struggle to answer critical business questions:
- Which advertising channels deliver the best ROI?
- Is budget being allocated efficiently across campaigns?
- What is the actual cost per customer acquisition?

This project provides a **data-driven framework** to evaluate campaign effectiveness and optimize marketing spend through an end-to-end analytics pipeline.

### Key Highlights

| Capability | Description |
|------------|-------------|
| **Data Pipeline** | End-to-end flow from raw data generation to actionable insights |
| **ML Model** | Random Forest regressor achieving **R² = 0.70** for revenue prediction |
| **Dashboard** | Streamlit-based UI with filters for channel, region, and date range |
| **Feature Analysis** | Identifies top revenue drivers (clicks: 68%, conversion rate: 14%) |
| **Dataset** | 8,000+ realistic synthetic marketing records |

---

## Features

### Data Pipeline
- **Synthetic Data Generation**: Creates realistic marketing campaign data
- **Data Preprocessing**: Handles missing values, removes duplicates, calculates derived KPIs
- **Feature Engineering**: CTR, CPC, Conversion Rate, ROI, CAC calculations

### Machine Learning
- **Revenue Prediction**: Random Forest regression model
- **Feature Importance**: Identifies key revenue drivers
- **Model Evaluation**: R², RMSE, MAE metrics

### Dashboard
- **KPI Overview**: Total spend, revenue, ROI, CTR, conversion rate
- **Interactive Visualizations**: ROI by channel, top campaigns, monthly trends
- **Multi-dimensional Filtering**: By channel, region, and date range
- **Data Table**: Campaign-level detail view

---

## Architecture

```
┌──────────────────┐    ┌───────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│     Data Gen     │───▶│  Preprocessing    │───▶│   ML Pipeline    │───▶│    Dashboard     │
│  (8,000+ recs)   │    │  (KPIs + Clean)   │    │ (Random Forest)  │    │   (Streamlit)    │
└──────────────────┘    └───────────────────┘    └──────────────────┘    └──────────────────┘
       Synthetic              Derived                  R² = 0.70              Interactive
         Data             CTR, CPC,                  Revenue                 Charts
                          ROI, CAC                 Prediction
```

### Pipeline Flow

| Step | Component | Description |
|------|-----------|-------------|
| 1 | Data Generation | Creates 8,000+ marketing records |
| 2 | Preprocessing | Cleans data, calculates CTR, CPC, ROI, CAC |
| 3 | ML Model | Trains Random Forest to predict revenue |
| 4 | Dashboard | Visualizes insights for non-technical users |

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.8+ |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn (Random Forest Regressor) |
| **Visualization** | Plotly, Matplotlib |
| **Dashboard** | Streamlit |
| **Development** | Jupyter Notebooks |

---

## Project Structure

```
marketing-campaign-roi-analytics/
├── data/
│   ├── raw_data.csv              # Generated raw campaign data
│   └── cleaned_data.csv          # Preprocessed data with derived metrics
├── src/
│   ├── __init__.py
│   ├── data_generator.py         # Synthetic data generation module
│   └── data_preprocessing.py     # Data cleaning and feature engineering
├── models/
│   ├── __init__.py
│   └── predict_performance.py    # ML model training and evaluation
├── dashboard/
│   ├── __init__.py
│   └── app.py                    # Streamlit dashboard application
├── outputs/
│   └── reports/                  # Generated model metrics and reports
├── notebooks/
│   └── eda_analysis.ipynb        # Exploratory data analysis
├── sql/
│   └── analysis_queries.sql      # SQL analysis queries
├── tests/                        # Unit tests (future)
├── scripts/                      # Utility scripts (future)
├── main.py                       # CLI entry point
├── setup.py                      # Package configuration
├── pyproject.toml               # Project metadata
├── requirements.txt              # Project dependencies
├── ARCHITECTURE.md               # System architecture documentation
├── CONTRIBUTING.md              # Contribution guidelines
├── ROADMAP.md                    # Project roadmap
├── LICENSE                       # MIT License
└── README.md                     # Project documentation
```

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/logeshkannan19/Marketing-Campaign-Performance-ROI-Analytics.git
cd Marketing-Campaign-Performance-ROI-Analytics

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

### Usage

```bash
# Run the full pipeline (generates data, cleans, trains model, launches dashboard)
python main.py all

# Run individual components
python main.py generate      # Generate synthetic data
python main.py preprocess     # Clean and preprocess data
python main.py model          # Train prediction model
python main.py dashboard      # Launch interactive dashboard
```

The dashboard will be available at `http://localhost:8501`.

---

## Key Metrics

| Metric | Formula | Business Significance |
|--------|---------|----------------------|
| **CTR** (Click-Through Rate) | Clicks ÷ Impressions | Measures ad visibility and appeal |
| **Conversion Rate** | Conversions ÷ Clicks | Indicates landing page effectiveness |
| **CPC** (Cost Per Click) | Cost ÷ Clicks | Measures efficiency of ad spend |
| **ROI** (Return on Investment) | (Revenue - Cost) ÷ Cost | Overall profitability of campaign |
| **CAC** (Customer Acquisition Cost) | Cost ÷ Conversions | Customer acquisition efficiency |

---

## Model Performance

### Evaluation Metrics

| Metric | Value |
|--------|-------|
| **R² Score** | 0.70 |
| **RMSE** | $5,489 |
| **MAE** | $2,002 |

### Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | Clicks | 68.2% |
| 2 | Conversion Rate | 14.4% |
| 3 | CTR | 4.7% |
| 4 | Impressions | 3.7% |
| 5 | Cost | 2.6% |

---

## Dashboard

### Visualizations

| Chart | Description |
|-------|-------------|
| **ROI by Channel** | Bar chart comparing ROI across Google Ads, Facebook, Email, Instagram, LinkedIn |
| **Top Campaigns** | Top 10 campaigns ranked by revenue |
| **Monthly Trends** | 12-month spend vs. revenue line chart |
| **Channel Performance** | CTR vs. conversion rate scatter plot (bubble size = spend) |

### Features

- **KPI Cards**: Total spend, revenue, ROI, CTR, conversion rate
- **Interactive Filters**: Channel, region, and date range selection
- **Campaign Data Table**: Detailed campaign-level information
- **Responsive Design**: Works on desktop and tablet screens

---

## Business Impact

| Impact Area | Value Delivered |
|-------------|-----------------|
| **Budget Optimization** | Identify high-performing channels to allocate more spend |
| **Campaign Selection** | Surface top-performing campaigns for scaling |
| **Cost Reduction** | Flag underperforming campaigns to reduce wasteful spend |
| **Faster Decisions** | Self-service dashboard reduces reliance on data teams |
| **Revenue Forecasting** | Predict expected revenue to plan marketing goals |

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Marketing Teams** | Evaluate channel performance and optimize budget allocation |
| **Digital Agencies** | Report campaign ROI to clients with visual dashboards |
| **Startups** | Make data-driven decisions with limited marketing budget |
| **E-commerce** | Track customer acquisition costs and campaign profitability |
| **Freelance Marketers** | Demonstrate analytical skills to potential clients |

---

## Limitations

- **Data Source**: Uses synthetic data generated for demonstration; real-world data would contain additional complexity and noise
- **Model Scope**: Single-model approach (Random Forest); more advanced ensemble methods could improve predictions
- **Geographic Scope**: Focused on a limited set of regions; can be extended for multi-country analysis
- **Real-time Capability**: Batch-processed pipeline; production deployment would require database integration

---

## Future Enhancements

- [ ] A/B test analysis for comparing campaign variants
- [ ] Anomaly detection to identify suspicious traffic patterns
- [ ] Budget optimization recommendations based on ROI projections
- [ ] Automated report generation for stakeholder presentations
- [ ] Integration with cloud data warehouses for real-time processing
- [ ] Time series forecasting (Prophet/ARIMA) for revenue prediction
- [ ] LLM-powered natural language queries for campaign insights

---

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Logesh Kannan**  
Data Analytics Professional

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/logeshkannan19)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/logeshkannan19)

---

<p align="center">
  <em>Last Updated: April 2026</em>
</p>
