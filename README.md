# Smart Loan Recovery System

A machine learning–based solution designed to help financial institutions recommend efficient, data-driven recovery strategies based on borrower behavior and predicted risk levels.  
This project is intended for internal use by bank recovery officers or loan servicing teams.

---

## Project Summary

Recovering unpaid loans is a critical part of financial operations. This project offers a data-driven tool to support recovery officers in evaluating borrower risk and planning the most suitable recovery action. The system combines borrower segmentation, supervised risk classification, and strategy recommendations into one cohesive pipeline, accessible through a Streamlit dashboard.

---

## Problem Statement

Manual recovery planning often lacks consistency and data support, leading to suboptimal decisions and resource usage. Financial institutions need a reliable way to:
- Identify borrowers with high default risk
- Personalise recovery strategies based on data
- Reduce manual workload and improve overall loan recovery efficiency

---

## Solution Overview

This project uses machine learning to classify borrowers into high- and low-risk groups and then assigns appropriate recovery strategies. The approach combines:
- Exploratory Data Analysis (EDA)
- K-Means clustering for borrower segmentation
- Random Forest classification model for risk prediction
- Rule-based logic to recommend targeted recovery actions

A Streamlit dashboard allows internal users to input borrower details and receive strategy recommendations supported by predicted risk scores.

---
### Dashboard Preview

The internal dashboard allows recovery officers to enter borrower details and receive recommended recovery strategy along with areal-time risk predictions.

#### 📸 Screenshot

![Dashboard Screenshot](assets/dashboard_screenshot.png)

---

#### 🎥 Quick Demo

Below is a short demo showing how the app works from input to output.

![Dashboard Demo](assets/dashboard_demo.gif)


## How It Works

### 1. Data Analysis and Preprocessing
- Cleaned and explored borrower features such as income, loan amount, missed payments, and repayment history.
- Verified data quality with no missing values.

### 2. Borrower Segmentation
- Applied K-Means clustering to group borrowers based on financial behavior.
- Interpreted and labeled each segment for clarity.

### 3. Risk Flagging
- Defined high-risk segments based on observed patterns.
- Created a binary `High_Risk_Flag` to train the classification model.

### 4. Model Training
- Used `RandomForestClassifier` to train a model on selected features.
- Achieved:
  - 98% training accuracy
  - 93% test accuracy

### 5. Strategy Generation
- Applied rule-based thresholds to risk scores to assign one of three recovery strategies:
  - Immediate legal action
  - Settlement offers or repayment plans
  - Automated follow-ups and monitoring

### 6. Dashboard Deployment
- Built a Streamlit interface for internal users.
- Allows manual data entry to generate predictions and strategy recommendations.

---

## Project Files

Intended Users
--------------

This project is designed **for internal use by banks or financial institutions**, specifically:

*   Loan recovery officers  
*   Risk analysts   
*   Collection strategy teams
    
It is **not intended for public or customer-facing use**.

Author
------

**Eby Thomas**Master of Data Science, University of Melbourne