# End-to-End Customer Satisfaction Prediction for Brazilian E-Commerce

## Project Overview

This repository contains an end-to-end data science project focused on predicting customer satisfaction for Olist, a major Brazilian e-commerce platform. The project leverages a large, real-world dataset of approximately 100,000 orders to build a multi-class classification model that predicts customer review scores, which range from 1 (very dissatisfied) to 5 (very satisfied).

The primary goal is to demonstrate the complete machine learning lifecycle, from initial data exploration and feature engineering to model training, hyperparameter tuning, and final deployment as an interactive web application using the Flask framework.

### Business Context

In e-commerce, customer satisfaction is a critical indicator of financial health. Low review scores are a strong predictor of customer churn, while high scores correlate with repeat purchases and increased Customer Lifetime Value (LTV). By proactively identifying orders likely to result in low satisfaction, a business can intervene to mitigate issues, reduce churn, and optimize operations.

## Dataset

The project uses the([https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)), which is publicly available on Kaggle. This rich dataset is distributed across nine separate CSV files, forming a relational schema that includes information on:

  * Orders
  * Customers
  * Products
  * Sellers
  * Payments
  * Order Items
  * Geolocation
  * Customer Reviews (this contains the target variable, `review_score`)

## Project Workflow [WIP]

The project is structured to follow a standard data science workflow:

1.  **Data Unification & Preprocessing:** The nine source CSV files are merged into a single master DataFrame.