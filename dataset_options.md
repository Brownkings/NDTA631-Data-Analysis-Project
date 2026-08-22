# South Africa Dataset Options & Pairings (World Bank Open Data)

Based on the assignment rubric, we need datasets that are robust enough for data cleaning, NumPy array operations, varied visualizations, and database integration. The best datasets are those with many years of historical data to show trends and those that have occasional missing values to allow us to score points in the "Data Preparation" section.

Here are the top ranked dataset pairings for South Africa from the World Bank Open Data platform, ranked by how likely they are to produce maximum marks across the rubric.

## 🏆 Rank 1: The Economic Engine - GDP Growth vs. Unemployment
This is the safest and most robust pair for achieving 100%.

*   **Dataset 1:** GDP growth (annual %)
    *   **URL:** [https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=ZA](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=ZA)
    *   **Description:** Annual percentage growth rate of GDP.
*   **Dataset 2:** Unemployment, total (% of total labor force)
    *   **URL:** [https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=ZA](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=ZA)
    *   **Description:** The share of the labor force that is without work but available for and seeking employment.
*   **Rubric Alignment:** 
    *   **NumPy Analysis (20 marks):** Excellent for calculating correlations, standard deviations, and year-over-year variance.
    *   **Visualization (20 marks):** Perfect for dual-axis line charts, scatter plots to show the inverse relationship (Okun's Law), and histograms of growth distribution.
    *   **Database Integration (20 marks):** Easy to structure in a relational database mapping years to both metrics.

## 🥈 Rank 2: Social Investment - Healthcare Expenditure vs. Life Expectancy
A highly compelling social narrative that works perfectly for a cohesive report.

*   **Dataset 1:** Current health expenditure (% of GDP)
    *   **URL:** [https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS?locations=ZA](https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS?locations=ZA)
    *   **Description:** Level of current health expenditure expressed as a percentage of GDP.
*   **Dataset 2:** Life expectancy at birth, total (years)
    *   **URL:** [https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=ZA](https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=ZA)
    *   **Description:** Indicates the number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life.
*   **Rubric Alignment:**
    *   **Data Preparation (15 marks):** Healthcare expenditure data often has slight gaps in historical reporting, giving us the perfect opportunity to demonstrate data imputation (handling missing values).
    *   **Visualization (20 marks):** Great for scatter plots (to show positive correlation) and box plots comparing different decades.

## 🥉 Rank 3: The Youth Crisis - Education Expenditure vs. Youth Unemployment
A highly relevant topic for South Africa that tells a strong story.

*   **Dataset 1:** Government expenditure on education, total (% of GDP)
    *   **URL:** [https://data.worldbank.org/indicator/SE.XPD.TOTL.GD.ZS?locations=ZA](https://data.worldbank.org/indicator/SE.XPD.TOTL.GD.ZS?locations=ZA)
    *   **Description:** General government expenditure on education expressed as a percentage of total GDP.
*   **Dataset 2:** Unemployment, youth total (% of total labor force ages 15-24)
    *   **URL:** [https://data.worldbank.org/indicator/SL.UEM.1524.ZS?locations=ZA](https://data.worldbank.org/indicator/SL.UEM.1524.ZS?locations=ZA)
    *   **Description:** Share of the labor force ages 15-24 without work but available for and seeking employment.
*   **Rubric Alignment:**
    *   **NumPy Analysis (20 marks):** We can use NumPy to calculate ratios and reshape the data to compare youth unemployment against total unemployment (if we bring in a 3rd dataset).
    *   **Report & Demo (10 marks):** Will make for a very strong, actionable report conclusion regarding education policy and job creation.

## 📊 Rank 4: Cost of Living - Inflation vs. Poverty Headcount
A strong economic story, but slightly risky due to potential data scarcity.

*   **Dataset 1:** Inflation, consumer prices (annual %)
    *   **URL:** [https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=ZA](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=ZA)
    *   **Description:** Inflation measured by the consumer price index reflects the annual percentage change in the cost to the average consumer of acquiring a basket of goods and services.
*   **Dataset 2:** Poverty headcount ratio at national poverty lines (% of population)
    *   **URL:** [https://data.worldbank.org/indicator/SI.POV.NAHC?locations=ZA](https://data.worldbank.org/indicator/SI.POV.NAHC?locations=ZA)
    *   **Description:** Percentage of the population living below the national poverty lines.
*   **Rubric Alignment:**
    *   **Risk Warning:** Poverty data is usually gathered via periodic census or surveys and might not have data for *every* single year. This will require heavy data cleaning and interpolation, which is good for the "Data Prep" rubric but might make "NumPy Analysis" more complicated if the arrays have different shapes.
