import json
import os

notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# NDTA 631 - Data Analysis and Visualization\n",
                "## Analyzing the Relationship Between GDP Growth and Unemployment in South Africa\n",
                "\n",
                "This notebook covers Phase 3 (Data Preparation), Phase 4 (NumPy Numerical Analysis), and Phase 5 (Visualization) from the project rubric."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "import sqlite3\n",
                "import os\n",
                "\n",
                "# Set visualization style\n",
                "sns.set_theme(style=\"whitegrid\")\n",
                "\n",
                "# Set database path\n",
                "db_path = '../data/economic_data.db'\n",
                "print(f\"Database path: {db_path}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Phase 3: Data Preparation (15 Marks)\n",
                "We will load the data directly from our SQLite database into a Pandas DataFrame."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Connect to the database and load data\n",
                "conn = sqlite3.connect(db_path)\n",
                "df = pd.read_sql_query(\"SELECT * FROM economic_indicators ORDER BY Year\", conn)\n",
                "conn.close()\n",
                "\n",
                "# Display the first few rows to ensure successful load\n",
                "df.head()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Handle Missing Values (Imputation)\n",
                "# Let's check for missing values\n",
                "missing_values = df.isnull().sum()\n",
                "print(\"Missing Values Before Cleaning:\\n\", missing_values)\n",
                "\n",
                "# We will use linear interpolation to handle any missing data points over the years\n",
                "df['GDP_Growth'] = df['GDP_Growth'].interpolate(method='linear')\n",
                "df['Unemployment_Rate'] = df['Unemployment_Rate'].interpolate(method='linear')\n",
                "\n",
                "# Drop any remaining NaNs (e.g., at the very beginning of the dataset where interpolation fails)\n",
                "df.dropna(inplace=True)\n",
                "\n",
                "print(\"\\nMissing Values After Cleaning:\\n\", df.isnull().sum())"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Generate Descriptive Statistics\n",
                "df.describe()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Phase 4: NumPy Numerical Analysis (20 Marks)\n",
                "We convert the Pandas series into NumPy arrays to perform calculations such as variance, standard deviation, and correlation."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Convert to NumPy Arrays\n",
                "years_arr = np.array(df['Year'])\n",
                "gdp_arr = np.array(df['GDP_Growth'])\n",
                "unemp_arr = np.array(df['Unemployment_Rate'])\n",
                "\n",
                "# Calculate basic statistics using NumPy\n",
                "gdp_variance = np.var(gdp_arr)\n",
                "unemp_variance = np.var(unemp_arr)\n",
                "gdp_std = np.std(gdp_arr)\n",
                "unemp_std = np.std(unemp_arr)\n",
                "\n",
                "print(f\"GDP Growth - Variance: {gdp_variance:.2f}, Standard Deviation: {gdp_std:.2f}\")\n",
                "print(f\"Unemployment - Variance: {unemp_variance:.2f}, Standard Deviation: {unemp_std:.2f}\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Array reshaping and operations\n",
                "# Calculate year-over-year differences (absolute change)\n",
                "gdp_yoy = np.diff(gdp_arr)\n",
                "unemp_yoy = np.diff(unemp_arr)\n",
                "\n",
                "print(f\"Max single-year GDP jump: +{np.max(gdp_yoy):.2f}%\")\n",
                "print(f\"Max single-year GDP drop: {np.min(gdp_yoy):.2f}%\")\n",
                "\n",
                "# Calculate the Correlation Matrix (Okun's Law investigation)\n",
                "# We expect a negative correlation (higher GDP growth -> lower unemployment)\n",
                "correlation = np.corrcoef(gdp_arr, unemp_arr)\n",
                "print(f\"\\nCorrelation Coefficient between GDP Growth and Unemployment: {correlation[0, 1]:.2f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Phase 5: Visualization (20 Marks)\n",
                "We will create 4 clear visualizations to explain the trends and patterns (Line, Scatter, Histogram, Box plot)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 1. Dual-Axis Line Chart (Trends over time)\n",
                "fig, ax1 = plt.subplots(figsize=(12, 6))\n",
                "\n",
                "color = 'tab:blue'\n",
                "ax1.set_xlabel('Year', fontweight='bold')\n",
                "ax1.set_ylabel('GDP Growth (%)', color=color, fontweight='bold')\n",
                "ax1.plot(df['Year'], df['GDP_Growth'], color=color, linewidth=2.5, label='GDP Growth')\n",
                "ax1.tick_params(axis='y', labelcolor=color)\n",
                "ax1.axhline(0, color='black', linewidth=1, linestyle='--')\n",
                "\n",
                "ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis\n",
                "color = 'tab:red'\n",
                "ax2.set_ylabel('Unemployment Rate (%)', color=color, fontweight='bold')\n",
                "ax2.plot(df['Year'], df['Unemployment_Rate'], color=color, linewidth=2.5, linestyle='-.', label='Unemployment')\n",
                "ax2.tick_params(axis='y', labelcolor=color)\n",
                "\n",
                "plt.title('South Africa: GDP Growth vs Unemployment', fontsize=16, fontweight='bold')\n",
                "fig.tight_layout() \n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 2. Scatter Plot (Correlation Visualization)\n",
                "plt.figure(figsize=(10, 6))\n",
                "sns.regplot(x='GDP_Growth', y='Unemployment_Rate', data=df, \n",
                "            scatter_kws={'s': 50, 'alpha': 0.6}, line_kws={'color': 'red', 'linewidth': 2})\n",
                "plt.title('Correlation: GDP Growth vs Unemployment', fontsize=16, fontweight='bold')\n",
                "plt.xlabel('GDP Growth (%)')\n",
                "plt.ylabel('Unemployment Rate (%)')\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 3. Histogram (Distribution of GDP Growth)\n",
                "plt.figure(figsize=(10, 6))\n",
                "sns.histplot(df['GDP_Growth'], bins=15, kde=True, color='purple')\n",
                "plt.title('Distribution of South African GDP Growth Rates', fontsize=16, fontweight='bold')\n",
                "plt.xlabel('GDP Growth (%)')\n",
                "plt.ylabel('Frequency (Years)')\n",
                "plt.axvline(df['GDP_Growth'].mean(), color='orange', linestyle='--', label=f\"Mean: {df['GDP_Growth'].mean():.2f}%\")\n",
                "plt.legend()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 4. Box Plot (Unemployment by Decade)\n",
                "df_box = df.copy()\n",
                "df_box['Decade'] = (df_box['Year'] // 10) * 10\n",
                "df_box['Decade'] = df_box['Decade'].astype(str) + 's'\n",
                "\n",
                "plt.figure(figsize=(10, 6))\n",
                "sns.boxplot(x='Decade', y='Unemployment_Rate', data=df_box, palette='Set2')\n",
                "sns.swarmplot(x='Decade', y='Unemployment_Rate', data=df_box, color=\".25\", alpha=0.6)\n",
                "plt.title('Unemployment Rate Distribution per Decade', fontsize=16, fontweight='bold')\n",
                "plt.xlabel('Decade')\n",
                "plt.ylabel('Unemployment Rate (%)')\n",
                "plt.show()"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
notebook_path = os.path.join(base_dir, 'notebooks', 'Data_Analysis_Visualization.ipynb')

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=4)

print(f"Successfully generated Jupyter Notebook at: {notebook_path}")
