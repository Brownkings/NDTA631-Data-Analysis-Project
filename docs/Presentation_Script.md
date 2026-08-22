# NDTA 631 - Project Presentation Script

**Project Title:** Analyzing the Relationship Between GDP Growth and Unemployment in South Africa  
**Target Duration:** 3–5 Minutes  
**Presentation Mode:** Image / Screenshot Presentation (`presentation_visuals/`)

---

## 🎬 Part 1: Introduction
**Speaker 1 (Brown)**  
📷 **Show Screenshot:** `presentation_visuals/01_Title_Page.png`

> "Hi everyone, we're Group 1. I'm Brown, and my group members are Rethabile, Thapelo, and Mpendulo. 
> 
> For our NDTA 631 project, we decided to look into how economic growth affects unemployment in South Africa. We really wanted to see if 'Okun's Law'—which basically says that when the economy grows, unemployment should go down—actually holds up here in SA. 
> 
> To figure this out, we got our datasets straight from the World Bank, specifically looking at annual GDP growth and the total unemployment rate over the years."

---

## 🎬 Part 2: Data Preparation & Database Integration
**Speaker 2 (Rethabile)**  
📷 **Show Screenshot 1:** `presentation_visuals/02_Setup_Database_Code.png` *(Python script)*  
📷 **Show Screenshot 2:** `presentation_visuals/03_CRUD_Terminal_Output.png` *(SQLite CRUD operations)*

> "When we downloaded the raw World Bank data, it was pretty messy and had a lot of extra formatting we didn't need. 
> 
> I set up a Python script using Pandas to read the CSV files, drop all that extra stuff, and organize it properly by year. Since there were some missing numbers in the older data, we used linear interpolation to fill in the gaps so we wouldn't lose those years. 
> 
> After cleaning it up, we used Python to create a SQLite database called `economic_data.db`. We made sure it could handle Create, Read, Update, and Delete operations to meet the rubric requirements, and then we pulled that clean data back into Pandas so we could analyze it."

---

## 🎬 Part 3: Numerical Analysis
**Speaker 3 (Thapelo)**  
📷 **Show Screenshot:** `presentation_visuals/04_Jupyter_Notebook.png`

> "Once the database was good to go, we moved on to the numerical analysis using NumPy. 
> 
> We turned our Pandas data into NumPy arrays to calculate things like variance and standard deviation. What we found was that South Africa's GDP bounces around a lot—it’s pretty volatile. But unemployment doesn’t bounce around; it just keeps steadily creeping up, even when the economy has a good year. 
> 
> We also calculated the correlation coefficient. Under Okun's Law, we’d expect a strong negative number there, but our stats showed that connection is getting weaker, which really points to what economists call 'jobless growth'."

---

## 🎬 Part 4: Visualizations & Conclusion
**Speaker 4 (Mpendulo)**  
📷 **Show Screenshots in Order:**
1. `presentation_visuals/05_Line_Chart.png` *(GDP vs Unemployment Trend)*
2. `presentation_visuals/06_Scatter_Plot.png` *(Correlation Analysis)*
3. `presentation_visuals/07_Histogram.png` *(Distribution of Growth)*
4. `presentation_visuals/08_Box_Plot.png` *(Decade Structural Shift)*

> "To actually visualize what Thapelo just explained, we built four charts using Matplotlib and Seaborn. 
> 
> Our line chart really highlights the problem—you can see unemployment rising over time even when the GDP line spikes up. Our scatter plot also backs up how weak that correlation is. But the most revealing one was our box plot. When we grouped the data by decade, you can clearly see the baseline unemployment rate just getting higher and higher since the 90s. 
> 
> So, our final conclusion is that just growing the economy isn't enough anymore to fix unemployment in South Africa—it's a deep structural problem. 
> 
> Thanks for listening, and you can check out all our code on our GitHub repo."
