## 📊 Customer Churn Prediction

A **Streamlit web app** that predicts whether a customer is likely to churn based on their details, using a machine learning model trained on the **Telco Customer Churn dataset**.  
The app also suggests **retention strategies** for customers predicted to churn.


## 🚀 Features
-  **Churn Prediction** – Predicts if a customer is likely to leave.  
-  **Retention Strategies** – Provides personalized suggestions to reduce churn.  
-  **Interactive Streamlit UI** – Easy-to-use sidebar for input.  
-  **Input Summary Tables** – Displays customer details in structured tables.  
-  **Pre-trained Model** – Uses a pickled machine learning model (`customer_churn_model.pkl`) and encoders.  


## 📂 Project Structure
```bash

├── .devcontainer/
├── app.py                     # Main Streamlit app
├── customer\_churn\_model.pkl   # Trained ML model
├── encoders.pkl               # Encoders for categorical variables
├── requirements.txt           # Dependencies
├── WA\_Fn-UseC\_-Telco-Customer-Churn.csv # Dataset
└── README.md                  # Documentation

```

## 🛠 How to Run the App Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/customer-churn-prediction.git
   cd customer-churn-prediction
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

## 📌 Example Retention Strategies

If a customer is predicted to churn, the app suggests strategies like:

*  Offer discounts or bundle services for high monthly charges
*  Promote long-term contracts with benefits
*  Provide free or discounted Tech Support trial
*  Give free Online Security for a limited time
*  Assign dedicated support for senior citizens with low tenure

## 🎯 Use Cases

* Telecom companies to identify at-risk customers
* Business analysts to understand churn patterns
* Customer success teams to design retention campaigns

## 📜 License

This project is licensed under the MIT License.

```
