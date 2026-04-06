<!-- markdownlint-disable MD033 MD041 -->
<div align="center">

# Marketing Campaign Performance & ROI Analytics

<p>

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)
[![Pipeline](https://img.shields.io/badge/Pipeline-ETL%20-orange?style=for-the-badge&logo=github-actions)]()
[![ML Model](https://img.shields.io/badge/ML-Random%20Forest-green?style=for-the-badge&logo=scikit-learn)]()
[![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red?style=for-the-badge&logo=streamlit)]()
[![Stars](https://img.shields.io/github/stars/logeshkannan19/Marketing-Campaign-Performance-ROI-Analytics?style=for-the-badge)]()
[![Forks](https://img.shields.io/github/forks/logeshkannan19/Marketing-Campaign-Performance-ROI-Analytics?style=for-the-badge)]()

</p>

> Enterprise-grade analytics platform for tracking, analyzing, and optimizing marketing campaign performance across digital channels with machine learning and interactive dashboards.

[Overview](#overview) •
[Features](#features) •
[Architecture](#architecture) •
[Tech Stack](#tech-stack) •
[Quick Start](#quick-start) •
[Demo](#demo) •
[Contributing](#contributing)

---

</div>

## 📌 Overview

Marketing teams often struggle to answer critical business questions:

- Which advertising channels deliver the best ROI?
- Is budget being allocated efficiently across campaigns?
- What is the actual cost per customer acquisition?

This project provides a **data-driven framework** to evaluate campaign effectiveness and optimize marketing spend through an end-to-end analytics pipeline.

### Key Highlights

| Metric | Value |
|--------|-------|
| **Dataset Size** | 8,000+ records |
| **ML Model** | Random Forest (R² = 0.70) |
| **Dashboard** | Streamlit Interactive UI |
| **Pipeline** | End-to-End ETL |
| **KPI Metrics** | CTR, CPC, ROI, CAC |

---

## ✨ Features

### 🔄 Data Pipeline

| Feature | Description |
|---------|-------------|
| **Data Generation** | Synthetic marketing campaign data with realistic metrics |
| **Data Preprocessing** | Handles missing values, removes duplicates |
| **Feature Engineering** | CTR, CPC, Conversion Rate, ROI, CAC calculations |

### 🤖 Machine Learning

| Feature | Description |
|---------|-------------|
| **Revenue Prediction** | Random Forest regression model |
| **Feature Importance** | Identifies key revenue drivers |
| **Model Evaluation** | R², RMSE, MAE metrics |

### 📊 Dashboard

| Feature | Description |
|---------|-------------|
| **KPI Overview** | Total spend, revenue, ROI, CTR, conversion rate |
| **Interactive Charts** | ROI by channel, top campaigns, monthly trends |
| **Multi-dimensional Filtering** | By channel, region, and date range |
| **Data Table** | Campaign-level detail view |

---

## 🏗️ Architecture

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
| 2 | Preprocessing | Cleans data, calculates derived KPIs |
| 3 | ML Model | Trains Random Forest to predict revenue |
| 4 | Dashboard | Visualizes insights for stakeholders |

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" height="18"> Python 3.8+ |
| **Data Processing** | <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white" height="18"> Pandas, NumPy |
| **Machine Learning** | <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white" height="18"> Scikit-learn |
| **Visualization** | <img src="https://img.shields.io/badge/Plotly-3F4B75?style=flat&logo=plotly&logoColor=white" height="18"> Plotly, Matplotlib |
| **Dashboard** | <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" height="18"> Streamlit |
| **CLI** | <img src="https://img.shields.io/badge/Click-000000?style=flat&logo=click&logoColor=white" height="18"> Click |
| **Testing** | <img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white" height="18"> pytest |

---

## 📂 Project Structure

```
marketing-campaign-roi-analytics/
├── data/                          # Data directory
│   ├── raw_data.csv               # Generated raw campaign data
│   └── cleaned_data.csv           # Preprocessed data
├── src/                           # Source modules
│   ├── data_generator.py          # Synthetic data generation
│   └── data_preprocessing.py      # Data cleaning & feature engineering
├── models/                        # ML models
│   └── predict_performance.py     # Revenue prediction model
├── dashboard/                     # Dashboard application
│   └── app.py                    # Streamlit dashboard
├── outputs/                       # Generated outputs
│   └── reports/                   # Model metrics & reports
├── notebooks/                     # Jupyter notebooks
│   └── eda_analysis.ipynb         # EDA analysis
├── tests/                         # Test suite
│   └── test_pipeline.py           # Unit tests
├── scripts/                       # Utility scripts
├── ARCHITECTURE.md                # Architecture documentation
├── CONTRIBUTING.md               # Contribution guidelines
├── ROADMAP.md                     # Project roadmap
├── LICENSE                        # MIT License
└── README.md                      # Project documentation
```

---

## 🚀 Quick Start

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
```

### Usage

```bash
# Run the full pipeline
python main.py all

# Run individual components
python main.py generate      # Generate synthetic data
python main.py preprocess     # Clean and preprocess data
python main.py model          # Train prediction model
python main.py dashboard      # Launch interactive dashboard
```

### Using Make

```bash
make install          # Install dependencies
make all             # Run complete pipeline
make test            # Run tests
make docker-build    # Build Docker image
```

The dashboard will be available at `http://localhost:8501`.

---

## 📊 Key Metrics

| Metric | Formula | Business Significance |
|--------|---------|----------------------|
| **CTR** (Click-Through Rate) | Clicks ÷ Impressions | Measures ad visibility and appeal |
| **Conversion Rate** | Conversions ÷ Clicks | Indicates landing page effectiveness |
| **CPC** (Cost Per Click) | Cost ÷ Clicks | Measures efficiency of ad spend |
| **ROI** (Return on Investment) | (Revenue - Cost) ÷ Cost | Overall profitability |
| **CAC** (Customer Acquisition Cost) | Cost ÷ Conversions | Customer acquisition efficiency |

---

## 📈 Model Performance

### Evaluation Metrics

| Metric | Value |
|--------|-------|
| **R² Score** | 0.70 |
| **RMSE** | $5,489 |
| **MAE** | $2,002 |

### Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 🥇 | Clicks | 68.2% |
| 🥈 | Conversion Rate | 14.4% |
| 🥉 | CTR | 4.7% |
| 4 | Impressions | 3.7% |
| 5 | Cost | 2.6% |

---

## 💼 Business Impact

| Impact Area | Value Delivered |
|-------------|-----------------|
| 📈 **Budget Optimization** | Identify high-performing channels for spend allocation |
| 🎯 **Campaign Selection** | Surface top-performing campaigns for scaling |
| 💰 **Cost Reduction** | Flag underperforming campaigns to reduce wasteful spend |
| ⚡ **Faster Decisions** | Self-service dashboard reduces reliance on data teams |
| 🔮 **Revenue Forecasting** | Predict expected revenue to plan marketing goals |

---

## 📌 Use Cases

| Use Case | Description |
|----------|-------------|
| **Marketing Teams** | Evaluate channel performance and optimize budget allocation |
| **Digital Agencies** | Report campaign ROI to clients with visual dashboards |
| **Startups** | Make data-driven decisions with limited marketing budget |
| **E-commerce** | Track customer acquisition costs and campaign profitability |
| **Freelance Marketers** | Demonstrate analytical skills to potential clients |

---

## ⚠️ Limitations

- **Data Source**: Uses synthetic data for demonstration; real-world data would have additional complexity
- **Model Scope**: Single Random Forest model; ensemble methods could improve predictions
- **Geographic Scope**: Focused on limited regions; extendable for multi-country analysis
- **Real-time Capability**: Batch-processed pipeline; production would require database integration

---

## 🔮 Future Enhancements

- [ ] A/B test analysis for campaign variant comparison
- [ ] Anomaly detection for suspicious traffic patterns
- [ ] Budget optimization recommendations
- [ ] Automated report generation
- [ ] Cloud data warehouse integration
- [ ] Time series forecasting (Prophet/ARIMA)
- [ ] LLM-powered natural language queries

---

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Logesh Kannan**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/logeshkannan19)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/logeshkannan19)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=flat&logo=twitter&logoColor=white)]()

---

<p align="center">
  Made with ❤️ by Logesh Kannan
</p>

</div>
