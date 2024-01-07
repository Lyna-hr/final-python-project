# Financial Indicator Analysis Tool

## Description
This Python script is designed to analyze financial data, specifically calculating the Simple Moving Averages (SMA) and Relative Strength Index (RSI) from historical stock data. The script reads from a CSV file containing stock prices (`orcl.csv`), performs the calculations, and outputs the results to separate CSV files.

## Installation
No installation is required. You can run this script with Python 3.x.

## Usage
Place the `orcl.csv` file with your historical stock data into the `data` directory. Then, run the script from the command line:

```bash
python main.py
```

The script will produce two output files:

data/orcl-sma.csv for the Simple Moving Averages
data/orcl-rsi.csv for the Relative Strength Index

