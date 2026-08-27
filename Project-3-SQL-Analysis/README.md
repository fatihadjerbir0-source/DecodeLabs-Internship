# Project 3 – SQL Data Analysis

## DecodeLabs Internship – Batch 2026

## 📌 Project Overview

This project is the third project completed during the **DecodeLabs Internship – Batch 2026**.

The objective of this project is to perform **SQL-based data analysis** on a cleaned e-commerce dataset.

The project demonstrates how to:

- Load a cleaned Excel dataset into a SQLite database
- Create and manage a local SQL database
- Write and execute multiple SQL queries
- Analyze sales, orders, products, payment methods, and customer traffic sources
- Use SQL concepts such as `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`, `COUNT`, `SUM`, `AVG`, and subqueries
- Generate a reusable text report containing all SQL queries and results
- Understand SQL execution order through an **Alias Trap** demonstration

The complete workflow is automated using **Python, Pandas, and SQLite**.

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Import the cleaned e-commerce dataset into a SQLite database.
2. Create a reusable local database named `ecommerce.db`.
3. Execute multiple SQL queries automatically.
4. Analyze business and sales-related information.
5. Practice fundamental and intermediate SQL concepts.
6. Generate a complete report containing the executed queries and their results.
7. Extract meaningful insights from the e-commerce dataset.

---

# 🔄 Project Workflow

The complete data analysis pipeline is:

```text
Cleaned_Dataset.xlsx
        │
        ▼
   run_queries.py
        │
        ▼
   ecommerce.db
        │
        ▼
    queries.sql
        │
        ▼
SQL Data Analysis
        │
        ▼
 query_results.txt
