# Product Roadmap: Marketing Analytics & ROI

This roadmap outlines the planned future capabilities and architectural evolutions for this repository.

## Phase 1: Core Foundation & Prototyping (✅ Completed)
- [x] Synthetic data generation emphasizing realistic edge-cases and marketing constraints.
- [x] Robust data preprocessing pipeline (cleaning NaN values, deduplication).
- [x] Engineering core KPIs (CTR, CPC, Conversion Rate, ROI).
- [x] Streamlit dashboard with interactive KPI cards and cross-filtering.
- [x] Foundational Random Forest predictive modeling for revenue estimation.

## Phase 2: Orchestration & Data Warehousing (In Progress)
- [ ] **SQL Database Migration**: Move from static CSV reading to robust PostgreSQL / SQLite instances.
- [ ] **dbt Integration**: Implement Data Build Tool (dbt) to handle the transformations previously managed purely by pandas.
- [ ] **Data Orchestration**: Introduce Apache Airflow DAGs to orchestrate the daily extraction, transformation, and dashboard refreshing routines.

## Phase 3: Advanced Analytics & AI
- [ ] **Time Series Forecasting**: Integrate Prophet or ARIMA to forecast future marketing spends and predicted revenue peaks.
- [ ] **LLM Data Assistant**: Implement an OpenAI-powered chatbot directly inside the Streamlit dashboard allowing marketers to "chat" with their campaign data for natural-language answers.
- [ ] **Attribution Modeling**: Support multi-touch attribution (MTA) models to measure cross-channel impact (e.g. first click vs. last click vs. linear).

## Phase 4: Production & Deployment
- [ ] **Dockerization**: Create Dockerfiles for both the backend transformation pipelines and the Streamlit frontend.
- [ ] **CI/CD Pipelines**: Setup GitHub Actions for automated testing, linting, and deployment of the application.
- [ ] **Cloud Hosting**: Deploy the dashboard persistently on AWS EC2, Streamlit Community Cloud, or Heroku.
