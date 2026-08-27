# 📊 Project 4 – Data Visualization

## 📌 Overview

This project is part of my **Data Analyst Internship at DecodeLabs (Batch 2026)**.

The goal of this project is not simply to create charts, but to transform data into meaningful insights that can support business decisions.

Using the cleaned e-commerce dataset from the previous projects, I created four visualizations. Each visualization focuses on one key business question and ends with a practical recommendation.

---

##  Project Objectives

The main objectives of this project are:

- Explore the e-commerce data through visualizations.
- Identify important business trends and patterns.
- Communicate insights clearly and simply.
- Use visual storytelling instead of creating charts without context.
- Provide actionable recommendations based on the results.

---

## 📊 Visualization Principles

This project follows three main principles of effective data visualization:

###  The Architect

The type of chart is selected based on the business question.

The visualizations use appropriate chart types and honest axes to make the results easy to understand.

###  The Editor

The charts are designed to remain simple and focused.

This includes:

- Removing unnecessary visual elements.
- Avoiding unnecessary legends.
- Using direct labels.
- Highlighting important information with an accent color.
- Reducing chart clutter.

###  The Storyteller

Each visualization tells a specific story.

Instead of using generic titles such as *"Revenue by Year"*, each chart uses an action-oriented title that communicates the main conclusion.

Each chart also includes a **"So What?"** section with a business recommendation.

---

#  Key Insights

## 1️ Revenue Trend

The analysis compares revenue across the available years using a comparable **January–June period**.

### Results:

- **2023:** $286,502
- **2024:** $257,059
- **2025:** $231,883

The results show a significant decline in revenue from 2023 to 2025.

### Business Recommendation

The company should investigate what changed between 2023 and 2025 before setting future revenue targets.

Possible areas for further investigation include:

- Changes in customer behavior.
- Order volume.
- Product performance.
- Payment methods.
- Order cancellations and returns.

📁 Output:

`insight_1_revenue_trend.png`

---

## 2️ Average Order Value by Product

This visualization compares the average value of orders for different products.

### Key Result:

**Laptop orders have the highest average order value at approximately $1,111.**

The lowest average order value comes from **Phone orders at approximately $973**.

This means Laptop orders are worth approximately **14% more on average than Phone orders**.

### Business Recommendation

High-value products such as Laptops could be featured more prominently in:

- Upselling strategies.
- Product bundles.
- Promotional campaigns.

📁 Output:

`insight_2_avg_order_value_by_product.png`

---

## 3️ Order Status Analysis

The analysis shows the distribution of different order statuses.

### Key Results:

- **Cancelled:** 20.8%
- **Returned:** 20.6%
- **Pending:** 19.8%
- **Shipped:** 19.6%
- **Delivered:** 19.2%

Approximately **41% of orders are either cancelled or returned**.

This represents an important business issue because cancellations and returns can reduce revenue and increase operational costs.

### Business Recommendation

The company should further investigate the reasons behind cancellations and returns.

Potential areas to analyze include:

- The checkout process.
- Product information.
- Customer expectations.
- Delivery and fulfillment processes.

📁 Output:

`insight_3_order_status.png`

---

## 4️ Average Order Value by Payment Method

This visualization compares the average order value for different payment methods.

### Key Results:

| Payment Method | Average Order Value |
|---------------|--------------------|
| Credit Card | $1,128 |
| Gift Card | $1,071 |
| Cash | $1,056 |
| Online | $1,017 |
| Debit Card | $1,002 |

**Credit Card orders have the highest average order value.**

On average, Credit Card orders are worth approximately **$126 more than Debit Card orders**.

### Business Recommendation

The company could test incentives encouraging customers to use Credit Card payments at checkout.

However, this result shows an association between the payment method and order value and does not necessarily prove that using a Credit Card causes customers to spend more.

📁 Output:

`insight_4_avg_order_value_by_payment.png`

---

#  Technologies Used

- Python
- Pandas
- Matplotlib
- Excel

---

# 📂 Project Structure

```text
Project_4_Data_Visualization/
│
├── Cleaned_Dataset.xlsx
├── visualizations.py
│
├── insight_1_revenue_trend.png
├── insight_2_avg_order_value_by_product.png
├── insight_3_order_status.png
└── insight_4_avg_order_value_by_payment.png
