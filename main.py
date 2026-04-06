#!/usr/bin/env python3
"""
Marketing Campaign Performance & ROI Analytics
Main CLI Entry Point

A command-line interface for executing the complete analytics pipeline:
data generation, preprocessing, ML model training, and dashboard launch.
"""

import os
import sys
from pathlib import Path

import click


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
    click.echo("\n" + "=" * 60)
    click.echo("STEP 1: Data Generation")
    click.echo("=" * 60 + "\n")

    from src.data_generator import generate_dataset, save_to_csv

    df = generate_dataset()
    output_path = save_to_csv(df, str(DATA_DIR))

    click.echo(click.style("✓ Data generation complete", fg="green"))
    click.echo(f"  Output: {output_path}")
    click.echo(f"  Records: {len(df):,}")


def run_preprocessing():
    """Execute data preprocessing module."""
    click.echo("\n" + "=" * 60)
    click.echo("STEP 2: Data Preprocessing")
    click.echo("=" * 60 + "\n")

    from src.data_preprocessing import preprocess_data

    preprocess_data(
        input_path=str(DATA_DIR / "raw_data.csv"),
        output_path=str(DATA_DIR / "cleaned_data.csv")
    )


def run_model():
    """Execute ML model training."""
    click.echo("\n" + "=" * 60)
    click.echo("STEP 3: ML Model Training")
    click.echo("=" * 60 + "\n")

    from models.predict_performance import run_pipeline

    run_pipeline()


def launch_dashboard():
    """Launch Streamlit dashboard."""
    click.echo("\n" + "=" * 60)
    click.echo("STEP 4: Launching Dashboard")
    click.echo("=" * 60 + "\n")

    try:
        import streamlit
    except ImportError:
        click.echo(click.style("ERROR: Streamlit not installed.", fg="red"))
        click.echo("Run: pip install streamlit")
        return

    click.echo("Starting Streamlit dashboard...")
    click.echo("Dashboard will open at: http://localhost:8501")
    click.echo("(Press Ctrl+C to stop)\n")

    dashboard_path = PROJECT_ROOT / "dashboard" / "app.py"
    import subprocess
    subprocess.run(["streamlit", "run", str(dashboard_path)])


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Marketing Campaign Analytics - Pipeline CLI."""
    pass


@cli.command()
def all():
    """Run complete pipeline (generate → preprocess → model → dashboard)."""
    raw_exists, _ = check_data_exists()

    if not raw_exists:
        run_data_generation()
    else:
        click.echo(click.style("[INFO] Raw data already exists, skipping generation.", fg="yellow"))

    run_preprocessing()
    run_model()
    launch_dashboard()


@cli.command()
def generate():
    """Generate synthetic campaign data."""
    run_data_generation()


@cli.command()
def preprocess():
    """Clean and preprocess data."""
    raw_exists, _ = check_data_exists()

    if not raw_exists:
        click.echo(click.style("ERROR: Raw data not found. Run 'generate' first.", fg="red"))
        return

    run_preprocessing()


@cli.command()
def model():
    """Train revenue prediction model."""
    _, cleaned_exists = check_data_exists()

    if not cleaned_exists:
        click.echo(click.style("ERROR: Cleaned data not found. Run 'preprocess' first.", fg="red"))
        return

    run_model()


@cli.command()
def dashboard():
    """Launch interactive dashboard."""
    _, cleaned_exists = check_data_exists()

    if not cleaned_exists:
        click.echo(click.style("ERROR: Cleaned data not found. Run 'preprocess' first.", fg="red"))
        return

    launch_dashboard()


if __name__ == "__main__":
    cli()
