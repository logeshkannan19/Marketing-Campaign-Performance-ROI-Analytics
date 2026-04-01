# Marketing Campaign Performance & ROI Analytics

## 📌 Project Overview
The **Marketing Campaign Performance & ROI Analytics** project is an end-to-end data analytics and predictive modeling solution designed to evaluate marketing campaign effectiveness, Return on Investment (ROI), and optimization strategies across various digital channels. 

Through robust data preprocessing, exploratory data analysis (EDA), SQL queries, machine learning, and an interactive Streamlit dashboard, this project provides actionable insights to help marketing teams optimize their ad spending and maximize revenue generation.

---

## 🚀 Features

- **Synthetic Data Generation**: Automates the creation of realistic raw marketing data.
- **Data Preprocessing**: Handles missing values, deduplication, and feature engineering for core metrics:
  - **CTR** (Click-Through Rate)
  - **Conversion Rate**
  - **CPC** (Cost Per Click)
  - **ROI** (Return on Investment)
- **SQL Analysis**: Aggregates top-performing campaigns, channel metrics, and regional insights.
- **Exploratory Data Analysis (EDA)**: Interactive geographic, channel, and time-series profiling.
- **Predictive Modeling**: Uses a Random Forest Regressor to predict revenue and highlight the most critical features dictating campaign success.
- **Streamlit Dashboard**: A fully interactive, production-ready frontend for marketers to visually slice and dice KPI metrics.

---

## 🛠 Tech Stack

- **Data Processing**: Python (`pandas`, `numpy`)
- **Database & Querying**: SQL
- **Machine Learning**: Python (`scikit-learn`)
- **Data Visualization & Dashboard**: Streamlit, Plotly, Matplotlib, Seaborn

---

## 📂 Project Structure

```text
Marketing-Analytics-ROI/
│
├── data/
│   ├── raw/                  # Generated raw marketing campaign data
│   └── processed/            # Cleaned data with calculated KPIs
│
├── src/                      # Source scripts
│   ├── data_generator.py     # Generates raw dataset
│   └── data_preprocessing.py # Cleans and engineers features
│
├── sql/
│   └── analysis_queries.sql  # SQL scripts for data aggregation
│
├── notebooks/
│   └── eda_analysis.ipynb    # Jupyter notebook for exploratory data analysis
│
├── models/
│   └── predict_performance.py# ML script for predicting campaign revenue
│
├── dashboard/
│   └── app.py                # Streamlit dashboard application
│
├── reports/                  # Generated ML feature importances and insights
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## 💡 Key Business Insights

1. **Best Performing Channels**: Assesses which marketing channels (e.g., Google Ads vs. Facebook) drive the highest ROI.
2. **Budget Allocation Optimization**: The Predictive ML model explicitly extracts feature importances to highlight whether impressions, specific regions, or target audiences directly correlate to top-line revenue.
3. **Inefficient Spend Detection**: Easily isolates campaigns that have high CPC but remarkably low Conversion Rates to reallocate marketing dollars towards more efficient funnels.

---

## ⚙️ How to Run

**1. Clone the repository and navigate to the project directory:**
```bash
git clone https://github.com/yourusername/Marketing-Analytics-ROI.git
cd Marketing-Analytics-ROI
```

**2. Create a virtual environment and install dependencies:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Generate and preprocess data:**
```bash
python3 src/data_generator.py
python3 src/data_preprocessing.py
```

**4. Run advanced predictive analytics (Optional):**
```bash
python3 models/predict_performance.py
```

**5. Launch the Streamlit Dashboard:**
```bash
streamlit run dashboard/app.py
```

---

*This project is designed as a portfolio-quality demonstration of full-cycle analytics, engineering, and predictive modeling.*
