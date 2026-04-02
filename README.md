# Marketing Campaign ROI Analytics

> End-to-end data pipeline for tracking and optimizing marketing campaign performance.

## The Problem

Marketing teams often struggle to answer basic questions:
- Which channels give us the best ROI?
- Are we overspending on certain campaigns?
- Which audience segments actually convert?
- What's our real cost per acquisition?

Without clear answers, budget decisions become guesswork. This project builds an analytics solution that takes raw campaign data and turns it into actionable insights.

## What This Project Does

1. **Generates realistic test data** - Creates synthetic marketing data that mimics real-world metrics (impressions, clicks, conversions, cost, revenue)

2. **Cleans and transforms data** - Handles missing values, removes duplicates, calculates derived metrics like CTR, conversion rate, CPC, and ROI

3. **Predicts revenue** - Trains a machine learning model to identify which factors drive the most revenue

4. **Provides an interactive dashboard** - Lets marketing teams explore data visually without needing SQL or Python skills

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run full pipeline (generates data, cleans it, trains model, opens dashboard)
python main.py all

# Or run individual steps:
python main.py generate   # Create synthetic data
python main.py preprocess # Clean the data
python main.py model      # Train prediction model
python main.py dashboard  # Open dashboard
```

The dashboard runs at `http://localhost:8501`.

## Project Structure

```
marketing-campaign-roi-analytics/
├── data/                  # Raw and cleaned data
├── src/                   # Source code
│   ├── data_generator.py  # Creates synthetic marketing data
│   └── data_preprocessing.py   # Cleans data, calculates metrics
├── models/
│   └── predict_performance.py  # ML model for revenue prediction
├── dashboard/            # Streamlit dashboard
│   └── app.py
├── outputs/              # Generated reports
├── main.py               # Entry point
└── requirements.txt      # Python dependencies
```

## Tech Stack

- **Python** - Core language
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning (Random Forest)
- **Plotly** - Interactive charts
- **Streamlit** - Web dashboard

## Key Metrics

| Metric | Formula | Why It Matters |
|--------|---------|-----------------|
| CTR | Clicks / Impressions | Measures ad visibility effectiveness |
| Conversion Rate | Conversions / Clicks | Measures landing page performance |
| CPC | Cost / Clicks | Measures efficiency of spend |
| ROI | (Revenue - Cost) / Cost | Bottom-line profitability |
| CAC | Cost / Conversions | Customer acquisition cost |

## What I Learned

Building this project taught me:
- How to structure a data pipeline from raw input to clean output
- Handling real-world data quality issues (missing values, duplicates)
- Why feature selection matters in ML models
- Building interactive dashboards that non-technical users can actually use

## Limitations & Future Work

**Current limitations:**
- Uses synthetic data - real data would have more complexity
- Basic ML model - could try XGBoost or time-series forecasting
- Single-region data - could expand to multi-country analysis
- No real-time updates - would need a database for that

**Nice to have:**
- A/B test analysis for comparing campaign variants
- Anomaly detection for identifying suspicious metrics
- Budget optimization recommendations
- Export to PDF reports for leadership

## Contact

Built by a data analyst learning to build production-quality analytics projects.

---

*This project is for educational/demonstration purposes.*