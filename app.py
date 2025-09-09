import streamlit as st
import pandas as pd
import pickle

# --- Load model and encoders ---
with open("customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)
loaded_model = model_data["model"]
feature_names = model_data["features_names"]

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

# --- Retention strategy function ---
def suggest_retention_strategies(customer_row):
    suggestions = []
    if customer_row['MonthlyCharges'] > 80:
        suggestions.append("💰 Offer discount or bundle services to reduce monthly cost.")
    if customer_row['Contract'] == "Month-to-month":
        suggestions.append("📄 Promote longer-term contracts with discounts.")
    if customer_row['TechSupport'] == "No":
        suggestions.append("🛠 Offer free or discounted Tech Support trial.")
    if customer_row['OnlineSecurity'] == "No":
        suggestions.append("🔒 Provide free Online Security for 3 months.")
    if customer_row['SeniorCitizen'] == 1 and customer_row['tenure'] < 12:
        suggestions.append("🤝 Assign a dedicated support representative.")
    if not suggestions:
        suggestions.append("💡 Maintain engagement with regular offers and communication.")
    return suggestions

# --- Streamlit UI ---
st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
st.title("📊 Customer Churn Prediction App")
st.markdown("Predict if a customer is likely to churn and get **retention strategies**.")

# --- Sidebar inputs ---
st.sidebar.header("Customer Details")
input_data = {}
input_data['gender'] = st.sidebar.selectbox("Gender", ["Male", "Female"])
input_data['SeniorCitizen'] = st.sidebar.selectbox("Senior Citizen", [0, 1])
input_data['Partner'] = st.sidebar.selectbox("Partner", ["Yes", "No"])
input_data['Dependents'] = st.sidebar.selectbox("Dependents", ["Yes", "No"])
input_data['tenure'] = st.sidebar.number_input("Tenure (months)", min_value=0, max_value=100, value=1)
input_data['PhoneService'] = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
input_data['MultipleLines'] = st.sidebar.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
input_data['InternetService'] = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
input_data['OnlineSecurity'] = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
input_data['OnlineBackup'] = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
input_data['DeviceProtection'] = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])
input_data['TechSupport'] = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
input_data['StreamingTV'] = st.sidebar.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
input_data['StreamingMovies'] = st.sidebar.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
input_data['Contract'] = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
input_data['PaperlessBilling'] = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
input_data['PaymentMethod'] = st.sidebar.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
input_data['MonthlyCharges'] = st.sidebar.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
input_data['TotalCharges'] = st.sidebar.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=50.0)

# --- Main Section ---
st.subheader("Customer Input Summary")

# Split the input_data into 3 groups for display
keys = list(input_data.keys())
split1 = keys[:7]   # first 7 columns
split2 = keys[7:14] # next 7 columns
split3 = keys[14:]  # remaining columns

df1 = pd.DataFrame([{k: input_data[k] for k in split1}])
df2 = pd.DataFrame([{k: input_data[k] for k in split2}])
df3 = pd.DataFrame([{k: input_data[k] for k in split3}])

# Display stacked vertically
st.table(df1)
st.table(df2)
st.table(df3)

# --- Prediction ---
if st.button("Predict Churn"):
    input_data_df = pd.DataFrame([input_data])

    # Encode categorical variables
    for column, encoder in encoders.items():
        input_data_df[column] = encoder.transform(input_data_df[column])

    prediction = loaded_model.predict(input_data_df)

    st.subheader("🔮 Prediction Result")
    if prediction[0] == 1:
        st.markdown(f"<h3 style='color:red'>Churn ⚠️</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color:green'>No Churn ✅</h3>", unsafe_allow_html=True)


    # Retention strategies
    if prediction[0] == 1:
        with st.expander("💡 Suggested Retention Strategies"):
            strategies = suggest_retention_strategies(input_data)
            for s in strategies:
                st.write("-", s)
    else:
        st.success("Customer is unlikely to churn. Keep up good service!")
