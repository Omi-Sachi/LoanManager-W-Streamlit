# BankOfDad: A Loan management system Using streamlit

![BankOfDad:Front](https://raw.githubusercontent.com/Omi-Sachi/LoanManager-W-Streamlit/main/images/Frontpage_1.png)
![BankOfDad:Front](https://raw.githubusercontent.com/Omi-Sachi/LoanManager-W-Streamlit/main/images/Frontpage_2.png)

Compared to my Hangman project, this introduced me to more complex Streamlit themes, like incorporating HTML, embedding media and much more complex OOP classes.

This was also the first time I've used SQLite. I have experience writing SQL queries for my A-level computer science projects, but incorporating queries and Python was something I was not used to.

This project opened my eyes to what it means to be a software developer, especially when trying to think of how a user will interact with the system I created.

I like to be open and honest; I did find myself during this project, especially when it came to the HTML and complex Streamlit positioning, referring to documentation or AI models.

I do try and limit the number of questions I ask AI, as I don't want to disempower myself from coming up with the answer myself, but at the same time acknowledge how using AI has helped with my learning.

Now that's out of the way. Here's how the application works:

Users start off at the main area of the app, a dashboard, which displays important information like:

Rules, A running total value of all loans and a notice board, which displays overdue and almost due loans.
Users can then navigate via a sidebar to the payment area, where they can:
Insert a new loan and repay an existing loan, as well as view a table containing loan history.


## My biggest challenges

### Persistant loan history:
![Scrollable_LoanHistory](https://raw.githubusercontent.com/Omi-Sachi/LoanManager-W-Streamlit/main/images/Loan_DB.png)

As discussed prior, Streamlit runs your entire Python script from top to bottom every time something in the app’s state changes. A way to combat this is to use a session state, which stores all data in your current session; this is great for a game like the hangman I built. But for a loan repayment system, the loans must remain even if the tab closes ~ something that doesn't occur with session state. So to retain the loan history, I moved from pandas, which I built the whole project in, to SQLite.

Implementing this was not a big challenge and made me feel confident with using databases in other projects; the only thing I had to wrap my head around was cursor and connection.

A connection is an object created when you connect to your database file or server, and a cursor is an object created from your connection to the server, allowing you to make queries.


### My usage of HTML

![Repayment_Frontpage](https://raw.githubusercontent.com/Omi-Sachi/LoanManager-W-Streamlit/main/images/LoanZn_FP3628.png)
I felt it was important for me to speak about my usage of HTML, as this was my first time coding with it, and it showed me that if I wanted to develop  web applications, this is something I need to focus more time and effort on.

So I've taken the initiative to start a course on HTML and wanted to explain to someone the HTML that appears in my code to further deepen my learning.

```python
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


```
The code above is a mixture of HTML and CSS used to create a scrollable container that will contain the table of loans.

The HTML acts as the container, and the CSS defines how we want the container to act. What causes the container to scroll is because of the line overflow. -y: auto; 

which creates a vertically scrolling container. Another thing to note is that setting the table width and the scrollable div width to 100% allows the table to fill the container making it look built-in.



```python
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
```
The HTML begins by creating an <div> element with the class = banner, which serves as a container to hold the image. By using the iframe element, which is used to store external media like GIFs, we can place the GIF inside the container. 

CSS then defines styling for the container, removing scrollability, allowing the image to take up 100% of the container, etc.

### Displaying loans using pandas

Streamlit inherently supports dataframes when displaying tables, which makes it a good solution when turning a SQLite, database into a table.

But, to use custom styling like making the container that holds the table scrollable, we must use markdown. This isn't possible, so instead the dataframe is converted into an HTML table.

To do this, we first convert the DataFrame (df) into HTML using df.to_html(), giving us the HTML table. Using this, we render the frame, including the styled HTML it's placed in.



### How the alert board was implemented

![Game StartPage](https://raw.githubusercontent.com/Omi-Sachi/LoanManager-W-Streamlit/main/images/ScrollableAlerts.png)

First, the database is queried to get two sets of loans: those that are overdue and those due within five days. I use Python's datetime module to compare the repayment dates for each loan with the current date.

If the query function returns empty lists, there are no upcoming or overdue loan which the user is notified on. 

If there are loans to display, I loop through the results and format each loan into a readable message using indexing to access specific fields (like loan ID, amount, due date, and reason).

To display it i place the  alerts inside a st.text_area widget so users can scroll through them. 


## Future updates:
### A list of improvements:

1. There are a few functions like delete_val and edit_val that I haven’t incorporated into the web application yet. Given the time I allocated to it, I could'nt finish those parts by the deadline. I will complete them and continue updating the system. I’ve had to think carefully about how to avoid cluttering the page with too many features and input boxes, which is another reason I haven’t implemented them yet.
2. Allowing multiple users: This isn't built into Streamlit by default and would require an extension. I could have created a basic password system using the SQL database, but I wanted to do it properly to understand more about encryption and how to keep passwords safe before attempting it. I did, however, create a skeleton class called User to simulate the creation of a LoanManager instance for each user.

