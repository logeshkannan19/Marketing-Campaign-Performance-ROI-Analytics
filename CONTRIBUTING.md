# Contributing to Marketing Analytics & ROI Project

First off, thank you for considering contributing to this repository. It's people like you that make the open-source community such a great place to learn, inspire, and create.

## 1. Where do I go from here?

If you've noticed a bug or have a feature request/idea, please **open an issue** before submitting a Pull Request.

## 2. Setting up your environment

1. **Fork & Clone** the repository.
2. Ensure you have Python 3.9+ installed.
3. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Generate the baseline data and run the preprocessing scripts:
   ```bash
   python3 src/data_generator.py
   python3 src/data_preprocessing.py
   ```

## 3. Pull Request Guidelines

- **Code Quality**: Ensure that your Python scripts are clean, human-readable, and well-commented.
- **Docstrings**: If you are adding new functions to `src/` or `models/`, include standard docstrings detailing inputs, outputs, and purpose.
- **Testing**: Whenever possible, ensure your scripts run end-to-end without throwing exceptions before submitting.
- **Commit Messages**: Write clear, descriptive commit messages.

## 4. Areas for Contribution

We actively welcome contributions in the following areas:
- **Dashboard Enhancements**: Adding new interactive Plotly charts, expanding the Streamlit metrics, or improving the mobile responsiveness of the UI.
- **Advanced Machine Learning**: Upgrading the predictive engine to include Time-Series forecasting (ARIMA/Prophet) for future revenue prediction.
- **Data Integrations**: Providing scripts to connect to live API feeds (e.g. Google Analytics, Facebook Graph API) instead of relying solely on synthetic generation.
- **SQL Transformations**: Expanding `analysis_queries.sql` to include Customer Lifetime Value (CLTV) estimates and advanced cohort behaviors.

## 5. Reporting Bugs

If you find a bug, please create a GitHub Issue detailing:
- The traceback or error message
- The operating system and python version
- The exact steps needed to replicate the error
