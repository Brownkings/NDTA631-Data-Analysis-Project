# NDTA 631 - Data Analysis And Visualization (Group 1)

## Project Overview
This project investigates the relationship between Economic Growth (GDP) and Unemployment in South Africa using data sourced from the World Bank. The analysis explores Okun's Law by combining these two datasets and visualizing the trends and correlations over time.

## Prerequisites
Ensure you have Python installed. You can install the required dependencies using the provided `requirements.txt` file.

## Setup Instructions

1. **Install Dependencies:**
   Navigate to the project root directory and run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Integration:**
   The raw data is stored in the `data/gdp_data` and `data/unemployment_data` directories. To prepare the database, run the setup script:
   ```bash
   python3 scripts/setup_database.py
   ```
   This will create a SQLite database (`economic_data.db`) in the `data/` folder containing the merged and cleaned data.

3. **Data Analysis and Visualization:**
   The primary analysis is contained in a Jupyter Notebook. Launch Jupyter to view and interact with the notebook:
   ```bash
   jupyter notebook notebooks/Data_Analysis_Visualization.ipynb
   ```
   *Alternatively, you can open the notebook directly using your IDE (like VS Code or JupyterLab).*

## Project Structure
- `data/` - Contains the raw World Bank CSV datasets and the generated SQLite database.
- `docs/` - Contains the final project report in DOCX and PDF formats.
- `notebooks/` - Contains the Jupyter Notebook used for the core numerical analysis and visualization.
- `scripts/` - Contains Python scripts used for database setup and data preparation.
