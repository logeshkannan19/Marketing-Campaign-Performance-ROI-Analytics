# Contributing to Marketing Campaign Analytics

Thank you for your interest in contributing to this project.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request:
1. Search existing issues to avoid duplicates
2. Open a new issue with:
   - Clear description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior

### Pull Request Guidelines

- **Code Quality**: Follow PEP 8 style guidelines
- **Documentation**: Add docstrings for new functions
- **Testing**: Verify scripts run without errors
- **Commit Messages**: Use clear, descriptive messages

### Development Setup

```bash
# Clone and setup
git clone https://github.com/logeshkannan19/Marketing-Campaign-Performance-ROI-Analytics.git
cd Marketing-Campaign-Performance-ROI-Analytics

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python main.py all
```

## Contribution Areas

| Area | Description |
|------|-------------|
| **Dashboard** | New Plotly visualizations, metrics, UI improvements |
| **Machine Learning** | Time-series forecasting, model ensembling |
| **Data Integration** | API connections (Google Analytics, Meta Ads) |
| **SQL Analytics** | CLTV calculations, cohort analysis |

## Code Style

- Use type hints where appropriate
- Add docstrings to all public functions
- Keep functions focused and modular
- Use meaningful variable names
