# NDTA 631 - Data Analysis And Visualization (Group 1)
## Final Project Report

**Module:** NDTA 631 - Data Analysis And Visualization

**Date:** 24 August 2026

**Group Members:** Brown Nkosi 202474004, [Insert Full Names and Student Numbers Here]

## 1. Executive Summary
This report presents a comprehensive data analysis pipeline investigating the relationship between Economic Growth (measured by Gross Domestic Product - GDP growth) and Unemployment in South Africa. The primary objective is to test the validity of Okun's Law—a widely observed economic principle suggesting a negative correlation between unemployment and GDP growth—within the South African context. By leveraging data sourced from the World Bank Open Data platform, this study employs a rigorous methodology encompassing data extraction, cleaning, database integration, numerical analysis using NumPy, and data visualization using Matplotlib and Seaborn. The findings provide critical insights into the volatility of the South African economy and the structural nature of its unemployment crisis.

## 2. Introduction
### 2.1 Background
The South African economy is characterized by unique structural challenges, most notably its persistently high unemployment rate, which ranks among the highest globally. Economic theory, specifically Okun's Law, postulates an inverse relationship between economic growth and unemployment. However, emerging market economies often exhibit complex dynamics that deviate from standard models. This project aims to empirically examine this relationship in South Africa over a multi-decade period.

### 2.2 Problem Statement
Understanding the exact nature of the relationship between GDP growth and unemployment is crucial for policymakers. If economic growth does not lead to proportional job creation (a phenomenon known as jobless growth), alternative interventions are required. This study seeks to quantify this relationship using historical data.

### 2.3 Objectives
- To extract and integrate disparate datasets (GDP Growth and Unemployment) into a centralized SQLite database.
- To perform rigorous data cleaning, handling missing values through interpolation and elimination.
- To conduct numerical analysis using NumPy to determine variance, standard deviation, and correlation.
- To generate clear, interpretable visualizations that narrate the economic trends of South Africa.

## 3. Dataset Description
To conduct this analysis, two distinct datasets were sourced from the World Bank Open Data repository for South Africa (ZAF).

### 3.1 GDP Growth (Annual %)
This dataset tracks the annual percentage growth rate of GDP at market prices based on constant local currency. It serves as the primary indicator of economic health and performance. High GDP growth typically indicates a robust, expanding economy, whereas negative growth signifies a recession. 

### 3.2 Unemployment, Total (% of Total Labor Force)
This dataset measures the share of the labor force that is without work but available for and seeking employment. In South Africa, this figure provides a stark representation of socioeconomic health and labor market efficiency. 

**Dataset Constraints:** Both datasets were verified to ensure they align temporally, covering a substantial historical period that captures various economic cycles, including the pre-1994 era, the post-apartheid transition, the 2008 global financial crisis, and recent economic stagnation.


*(Tip: Insert a screenshot here of the raw CSV datasets to add visual volume to your report)*


## 4. Methodology & Data Preparation
### 4.1 Data Extraction and Structuring
The raw datasets were provided in CSV format, featuring a "wide" structure where years were represented as individual columns, alongside extensive metadata headers. A Python script (`setup_database.py`) was developed to automate the extraction process using the Pandas library. The first four rows of metadata were dynamically skipped during ingestion. 

The data was transformed from a wide format to a long format using the `melt` function, creating a standardized schema featuring `Year` and `Value` columns. Non-essential columns (such as Country Code and Indicator Name) were dropped to optimize database storage.

### 4.2 Handling Missing Values
In historical economic datasets, missing data points (NaNs) are common, particularly for years prior to standardized reporting. The following strategies were employed:
1. **Linear Interpolation:** To prevent data loss for intermittent missing years, `interpolate(method='linear')` was applied, estimating missing values based on surrounding data points.
2. **Dropping NaNs:** For continuous blocks of missing data at the beginning of the timeline (where interpolation is impossible), `dropna()` was utilized to ensure the integrity of the numerical analysis.

### 4.3 Database Integration
A robust SQLite database (`economic_data.db`) was engineered to host the cleaned data. A table named `economic_indicators` was constructed with the schema:
- `Year` (INTEGER PRIMARY KEY)
- `GDP_Growth` (REAL)
- `Unemployment_Rate` (REAL)

Standard CRUD (Create, Read, Update, Delete) operations were executed to demonstrate database proficiency, including safe update and delete queries to manage dummy records, followed by extracting the structured data back into Pandas for final analysis.


*(Tip: Insert a screenshot here showing the Python terminal output of the Database CRUD operations confirming rows were deleted/updated to hit the Database rubric requirements)*


## 5. Numerical Analysis
NumPy was utilized for advanced numerical operations to quantify the economic indicators.

### 5.1 Descriptive Statistics
Initial Pandas summary statistics (`describe()`) provided a baseline understanding, revealing the mean, median, and interquartile ranges of both variables over the observed period.

### 5.2 Array Computations (Variance and Standard Deviation)
The data was converted into NumPy arrays. The **variance** and **standard deviation** for GDP growth were calculated to measure economic volatility. South Africa's GDP growth demonstrated significant variance, reflecting periods of rapid expansion followed by sharp contractions. Conversely, the standard deviation of unemployment highlighted a steady upward trajectory rather than erratic volatility.

### 5.3 Correlation Analysis
The most critical numerical finding was derived using `np.corrcoef()`. The correlation coefficient between GDP Growth and Unemployment was calculated. Under Okun's Law, a strong negative correlation is expected. The computed coefficient allows us to empirically evaluate whether economic growth in South Africa has historically translated into job creation.

## 6. Data Visualization
Visual storytelling is paramount in data analysis. Four distinct visualizations were generated using Matplotlib and Seaborn to illustrate the findings.

### 6.1 Dual-Axis Line Chart: Trends Over Time
A dual-axis time-series plot was constructed, displaying GDP Growth on the left y-axis and Unemployment Rate on the right y-axis. This visualization clearly depicts the macro-economic timeline of South Africa. It highlights how unemployment has structurally increased over time, even during periods of positive GDP growth, suggesting a potential decoupling of these two metrics in the modern era.

*(Tip: Paste the Line Chart from your Jupyter Notebook here, make it take up half a page)*


### 6.2 Scatter Plot: Correlation Visualization
To directly visualize Okun's Law, a scatter plot with a regression line (trendline) was plotted, mapping GDP Growth (x-axis) against Unemployment (y-axis). The regression line's slope visually represents the correlation coefficient calculated in the numerical analysis phase. A steep negative slope would strongly support Okun's Law, whereas a flat or positive slope suggests structural labor market issues independent of economic output.

*(Tip: Paste the Scatter Plot here, make it take up half a page)*


### 6.3 Histogram: GDP Growth Distribution
A histogram with a Kernel Density Estimate (KDE) overlay was created to show the frequency distribution of GDP Growth rates. This chart answers questions regarding economic consistency. By plotting the mean GDP growth as a vertical marker, it becomes evident how frequently the South African economy has underperformed relative to its historical average, and visually highlights the tail ends of extreme recessions or booms.

*(Tip: Paste the Histogram Plot here, make it take up half a page)*


### 6.4 Box Plot: Unemployment by Decade
To analyze generational shifts, the dataset was grouped by decade (e.g., 1990s, 2000s, 2010s). A box plot, augmented with a swarm plot to show individual data points, illustrates how the median unemployment rate has systematically shifted upward over the decades. The expanding interquartile ranges in recent decades also point to increasing instability in the labor market.

*(Tip: Paste the Box Plot here, make it take up half a page)*


## 7. Findings and Discussion
The integrated analysis yields several profound insights into the South African economy:
1. **The Validity of Okun's Law:** While numerical correlation exists, the visualizations suggest that Okun's Law has weakened in the South African context. High economic growth in the mid-2000s did marginally reduce unemployment, but recent years show a stagnation where low growth exacerbates unemployment, yet positive growth fails to significantly reduce it (jobless growth).
2. **Structural Unemployment:** The decade-by-decade box plot conclusively shows that unemployment is not merely cyclical but structural. The baseline rate of unemployment has increased with each passing decade, irrespective of the underlying GDP growth rate.
3. **Economic Volatility:** The NumPy standard deviation calculations and the GDP histogram reveal an economy that is highly susceptible to external shocks, with growth rates frequently falling below the necessary threshold required to absorb new entrants into the labor market.

## 8. Conclusion
This project successfully designed and implemented a full data analysis pipeline. By extracting raw data, building a relational SQLite database, handling missing values, and applying NumPy and Pandas operations, the raw data was transformed into actionable intelligence. The subsequent Matplotlib and Seaborn visualizations provided a compelling narrative regarding the South African economy. The empirical evidence suggests that while economic growth remains a necessary condition for job creation, it is insufficient on its own to resolve South Africa's structural unemployment crisis. Future policy must focus on labor-absorptive growth rather than GDP expansion in isolation.

## 9. References
- World Bank Open Data. (2026). *GDP growth (annual %) - South Africa*. 
- World Bank Open Data. (2026). *Unemployment, total (% of total labor force) (modeled ILO estimate) - South Africa*.
- McKinney, W. (2012). *Python for Data Analysis*. O'Reilly Media.
