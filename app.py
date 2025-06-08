import streamlit as st
from chat_local_llm import chat_with_llm
from goal_forecasting import forecast_goals
from generate_pdf import create_pdf
from risk_profiler import predict_risk

st.title("💰 AI Financial Advisor")

option = st.sidebar.selectbox("Choose Service", [
    "Chat", "Goal Forecasting", "PDF Report", "Risk Profiling", "Custom Financial Plan"
])

if option == "Chat":
    user_input = st.text_input("Ask anything:")
    if user_input:
        st.write(chat_with_llm(user_input))

elif option == "Goal Forecasting":
    st.write(forecast_goals())

elif option == "PDF Report":
    if st.button("Generate Report"):
        create_pdf()
        st.success("PDF created successfully.")

elif option == "Risk Profiling":
    st.write(f"Risk Level: {predict_risk()}")

elif option == "Custom Financial Plan":
    st.subheader("Enter your details")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    income = st.number_input("Monthly Income", min_value=0)
    expenses = st.number_input("Monthly Expenses", min_value=0)
    savings_goal = st.number_input("Savings Goal", min_value=0)

    if st.button("Calculate Plan"):
        from custom_financial_model import calculate_financial_plan
        result = calculate_financial_plan(age, income, expenses, savings_goal)
        st.write(result)