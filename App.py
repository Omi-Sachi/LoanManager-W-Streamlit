import streamlit as st
from TheBankofdad import User



custom_html = """
<div class="banner">
    <iframe src="https://giphy.com/embed/3o751Syb8nQNtUPD7G" 
    width="100%" 
    height="300" 
    style="" 
    frameBorder="0" 
    class="giphy-embed" 
    allowFullScreen>
    </iframe>
</div>
<style>
    .banner {
        width: 100%;
        height: 260px;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .giphy-embed {
        border-radius: 10px;
    }
</style>
"""

# Display the custom HTML
st.components.v1.html(custom_html)

st.title("TheBankofDad ")
st.header(":blue[A loan repayment system]")

# Define import session states

if "user" not in st.session_state:
    st.session_state.user = User("Omi")

lm = st.session_state.user.LoanManager

if "Balance" not in st.session_state:
    st.session_state.Balance = lm.Get_Balance()

# Page layout

st.set_page_config(page_title="BankOfDad",page_icon="🏦")

# Set up the Rules and balance collumns

with st.container():
    colum1, colum2 = st.columns([3, 1])
    with colum1:
        st.subheader("Rules:")
        st.markdown("1. You can either make a partial or full repayment but you cannot pay more then the value of the loan.\n"
                    "2. Pay on time\n"
                    "3. To repay a specific loan use it's index in the loan table.\n")
    with colum2:
        st.subheader("Balance")
        st.header(st.session_state.Balance)


with st.container():
    st.subheader("📢 Loan Alerts")

    overdue = lm.db.get_overdue_loans()
    due_soon = lm.db.get_most_due_loans()

    if not overdue and not due_soon:
        st.success("✅ No upcoming or overdue loans!")
    else:
        # Prepare alert strings
        messages = []
        if overdue:
            messages.append("⚠ Overdue Loans:\n")
            for loan in overdue:
                messages.append(f"Loan ID {loan[0]} _ Amount: £{loan[1]} _ Due: {loan[3]} _ Reason: {loan[4]}\n")
        if due_soon:
            messages.append("\n📅 Most Due Loans:\n")
            from datetime import datetime
            for loan in due_soon:
                repay_date = datetime.strptime(loan[3], "%Y-%m-%d").date()
                days_left = (repay_date - datetime.today().date()).days
                messages.append(f"Loan ID {loan[0]} — Amount: £{loan[1]} — Due in {days_left} days — Reason: {loan[4]}\n")

        all_alerts = "".join(messages)

        st.text_area("Loan Notifications", value=all_alerts, height=300, disabled=True)



