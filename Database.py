import sqlite3
from datetime import date


class DatabaseCommands:

    def __init__(self, db_path="loan_history.db"):
        self.conn = sqlite3.connect(db_path,check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS loan_history (
                                loan_id INTEGER PRIMARY KEY,
                                Amount INTEGER,
                                Date DATE,
                                Repay_Date DATE,
                                Loan_Reason TEXT
                            )''')
            self.conn.commit()
        except Exception as e:
            print(e)


    def insert_loan(self, amount, date, repay_date, loan_reason):
        try:
            query = "INSERT INTO loan_history (Amount, Date, Repay_Date, Loan_Reason) VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (amount, date, repay_date, loan_reason))
            self.conn.commit()
            print("Insert successful, lastrowid =", self.cursor.lastrowid)
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print("Insert error:", e)
            return None




    def edit_value(self,loan_id, field, value):
        try:
            #Check if the field exsists.
            if field not in ("Amount", "Date", "Repay_Date", "Loan_Reason"):
                raise ValueError(f"Invalid field name: {field}")
        # Query to update a table.
            query = f"UPDATE loan_history SET {field} = ? WHERE loan_id = ?"
            self.cursor.execute(query, (value, loan_id))
            if self.cursor.rowcount == 0:
                return None  # loan_id not found
            self.conn.commit()
            return True
        except (sqlite3.Error, ValueError) as e:
            print("Update error:", e)
            return None

    def get_value(self,variable, loan_id):
        try:
            if variable not in ("loan_id", "Amount", "Date", "Repay_Date", "Loan_Reason"):
                raise ValueError(f"Invalid column name: {variable}")

            query = f"SELECT {variable} FROM loan_history WHERE loan_id = ?"
            self.cursor.execute(query, (loan_id,))
            result = self.cursor.fetchone()
            return result[0] if result else False
        except (sqlite3.Error, ValueError) as e:
            print("SQLite error:", e)
            return None


    def get_balance(self):
        try:
            query = "SELECT SUM(Amount) FROM loan_history"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result[0] if result and result[0] is not None else 0
        except sqlite3.Error as e:
            print("Balance retrieval error:", e)
            return 0

    def delete_val(self,loan_id):
        try:
            query = "DELETE FROM loan_history WHERE loan_id = ?"
            self.cursor.execute(query, (loan_id,))
            self.conn.commit()
            if self.cursor.rowcount == 0:
                return None  # loan_id not found
            return True
        except sqlite3.Error as e:
            print("Delete error:", e)
            return None

    def get_all_loans(self):
        try:
            query = "SELECT loan_id, Amount, Date, Repay_Date, Loan_Reason FROM loan_history"
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            return results
        except sqlite3.Error as e:
            print("Fetch all loans error:", e)
            return []


    def update_loan_multiple_fields(self,loan_id, updates: dict):
       
        try:
            allowed_fields = {"Amount", "Date", "Repay_Date", "Loan_Reason"}
            set_clauses = []
            params = []

            for field, value in updates.items():
                if field not in allowed_fields:
                    raise ValueError(f"Invalid field: {field}")
                set_clauses.append(f"{field} = ?")
                params.append(value)

            if not set_clauses:
                print("No fields to update.")
                return False

            params.append(loan_id)
            query = f"UPDATE loan_history SET {', '.join(set_clauses)} WHERE loan_id = ?"
            self.cursor.execute(query, tuple(params))

            if self.cursor.rowcount == 0:
                return None  # loan_id not found
            self.conn.commit()
            return True
        except (sqlite3.Error, ValueError) as e:
            print("Update multiple fields error:", e)
            return None

    def get_overdue_loans(self):
        query = "SELECT * FROM loan_history WHERE Repay_Date < ?"
        self.cursor.execute(query, (date.today().isoformat(),))
        return self.cursor.fetchall()

    def get_most_due_loans(self, limit=5):
        query = "SELECT * FROM loan_history WHERE Repay_Date >= ? ORDER BY Repay_Date ASC LIMIT ?"
        self.cursor.execute(query, (date.today().isoformat(), limit))
        return self.cursor.fetchall()

