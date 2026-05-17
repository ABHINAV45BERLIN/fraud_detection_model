import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection Model")   

st.markdown("Please enter the details of the transaction to predict if it is fraudulent or not.")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT","TRANSFER","CASH_OUT"])

amount = st.number_input("Amount", min_value = 0.0, value= 1000.0)

oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value = 0.0, value=0.0)

newbalanceOrig = st.number_input("New Balance (Sender)", min_value= 0.0, value=0.0)

oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)

newbalanceDest = st.number_input("New Balance (Receiver)", min_value= 0.0, value=0.0)


if st.button("Predict"):

    input_data = pd.DataFrame([{
        "type" : transaction_type,
        "amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg,
        "newbalanceOrig" : newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest" : newbalanceDest
    }])
    prediction = model.predict(input_data)
    st.write(f"Prediction: {'Fraudulent' if prediction[0] == 1 else 'Not Fraudulent'}")