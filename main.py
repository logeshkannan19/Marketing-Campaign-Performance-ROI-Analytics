"""
Marketing Campaign Performance & ROI Analytics
Main CLI Entry Point

A command-line interface for executing the complete analytics pipeline:
data generation, preprocessing, ML model training, and dashboard launch.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"


def check_data_exists():
    """Check if required data files exist."""
    raw_exists = DATA_DIR.exists() and (DATA_DIR / "raw_data.csv").exists()
    cleaned_exists = DATA_DIR.exists() and (DATA_DIR / "cleaned_data.csv").exists()
    return raw_exists, cleaned_exists


def run_data_generation():
    """Execute data generation module."""
    print("\n" + "=" * 60)
    print("STEP 1: Data Generation")
    print("=" * 60 + "\n")
    
    from src.data_generator import generate_dataset, save_to_csv
    
    df = generate_dataset()
    output_path = save_to_csv(df, str(DATA_DIR))
    
    print(f"\n✓ Data generation complete")
    print(f"  Output: {output_path}")
    print(f"  Records: {len(df):,}")


def run_preprocessing():
    """Execute data preprocessing module."""
    print("\n" + "=" * 60)
    print("STEP 2: Data Preprocessing")
    print("=" * 60 + "\n")
    
    from src.data_preprocessing import preprocess_data
    
    preprocess_data(
        input_path=str(DATA_DIR / "raw_data.csv"),
        output_path=str(DATA_DIR / "cleaned_data.csv")
    )


def run_model():
    """Execute ML model training."""
    print("\n" + "=" * 60)
    print("STEP 3: ML Model Training")
    print("=" * 60 + "\n")
    
    from models.predict_performance import run_pipeline
    run_pipeline()


def launch_dashboard():
    """Launch Streamlit dashboard."""
    print("\n" + "=" * 60)
    print("STEP 4: Launching Dashboard")
    print("=" * 60 + "\n")
    
    try:
        import streamlit
    except ImportError:
        print("ERROR: Streamlit not installed.")
        print("Run: pip install streamlit")
        return
    
    print("Starting Streamlit dashboard...")
    print("Dashboard will open at: http://localhost:8501")
    print("(Press Ctrl+C to stop)\n")
    
    dashboard_path = PROJECT_ROOT / "dashboard" / "app.py"
    subprocess.run(["streamlit", "run", str(dashboard_path)])


def print_help():
    """Display help message."""
    print("""
Marketing Campaign Analytics - Pipeline CLI
=============================================

Usage: python main.py <command>

Commands:
  all           Run complete pipeline (generate → preprocess → model → dashboard)
  generate      Generate synthetic campaign data
  preprocess    Clean and preprocess data
  model         Train revenue prediction model
  dashboard     Launch interactive dashboard
  help          Show this help message

Examples:
  python main.py all
  python main.py generate
  python main.py dashboard
    """)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Marketing Campaign Analytics Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="help",
        choices=["all", "generate", "preprocess", "model", "dashboard", "help"]
    )
    args = parser.parse_args()
    
    if args.command == "help":
        print_help()
        return
    
    raw_exists, cleaned_exists = check_data_exists()
    
    if args.command == "all":
        if not raw_exists:
            run_data_generation()
        else:
            print("\n[INFO] Raw data already exists, skipping generation.")
        run_preprocessing()
        run_model()
        launch_dashboard()
    
    elif args.command == "generate":
        run_data_generation()
    
    elif args.command == "preprocess":
        if not raw_exists:
            print("ERROR: Raw data not found. Run 'generate' first.")
            return
        run_preprocessing()
    
    elif args.command == "model":
        if not cleaned_exists:
            print("ERROR: Cleaned data not found. Run 'preprocess' first.")
            return
        run_model()
    
    elif args.command == "dashboard":
        if not cleaned_exists:
            print("ERROR: Cleaned data not found. Run 'preprocess' first.")
            return
        launch_dashboard()


if __name__ == "__main__":
    main()
