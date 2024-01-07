from setuptools import setup, find_packages

setup(
    name='Final Project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # No dependencies required
    ],
    author='Lyna Herhar',
    author_email='lyna.hr2005@gmail.com',
    description='A simple tool for financial market analysis, calculating Simple Moving Averages (SMA) and Relative Strength Index (RSI).',
    long_description="""
    This project, Financial Indicator Analysis Tool, is a Python-based application designed to process historical stock data for technical analysis. It reads data from a 'orcl.csv' file, which contains historical pricing information about a stock. The script performs two primary analyses: it calculates the Simple Moving Averages (SMA) over a 5-day window and the Relative Strength Index (RSI) over a 14-day window.

    After performing the calculations, the project writes the resulting SMA and RSI values into separate CSV files named 'orcl-sma.csv' and 'orcl-rsi.csv', respectively. This structured output enables users to easily consume the data for further analysis, visualization, or integration with other tools and platforms.

    The tool is implemented with straightforward Python code, making it accessible for further modifications and extensions by users with a basic understanding of Python and financial market analysis. The simplicity and modularity of the code base encourage customization and further development to suit more specialized or advanced needs.

    The script is designed to be run from the command line. Ensure that the 'orcl.csv' file is present in the 'data' directory and simply execute the script. The user will be notified upon successful completion of the analysis with the message "Done!... YOU NAILED IT LINA!"
    """,
    license='MIT',
    url='https://github.com/yourusername/yourrepositoryname',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Currency Market Enthusiasts',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    package_data={
        # data file 
        'FINAL-PROJECT': ['data/orcl.csv'],
    },
)
