from setuptools import setup, find_packages

setup(
    name="PenToolkit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "scapy",          # Network packet manipulation
        "nmap",           # For port and service scanning
        "requests",       # HTTP requests
        "beautifulsoup4", # Web scraping/parsing
        "argparse"        # Command-line parsing (optional)
    ],
)