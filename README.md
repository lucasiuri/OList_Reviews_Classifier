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

## Project Workflow

The project is structured to follow a standard data science workflow:

1.  **Data Unification & Preprocessing:** The nine source CSV files are merged into a single master DataFrame. Data cleaning is performed, including handling missing values and correcting data types.
2.  **Exploratory Data Analysis (EDA):** In-depth analysis is conducted to understand the distribution of the target variable (`review_score`), identify geographical and temporal patterns in sales, and explore relationships between features. A key finding is the significant class imbalance, with a majority of reviews being 5-star ratings.
3.  **Feature Engineering:** New, meaningful features are created to quantify the customer experience. This is a critical step and includes engineering time-based features (e.g., `delivery_delta`, `processing_time`) and seller reputation metrics (e.g., `seller_avg_review_score`, `seller_order_count`).
4.  **Model Training & Tuning:** Several classification models are trained and compared, including a Logistic Regression baseline, Random Forest, and a final XGBoost model. Hyperparameter tuning is performed systematically using `GridSearchCV` with a `f1_macro` scoring metric to account for class imbalance.
5.  **Model Evaluation:** The final model's performance is rigorously assessed on a held-out test set using a confusion matrix and metrics like precision, recall, and F1-score, with a focus on macro-averaging to ensure performance across all classes is considered.
6.  **Model Deployment:** The complete preprocessing and modeling pipeline is serialized using `joblib`. A web application is built with Flask to serve the model, featuring a simple HTML frontend for user input and a backend to process requests and return predictions.



## Technologies Used

  * **Programming Language:** Python
  * **Data Manipulation:** Pandas, NumPy
  * **Data Visualization:** Matplotlib, Seaborn
  * **Machine Learning:** Scikit-learn, XGBoost
  * **Model Persistence:** Joblib
  * **Web Framework:** Flask

## How to Run the Application

To run the prediction web application on your local machine, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/<your-username>/customer-satisfaction-prediction.git
    cd customer-satisfaction-prediction
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**

    ```bash
    flask run
    ```

    Alternatively, you can run `python app.py`.

5.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000`. You will see a form where you can input order details to get a predicted satisfaction score.

## Future Improvements

  * **Containerization:** Package the application using Docker for easier deployment and scalability.
  * **Cloud Deployment:** Deploy the containerized application to a cloud service like AWS, Google Cloud, or Heroku.
  * **CI/CD Pipeline:** Implement a CI/CD pipeline to automate testing and deployment.
  * **Model Monitoring:** Set up a system to monitor the model's performance in production and trigger retraining when necessary.