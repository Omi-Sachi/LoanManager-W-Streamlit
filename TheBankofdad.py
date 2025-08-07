import streamlit as st
import pandas as pd
from Database import DatabaseCommands



class User:
    def __init__(self,name):
        self.name = name
        self.LoanManager = LoanManager()

class settings:
    def __init__(self):
        self.Max_Balance = 100

class LoanManager:
    def __init__(self):
        self.Balance = 0
        self.settings = settings()
        self.db = DatabaseCommands()

    def Add_Loan(self, amount, date, repay_date, loan_reason):

        # Insert a new loan to the DB and manage any errors.
        loan_id = self.db.insert_loan(amount, date, repay_date, loan_reason)

        if loan_id is None:
            st.warning('Error insertings loan.', icon="⚠️")
            return None

        # Store the current balance
        self.Balance = self.db.get_balance()

        # Check if the amount loaned is within the set limits.
        if self.Balance > self.settings.Max_Balance:
            st.warning("Warning! You have now overspent, repay Dad back immediately", icon="❌")

        st.success("Loan Added", icon="💷")
        return loan_id

    def Get_Balance(self):

    # Get the current balance
        self.Balance = self.db.get_balance()
        return self.Balance
# do not use
    def export_loan_History(self):
        # Returns list of all loans (list of tuples)
        loans = self.db .get_all_loans()
        if not loans:
            st.warning("No loans found.", icon="⁉️")
        return loans
# do not use
    def delete_loan(self, loan_id):
        success = self.db.delete_val(loan_id)
        if success:
            st.warning(f"Loan {loan_id} deleted.", icon="💷")
        else:
            st.warning(f"Loan {loan_id} does not exist.", icon="❌")

    def repay(self, loan_id, repay_amount):
        current_amount = self.db.get_value("Amount", loan_id)

        if current_amount is False or current_amount is None:
            st.warning("Please try again, that loan ID does not exist.", icon="⁉️")
            return

        if repay_amount < current_amount:
            new_amount = current_amount - repay_amount
            success = self.db.edit_value(loan_id, "Amount", new_amount)
            if success:
                st.warning("Thank you for the partial repayment.", icon="👍")
            else:
                st.warning("Failed to update repayment.", icon="❌")
        elif repay_amount == current_amount:
            success = self.db.delete_val(loan_id)
            if success:
                st.warning("The loan has been successfully repaid.", icon="💷")
            else:
                st.warning("Failed to delete loan after repayment.", icon="❌")
        else:
            st.warning("The amount you've set to repay is greater than the loaned amount. Please enter the correct amount.", icon="❌")

    def display_loans(self):
        # Inject the scroll CSS once
        scroll_style = """
            <style>
            .scrollable-div {
              max-height: 300px;      
              overflow-y: auto;        
              border: 1px solid #ddd; 
              border-radius: 15px;
              padding: 10px;
              width: 100%;           
              box-sizing: border-box;  
            }
            table {
              width: 100%;             
            }
            </style>
            """
        st.markdown(scroll_style, unsafe_allow_html=True)

        # Get loans as list of tuples from DB
        loans = self.db.get_all_loans()
        if not loans:
            st.warning("No loans found.", icon="⁉️")
            return
        # Convert to DataFrame
        df = pd.DataFrame(loans, columns=["Loan ID", "Amount", "Date", "Repay Date", "Loan Reason"])
        # Wrap DataFrame HTML in scrollable div
        df_html = df.to_html(index=False)  # pandas → HTML
        st.markdown(f"<div class='scrollable-div'>{df_html}</div>", unsafe_allow_html=True)

        return df







