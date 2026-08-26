# Project 1 - Data Cleaning

## 📌 Project Overview

This project is part of my Data Analytics Internship at DecodeLabs.

The objective of this project was to clean and prepare a raw dataset before performing further analysis.

Data cleaning is an important step in the data analysis process because the quality of the results depends on the quality of the data.

---

## 📊 Dataset

The original dataset contains information about customer orders, including:

- Order ID
- Date
- Customer ID
- Product
- Quantity
- Unit Price
- Shipping Address
- Payment Method
- Order Status
- Tracking Number
- Items in Cart
- Coupon Code
- Referral Source
- Total Price

### Dataset Size

- **Number of rows:** 1,200
- **Number of columns:** 14
- **Period covered:** January 2023 to June 2025

---

## 🎯 Project Objective

The main objective was to clean the raw dataset and create a reliable dataset that could be used for further analysis.

The following data cleaning steps were performed:

1. Checking missing values
2. Detecting duplicate records
3. Checking and standardizing dates
4. Cleaning unnecessary spaces in text columns
5. Checking numerical data
6. Verifying the TotalPrice calculation
7. Exporting the cleaned dataset

---

## 🛠️ Tools and Libraries Used

- Python
- Pandas
- NumPy
- OpenPyXL
- Microsoft Excel

---

## 🔄 Data Cleaning Process

### 1. Checking Missing Values

The dataset was checked for missing values.

The only missing values were found in the **CouponCode** column:

- **309 missing values**
- Approximately **25.8% of the dataset**

These missing values were replaced with:

```text
No Coupon
