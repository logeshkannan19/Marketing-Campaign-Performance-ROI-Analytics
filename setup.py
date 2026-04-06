"""
Setup configuration for Marketing Campaign Analytics
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="marketing-campaign-analytics",
    version="1.0.0",
    author="Logesh Kannan",
    author_email="logeshkannan19@example.com",
    description="Enterprise-grade analytics platform for marketing campaign performance and ROI optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/logeshkannan19/Marketing-Campaign-Performance-ROI-Analytics",
    project_urls={
        "Bug Tracker": "https://github.com/logeshkannan19/Marketing-Campaign-Performance-ROI-Analytics/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "marketing-analytics=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
