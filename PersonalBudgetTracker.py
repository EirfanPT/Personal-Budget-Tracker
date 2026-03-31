import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Expense Tracker", page_icon="📊")

# Title
st.markdown("## 📊 Daily Expense Tracker")
st.write("Keep track of your daily spending easily!")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# --- INPUT SECTION ---
st.markdown("### ➕ Enter Expense Details")

col1, col2 = st.columns(2)

with col1:
    date = st.date_input("Select Date", value=None)

with col2:
    item = st.text_input("Expense Name")

amount = st.text_input("Amount (RM)")

# Submit button outside form (different style)
if st.button("Save Expense"):
    try:
        if date is None or item.strip() == "":
            raise ValueError

        amount = float(amount)

        if amount < 0:
            raise ValueError

        # Store data
        st.session_state.expenses.append({
            "Date": date,
            "Item": item,
            "Amount (RM)": amount
        })

        st.success(f"Added: {item} (RM {amount:.2f})")

    except:
        st.warning("⚠ Please enter valid data (non-empty item, valid date, positive number).")

# --- DISPLAY SECTION ---
st.markdown("---")
st.markdown("### 📋 Recorded Expenses")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    # Display dataframe instead of table (more interactive)
    st.dataframe(df, use_container_width=True)

    # Total calculation
    total = df["Amount (RM)"].sum()

    st.markdown(f"### 💵 Total Spending: RM {total:.2f}")

else:
    st.info("No data yet. Start adding your expenses!")