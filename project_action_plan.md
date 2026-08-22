# Project Action Plan: GDP Growth vs. Unemployment

Excellent choice! The relationship between Economic Growth (GDP) and Unemployment (often explored through *Okun's Law*) provides a very strong narrative for your project.

Here is a step-by-step action plan to guarantee maximum marks across all rubric sections using these datasets.

## 🛠️ Phase 1: Environment & Data Setup
**Goal:** Get the project foundation ready.
1. **Initialize Git Repository:** Create a new GitHub repo. Set up a basic folder structure:
   - `/data` (for raw and cleaned CSVs)
   - `/notebooks` (for Jupyter Notebook analysis)
   - `/scripts` (for Python files or database scripts)
   - `/docs` (for your final report)
2. **Download Data:** Go to the World Bank links provided in the options file and download the datasets as **CSV** files. Place them in your `/data` folder.
3. **Install Dependencies:** Ensure your environment has `pandas`, `numpy`, `matplotlib`, `seaborn`, and `jupyter` installed.

## 🗄️ Phase 2: Database Integration (20 Marks)
**Goal:** Prove you can build and query a database before doing the deep analysis.
1. **Create SQLite Database:** Write a short Python script using the built-in `sqlite3` library to create a database file (e.g., `zaf_economy.db`).
2. **Design the Schema:** Create a table named `economic_indicators` with columns: `Year`, `GDP_Growth`, and `Unemployment_Rate`.
3. **CRUD Operations:**
   - **Insert:** Read the raw CSVs and insert the merged data into the database.
   - **Update/Delete:** Write a dummy script to safely update a specific year's record or delete an invalid row (take screenshots of this for the report!).
4. **Export to Pandas:** Write a SQL query (`SELECT * FROM economic_indicators`) to pull the data directly from the database into a Pandas DataFrame for the next phases.

## 🧹 Phase 3: Data Preparation (15 Marks)
**Goal:** Clean the data and generate initial insights.
1. **Clean Data:** The World Bank CSVs have several header rows that need skipping. The data is also in a "wide" format (years as columns). You will need to "melt" or transpose the data so that `Year` is a single column.
2. **Handle Missing Values:** South African unemployment data might be missing for some years before 1994. Use Pandas to handle these `NaN` values (e.g., dropping them, or using linear interpolation). **Document this process clearly!**
3. **Descriptive Stats:** Use `df.describe()` to generate summary statistics (mean, median, min, max) for both datasets.

## 🧮 Phase 4: NumPy Numerical Analysis (20 Marks)
**Goal:** Demonstrate array operations and mathematical calculations.
1. **Extract Arrays:** Convert the Pandas columns into NumPy arrays (`np.array()`).
2. **Perform Calculations:**
   - Calculate the **variance** and **standard deviation** of GDP growth to show economic volatility.
   - Calculate the **correlation coefficient** (`np.corrcoef()`) between GDP growth and Unemployment. (Does higher GDP growth mean lower unemployment in SA?)
   - Reshape arrays or calculate year-over-year differences (`np.diff()`) to find the years with the sharpest changes.
3. **Explain Findings:** Write markdown cells in your Jupyter Notebook explaining what these numbers actually mean in real life.

## 📈 Phase 5: Visualization (20 Marks)
**Goal:** Tell the story visually using Matplotlib and Seaborn.
1. **Line Chart:** Create a dual-axis line chart. Plot `Year` on the x-axis, `GDP Growth` on the left y-axis (maybe as a bar chart), and `Unemployment` as a line on the right y-axis.
2. **Scatter Plot:** Plot `GDP Growth` (x-axis) vs `Unemployment` (y-axis). Add a trendline. This directly visualizes the correlation calculated in Phase 4.
3. **Histogram:** Create a histogram of GDP Growth to show the distribution of economic performance (e.g., how many years did SA experience negative growth?).
4. **Box Plot:** Group the years into decades (e.g., 1990s, 2000s, 2010s) and create a box plot showing how the median unemployment rate has shifted over the decades.
5. *Ensure all graphs have clear titles, axis labels, legends, and pleasing colors!*

## 📝 Phase 6: Report & Demo (10 Marks)
**Goal:** Wrap it all up into a professional submission.
1. **Write the Report (7-9 pages):**
   - **Intro:** Explain the datasets and the objective (investigating Okun's Law in SA).
   - **Methodology:** Show snippets of your data cleaning and database integration.
   - **Analysis:** Present the NumPy stats and the 4 visualizations. Explain the "story" the graphs tell.
   - **Conclusion:** Summarize the findings.
2. **Record Demo:** Do a quick 3-5 minute screen recording showing your code running, the database being queried, and the final graphs.

---
**Next Step:** Would you like me to help you initialize the Git repository and set up the folder structure, or do you want to download the CSVs first and have me write the initial Data Preparation/Database script?
