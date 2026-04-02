import os
import sys
import subprocess


def check_data_exists():
    raw_exists = os.path.exists('data/raw_data.csv')
    cleaned_exists = os.path.exists('data/cleaned_data.csv')
    return raw_exists, cleaned_exists


def run_data_generation():
    print("\n" + "="*50)
    print("STEP 1: Generating Raw Data")
    print("="*50 + "\n")
    from src.data_generator import generate_dataset, save_to_csv
    df = generate_dataset()
    output_path = save_to_csv(df, 'data')
    print(f"\nData generation complete!")
    print(f"  Output: {output_path}")
    print(f"  Records: {len(df)}")


def run_preprocessing():
    print("\n" + "="*50)
    print("STEP 2: Preprocessing Data")
    print("="*50 + "\n")
    from src.data_preprocessing import preprocess_data
    preprocess_data(input_path='data/raw_data.csv', output_path='data/cleaned_data.csv')


def run_model():
    print("\n" + "="*50)
    print("STEP 3: Training Prediction Model")
    print("="*50 + "\n")
    from models.predict_performance import run_pipeline
    run_pipeline()


def launch_dashboard():
    print("\n" + "="*50)
    print("STEP 4: Launching Dashboard")
    print("="*50 + "\n")
    try:
        import streamlit
    except ImportError:
        print("ERROR: Streamlit not installed.")
        print("Run: pip install streamlit")
        return
    print("Starting Streamlit dashboard...")
    print("Dashboard will open at: http://localhost:8501")
    dashboard_path = os.path.join(os.path.dirname(__file__), 'dashboard', 'app.py')
    subprocess.run(['streamlit', 'run', dashboard_path])


def print_help():
    print("""
Marketing Campaign Analytics - Main Pipeline
==============================================

Usage: python main.py [command]

Commands:
  all           Run full pipeline
  generate      Generate synthetic data
  preprocess    Clean and preprocess data
  model         Train prediction model
  dashboard     Launch dashboard
  help          Show this help message

Examples:
  python main.py all
  python main.py dashboard
    """)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Marketing Campaign Analytics Pipeline')
    parser.add_argument('command', nargs='?', default='help', choices=['all', 'generate', 'preprocess', 'model', 'dashboard', 'help'])
    args = parser.parse_args()
    
    if args.command == 'help':
        print_help()
        return
    
    raw_exists, cleaned_exists = check_data_exists()
    
    if args.command == 'all':
        if not raw_exists:
            run_data_generation()
        else:
            print("\nRaw data already exists, skipping generation.")
        run_preprocessing()
        run_model()
        launch_dashboard()
    
    elif args.command == 'generate':
        run_data_generation()
    
    elif args.command == 'preprocess':
        if not raw_exists:
            print("ERROR: Raw data not found. Run 'generate' first.")
            return
        run_preprocessing()
    
    elif args.command == 'model':
        if not cleaned_exists:
            print("ERROR: Cleaned data not found. Run 'preprocess' first.")
            return
        run_model()
    
    elif args.command == 'dashboard':
        if not cleaned_exists:
            print("ERROR: Cleaned data not found. Run 'preprocess' first.")
            return
        launch_dashboard()


if __name__ == "__main__":
    main()