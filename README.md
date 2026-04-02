# Marketing Campaign Performance & ROI Analytics

An end-to-end data analytics solution for tracking, analyzing, and optimizing marketing campaign performance across digital channels.

---

## ✨ Key Highlights

- **Complete Data Pipeline**: End-to-end flow from raw data generation to actionable insights
- **ML Model**: Random Forest regressor achieving **R² = 0.70** for revenue prediction
- **Interactive Dashboard**: Streamlit-based UI with filters for channel, region, and date range
- **Feature Analysis**: Identifies top revenue drivers (clicks: 68%, conversion rate: 14%)
- **5 Key Metrics**: CTR, CPC, Conversion Rate, ROI, and CAC with business context
- **8,000+ Records**: Realistic synthetic dataset simulating real marketing campaigns

---

## Problem Statement

Marketing teams frequently face challenges in answering critical business questions:

- Which advertising channels deliver the best return on investment?
- Are we allocating budget efficiently across campaigns?
- Which audience segments are driving conversions?
- What is our actual cost per customer acquisition?

Without a structured approach to analyzing campaign data, marketing decisions often rely on intuition rather than evidence. This project addresses the need for a data-driven framework to evaluate campaign effectiveness and optimize marketing spend.

---

## Project Overview

This project demonstrates a complete analytics pipeline that transforms raw marketing campaign data into actionable business insights. It includes data generation, preprocessing, machine learning-based revenue prediction, and an interactive visualization dashboard.

The solution is designed to help marketing teams make informed budget allocation decisions by providing clear visibility into channel performance, campaign ROI, and audience behavior.

---

## Business Impact

In a real-world setting, this analytics system would provide:

| Impact Area | Value |
|-------------|-------|
| **Budget Optimization** | Identify high-performing channels to allocate more spend |
| **Campaign Selection** | Surface top-performing campaigns for scaling |
| **Cost Reduction** | Flag underperforming campaigns to reduce wasteful spend |
| **Faster Decisions** | Self-service dashboard reduces reliance on data teams |
| **Revenue Forecasting** | Predict expected revenue to plan marketing goals |

---

## Use Cases

This project is applicable in various marketing and business scenarios:

- **Marketing Teams** → Evaluate channel performance and optimize budget allocation
- **Digital Agencies** → Report campaign ROI to clients with visual dashboards
- **Startups** → Make data-driven decisions with limited marketing budget
- **E-commerce Businesses** → Track customer acquisition costs and campaign profitability
- **Freelance Marketers** → Demonstrate analytical skills to potential clients

---

## Architecture Overview

```
┌─────────────┐    ┌───────────────┐    ┌─────────────┐    ┌─────────────┐
│    Data     │───▶│  Processing   │───▶│ ML Model    │───▶│  Dashboard  │
│ Generation  │    │ & Cleaning    │    │ (RandomForest)│   │ (Streamlit) │
└─────────────┘    └───────────────┘    └─────────────┘    └─────────────┘
     8K+               Derived KPIs        R² = 0.70        Interactive
   Records             CTR, CPC,          Revenue            Charts
                       ROI, CAC           Prediction
```

**Pipeline Flow:**
1. **Data Generation** → Creates 8,000+ marketing records
2. **Processing** → Cleans data, calculates CTR, CPC, ROI, CAC
3. **ML Model** → Trains Random Forest to predict revenue
4. **Dashboard** → Visualizes insights for non-technical users

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Data Generation** | Creates synthetic marketing data simulating real-world metrics (impressions, clicks, conversions, cost, revenue) |
| **Data Preprocessing** | Handles missing values, removes duplicates, and calculates derived KPIs (CTR, CPC, conversion rate, ROI, CAC) |
| **Predictive Modeling** | Uses Random Forest regression to identify factors that most significantly impact revenue |
| **Interactive Dashboard** | Streamlit-based UI with filtering capabilities for exploring campaign performance by channel, region, and time period |
| **Feature Importance Analysis** | Identifies which campaign attributes drive the most value for budget planning |

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python |
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
│   ├── raw_data.csv           # Generated raw campaign data
│   └── cleaned_data.csv       # Preprocessed data with derived metrics
├── src/
│   ├── data_generator.py      # Synthetic data generation module
│   └── data_preprocessing.py  # Data cleaning and feature engineering
├── models/
│   └── predict_performance.py # ML model training and evaluation
├── dashboard/
│   └── app.py                 # Streamlit dashboard application
├── outputs/
│   └── reports/               # Generated model metrics and feature importance
├── main.py                    # CLI entry point for pipeline execution
└── requirements.txt           # Project dependencies
```

---

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run full pipeline (generates data, cleans, trains model, launches dashboard)
python main.py all

# Alternative: Run individual steps
python main.py generate   # Generate synthetic data
python main.py preprocess # Clean and preprocess data
python main.py model      # Train prediction model
python main.py dashboard # Launch dashboard
```

The dashboard will be available at `http://localhost:8501`.

---

## Output Preview

### Dashboard Overview
![Dashboard Screenshot](screenshots/dashboard_overview.png)

### Key Visualizations Included
| Chart | What It Shows |
|-------|---------------|
| **ROI by Channel** | Bar chart comparing ROI across Google Ads, Facebook, Email, Instagram, LinkedIn |
| **Top Campaigns** | Top 10 campaigns ranked by revenue |
| **Monthly Trends** | 12-month spend vs. revenue line chart |
| **Channel Performance** | CTR vs. conversion rate scatter plot (bubble size = spend) |

### Model Performance

| Metric | Value |
|--------|-------|
| **R² Score** | 0.70 |
| **RMSE** | $5,489 |
| **MAE** | $2,002 |

### Top Feature Importances
| Rank | Feature | Importance |
|------|---------|------------|
| 1 | Clicks | 68.2% |
| 2 | Conversion Rate | 14.4% |
| 3 | CTR | 4.7% |
| 4 | Impressions | 3.7% |
| 5 | Cost | 2.6% |

---

## Key Metrics

| Metric | Formula | Business Significance |
|--------|---------|---------------------|
| **CTR** (Click-Through Rate) | Clicks ÷ Impressions | Measures ad visibility and appeal |
| **Conversion Rate** | Conversions ÷ Clicks | Indicates landing page effectiveness |
| **CPC** (Cost Per Click) | Cost ÷ Clicks | Measures efficiency of ad spend |
| **ROI** (Return on Investment) | (Revenue - Cost) ÷ Cost | Overall profitability of campaign |
| **CAC** (Customer Acquisition Cost) | Cost ÷ Conversions | Customer acquisition efficiency |

---

## Why This Project Stands Out

- **End-to-End**: Complete pipeline from raw data → cleaning → ML → dashboard
- **Business-Focused**: Explains *why* metrics matter, not just what they are
- **ML + UI**: Combines predictive modeling with user-friendly visualization
- **Production-Like Structure**: Proper modular code, CLI entry point, documented functions
- **Realistic Scope**: Student project with honest limitations but meaningful results

---

## Learning Outcomes

This project provided hands-on experience in:

- Designing and implementing a complete data pipeline (ingestion → transformation → analysis)
- Handling real-world data quality challenges (missing values, duplicates, invalid entries)
- Building and evaluating machine learning models for business prediction
- Creating interactive dashboards that enable non-technical users to derive insights
- Translating technical findings into business recommendations

---

## Limitations

- **Data Source**: Uses synthetic data generated for demonstration purposes; real-world data would contain additional complexity and noise
- **Model Scope**: Single-model approach (Random Forest); more advanced ensemble methods or time-series models could improve predictions
- **Geographic Scope**: Focused on a limited set of regions; can be extended for multi-country analysis
- **Real-time Capability**: Batch-processed pipeline; production deployment would require database integration and scheduled jobs

---

## Future Improvements

- Implement A/B test analysis for comparing campaign variants
- Add anomaly detection to identify suspicious traffic patterns
- Develop budget optimization recommendations based on ROI projections
- Enable automated report generation for stakeholder presentations
- Integrate with cloud data warehouses for real-time data processing

---

## Author

**Logesh Kannan**  
Data Analytics Student | Aspiring Data Analyst

This project was developed as part of my learning journey in data analytics. It demonstrates my ability to build end-to-end analytics solutions—from data processing and machine learning to building user-facing applications that drive business value.

I'm actively seeking opportunities to apply these skills in real-world data analytics roles.

---

*Last Updated: April 2026*