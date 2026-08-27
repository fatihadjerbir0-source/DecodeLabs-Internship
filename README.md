# DecodeLabs Data Analyst Internship

## Overview

This repository contains the work completed during my Data Analyst Internship at DecodeLabs, Batch 2026.

The internship was structured around several practical projects covering different stages of the data analysis process. Starting with raw data, the projects progressed through data cleaning, exploratory data analysis, SQL analysis, and data visualization.

The objective was to build a complete data analysis workflow and gain practical experience using Python, SQL, Excel, and data visualization tools.

## Projects

### Project 1: Data Cleaning

The first project focused on preparing the dataset for analysis.

The original e-commerce dataset contained 1,200 rows and 14 columns. The cleaning process included checking data quality, handling missing values, removing duplicates, standardizing formats, and verifying numerical values.

The main steps included:

- Checking for missing values.
- Handling missing CouponCode values by replacing them with "No Coupon".
- Checking for duplicate records.
- Verifying duplicate OrderID values.
- Standardizing date formats.
- Removing unnecessary spaces from text columns.
- Converting Quantity and UnitPrice to numerical values.
- Verifying and recalculating TotalPrice when necessary.

After cleaning, the final dataset was saved as:

`Cleaned_Dataset.xlsx`

This cleaned dataset was then used in the following projects.

---

### Project 2: Exploratory Data Analysis

The second project focused on exploring and understanding the cleaned dataset.

The analysis included:

- Data understanding.
- Descriptive statistics.
- Distribution analysis.
- Correlation analysis.
- Trend analysis.
- Outlier detection.
- Data visualization.
- Identification of key insights.

Python was used to analyze the dataset and generate visualizations.

The main objective of this project was to better understand the structure of the data and identify important patterns before performing more advanced analysis.

---

### Project 3: SQL Data Analysis

The third project focused on analyzing the cleaned e-commerce data using SQL.

The dataset was loaded into a local SQLite database named:

`ecommerce.db`

A Python script was used to automate the process of loading the Excel dataset into the database and executing SQL queries.

The SQL analysis included:

- SELECT statements.
- WHERE conditions.
- ORDER BY.
- GROUP BY.
- Aggregate functions.
- HAVING conditions.
- Revenue analysis.
- Product analysis.
- Payment method analysis.
- Order status analysis.
- Percentage contribution.
- Temporal trends.

The project included 13 SQL queries designed to answer different business questions.

The query results were displayed and saved for further analysis.

---

### Project 4: Data Visualization

The final project focused on transforming data into clear and meaningful business insights through visualization.

Instead of creating charts only to display numbers, each visualization was designed to answer a specific business question and communicate a clear conclusion.

The project followed three main principles:

- Choosing the appropriate chart based on the business question.
- Keeping the visualizations simple and focused.
- Using action-oriented titles and practical business recommendations.

Four main insights were identified.

#### Revenue Trend

Revenue decreased from 2023 to 2025 when comparing the available January to June periods.

This trend suggests that further analysis is needed to understand what caused the decline and to support future business planning.

#### Average Order Value by Product

Laptop orders had the highest average order value at approximately $1,111.

Phone orders had the lowest average order value at approximately $973.

Laptop orders were worth around 14% more on average than Phone orders.

This suggests that high-value products could be considered for upselling and bundle strategies.

#### Order Status Analysis

Approximately 41% of orders were either cancelled or returned.

This represents an important area for further investigation because cancellations and returns can affect revenue and operational performance.

Possible areas for analysis include customer behavior, product information, delivery processes, and the overall order experience.

#### Average Order Value by Payment Method

Credit Card orders had the highest average order value at approximately $1,128.

On average, Credit Card orders were worth around $126 more than Debit Card orders.

This result could help identify opportunities for testing payment-related strategies at checkout.

---

## Technologies Used

The following tools and technologies were used during the internship:

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- Excel
- OpenPyXL

---

## Repository Structure

```text
DecodeLabs-Internship/
│
├── Project_1_Data_Cleaning/
│   ├── data_cleaning.py
│   ├── Cleaned_Dataset.xlsx
│   └── Data_Cleaning_Report.txt
│
├── Project_2_EDA/
│   ├── eda.py
│   ├── charts/
│   └── eda_report.txt
│
├── Project_3_SQL_Data_Analysis/
│   ├── ecommerce.db
│   ├── queries.sql
│   ├── run_queries.py
│   └── query_results.txt
│
├── Project_4_Data_Visualization/
│   ├── visualizations.py
│   ├── insight_1_revenue_trend.png
│   ├── insight_2_avg_order_value_by_product.png
│   ├── insight_3_order_status.png
│   └── insight_4_avg_order_value_by_payment.png
│
└── README.md
