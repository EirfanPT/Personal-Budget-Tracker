import streamlit as st
import pandas as pd

# Title
st.title("Personal Budget Tracker")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Section: Add Expense
st.header("Add a New Expense")

with st.form("expense_form"):
    date = st.date_input("Date", value=None)  # ✅ Set to None to make it blank
    item = st.text_input("Expense Item")
    amount = st.text_input("Amount Spent (RM)")

    submit = st.form_submit_button("Add Expense")

    if submit:
        try:
            # Check if date is empty
            if date is None:
                raise ValueError("Date is required")

            amount = float(amount)

            if amount < 0:
                raise ValueError("Negative value")

            # Save expense
            st.session_state.expenses.append({
                "Date": date,
                "Expense Item": item,
                "Amount Spent (RM)": amount
            })

            st.success(f"✅ Expense '{item}' added successfully!")

        except:
            st.error("❌ Error: Please enter a valid date and positive amount!")

# Section: Expense Summary
st.header("Expense Summary")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    st.table(df)

    total = df["Amount Spent (RM)"].sum()
    st.subheader(f"Total Expenses: RM {total:.2f}")
else:
    st.info("No expenses recorded yet.")