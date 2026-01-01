# 📈 REAL-TIME DYNAMIC PRICING ANALYTICS

## 🧠 Project Summary
This project designs and implements an **end-to-end data analytics solution** to evaluate the effectiveness of **dynamic pricing strategies** in an e-commerce environment.

Using transactional, customer, and time-based data, the project measures **revenue uplift** when prices are dynamically adjusted during peak hours and for high-rated products.

The solution combines **Python for data processing and business logic** with **Power BI for interactive dashboards and insights**.

> ⚠️ Note: This project **simulates real-time pricing decisions using historical data and time-based logic**.

---

## 👥 Target Roles
This project is relevant for:
- Data Analyst
- Business Analyst
- Revenue / Pricing Analyst
- Junior Analytics Engineer

---

## 🎯 Business Problem
E-commerce platforms often rely on **static pricing**, which fails to adapt to:
- Peak demand hours
- Customer satisfaction signals (ratings and reviews)
- Regional purchasing behavior

### Core Business Question
**Does applying dynamic pricing increase overall revenue without negatively impacting customer behavior?**

---

## ❓ Key Business Questions Answered
- Does dynamic pricing increase total revenue?
- How much revenue uplift is generated compared to static pricing?
- During which **hours** does dynamic pricing perform best?
- Which **regions/states** generate the highest uplift?
- How do **product ratings** impact pricing effectiveness?
- What customer segments benefit most from dynamic pricing?

---

## 🧩 Dataset Description
The project uses a **relational e-commerce dataset** containing:
- Orders and order timestamps
- Order items (price and freight cost)
- Customers and geographic information
- Products and categories
- Payments and reviews (optional)

> ⚠️ Raw and cleaned datasets are excluded from GitHub due to size and data governance best practices.

---

## 🏗️ Project Structure
REAL_TIME_DYNAMIC_PRICING_ANALYTICS/
│
├── raw_data/ # Raw datasets (ignored in Git)
├── cleaned_data/ # Processed datasets (ignored in Git)
├── scripts/ # Python scripts
│ ├── clean_data.py
│ ├── feature_engineering.py
│ ├── merge_data.py
│ └── dynamic_pricing.py
│
├── powerbi/ # Power BI dashboards (.pbix ignored)
├── documentation/
│ └── dashboard.png # Dashboard preview
│
├── .gitignore
└── README.md


---

## ⚙️ Technologies Used
- **Python** (pandas, numpy)
- **Power BI** (DAX, KPI cards, maps, slicers)
- **Git & GitHub**
- **Windows / Spyder / VS Code**

---

## 🔄 Project Workflow
1. **Data Cleaning**
   - Removed duplicates
   - Handled invalid prices and timestamps
   - Ensured data consistency

2. **Feature Engineering**
   - Extracted order hour, day, and month
   - Calculated revenue metrics
   - Categorized customer ratings (High / Medium / Low)

3. **Dynamic Pricing Logic**
   - Increased prices during peak hours (18:00–22:00)
   - Applied premium pricing for high-rated products
   - Computed dynamic revenue and uplift

4. **Data Modeling**
   - Created a single analytics-ready dataset
   - Exported data for Power BI consumption

5. **Visualization & Analysis**
   - Built KPI dashboards
   - Analyzed trends, geography, and customer impact

---

## 🧮 Dynamic Pricing Logic (Simplified)
- **Peak hours:** +15% price adjustment
- **High-rated products:** +5% premium
- **Revenue uplift formula:**
Revenue Uplift % = (Dynamic Revenue − Static Revenue) / Static Revenue


---

## 📊 Power BI Dashboard
The Power BI dashboard provides:
- **KPI Cards**
- Total Revenue
- Total Dynamic Revenue
- Revenue Uplift %
- **Trend Analysis**
- Revenue by hour and month
- **Geographic Insights**
- Revenue uplift by customer state
- **Interactive Filters**
- Rating category
- Time period

### Dashboard Preview
![Dynamic Pricing Dashboard](documentation/dashboard.png)

---

## 📌 Key Results
- Dynamic pricing resulted in **measurable revenue uplift**
- Peak evening hours (18:00–22:00) generated the **highest revenue gains**
- High-rated products benefited most from premium pricing
- Certain regions showed stronger responsiveness to dynamic pricing
- Revenue increased **without increasing order volume**

---

## 📈 Key Insights & Outcomes
- Time-based pricing significantly improves revenue performance
- Customer satisfaction signals can be safely leveraged for pricing
- Geographic segmentation reveals uneven pricing sensitivity
- Dynamic pricing can be applied as a **scalable business strategy**

---

## 🧠 Skills Demonstrated
- Data cleaning & preprocessing
- Feature engineering
- Business logic implementation
- Revenue impact analysis
- Power BI dashboard design
- KPI & metric development
- Analytical storytelling
- Git version control

---

## 💼 Resume-Ready Project Description
> **Real-Time Dynamic Pricing Analytics**  
> Designed and implemented an end-to-end analytics solution using Python and Power BI to evaluate revenue uplift from dynamic pricing strategies. Built feature engineering pipelines, pricing logic, and KPI dashboards to quantify business impact.

---

## 🚀 Future Enhancements
- Machine learning-based price optimization
- Demand forecasting models
- A/B testing simulations
- Real-time data streaming integration

---

## 👤 Author
**Satyam**  
Aspiring Data Analyst | Python | Power BI | SQL | Business Analytics

---

## ⭐ Acknowledgement
If you found this project useful, please ⭐ the repository.
