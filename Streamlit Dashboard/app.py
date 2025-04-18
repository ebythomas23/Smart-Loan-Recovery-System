import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('/Users/ebythomas/Github_Projects/Smart-Loan-Recovery-System/model/model.pkl')

# Define strategy based on risk score
def assign_recovery_strategy(risk_score):
    if risk_score > 0.75:
        return "Immediate legal notices & aggressive recovery"
    elif 0.50 < risk_score <= 0.75:
        return "Settlement offers & repayment plans"
    else:
        return "Automated reminders & monitoring"

#st.title("Loan Risk Prediction and Recovery Strategy")
st.markdown(
    "<h2 style='text-align: center;'>Loan Recovery Strategy and Risk Prediction</h2>",
    unsafe_allow_html=True
)


st.markdown("Enter borrower details to recommend a recovery approach and assess risk.")

# Input fields
income = st.number_input("Monthly Income ($)", min_value=0, value=50000)
loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=150000)
missed_payments = st.slider("Number of Missed Payments", 0, 15, 2)
loan_tenure = st.slider("Loan Tenure (months)", 6, 60, 36)
interest_rate = st.number_input("Interest Rate (%)", min_value=1.0, max_value=30.0, value=12.0)
collateral_value = st.number_input("Collateral Value ($)", min_value=0, value=100000)
outstanding_amount = st.number_input("Outstanding Loan Amount ($)", min_value=0, value=75000)
emi = st.number_input("Monthly EMI ($)", min_value=0, value=2500)
days_past_due = st.slider("Days Past Due", 0, 90, 10)
age = st.slider("Borrower Age", 18, 80, 35)

# Predict button
if st.button("Predict Risk"):
    # Create input DataFrame
    input_data = pd.DataFrame([{
        'Age': age,
        'Monthly_Income': income,
        'Loan_Amount': loan_amount,
        'Loan_Tenure': loan_tenure,
        'Interest_Rate': interest_rate,
        'Collateral_Value': collateral_value,
        'Outstanding_Loan_Amount': outstanding_amount,
        'Monthly_EMI': emi,
        'Num_Missed_Payments': missed_payments,
        'Days_Past_Due': days_past_due
    }])

    # Predict risk score and flag
    risk_score = model.predict_proba(input_data)[0][1]
    high_risk_flag = int(risk_score > 0.5)
    strategy = assign_recovery_strategy(risk_score)

    st.subheader("Prediction Result")
    st.write(f"**Predicted Risk Score:** {risk_score:.2f}")
    st.write(f"**High Risk:** {'Yes' if high_risk_flag else 'No'}")
    st.write(f"**Recommended Recovery Strategy:** {strategy}")
