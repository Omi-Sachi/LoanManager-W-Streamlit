# BankOfDad: A Loan management system Using streamlit

![Game StartPage](https://raw.githubusercontent.com/Omi-Sachi/Hangman-w-Streamlit/main/images/StartGame.png)

Compared to my hangman project this introduced me to more complex streamlit theme like, encorporating html, embedded giph and much more complex class.
Aswell as that this was one of the firt times i've used sqlite, i have experience writing sql queries for my Alevel computer science but using those queries along side python 
wa something i was not used to.

This project really opened my eyes to what it means to be a software developer, epecially when trying to think of how a user will interact with the system you create.
I like to be open and honest i did find myself during this project especially when it cam to the html and complex streamlit position rerering do documentation or AI models.
I do try and limit the amount of questions i ask AI as i don't want to disempower myelf from coming up with the answer myself but at the same time acknowledge how using AI 
has helped with my learning.

Now that' out of the way heres how the Application work:

Users start of at the main area of the app a dashboard, which displays important information like:
Rules, A running total value of all loans and a notice board, which displays over due and almost due loans.

Users can then navigate via a side bar to the payment area where they can:
Insert a new loan and repay and exsisting loan aswell as view a table containing loan history.


## My biggest challenges

### Persitance loan history:
![Game StartPage](https://raw.githubusercontent.com/Omi-Sachi/Hangman-w-Streamlit/main/images/inputbox.png)

As discused prior streamlit runs your entire Python script from top to bottom every time something in the app’s state changes. A way to combat this is to use a session state which
stores all data in your current session, this is great for a game like the hangman i bulit. but for a loan repayment system the loans must remain even if the tab closes,
something that deson''t occure with session state. so to retain the loan history a moved from pandas which i built the whoel project in to SQlite,

Implementing this was not a big challenge and made me feel confident with using databases i other projects, the only hting i had to wrap my head around is cursor and connection
A connection is  object created when you connect to your database file or server and cursor a object created from your connection to the server allowing you to make querie.


### My usage of HTML

![Game StartPage](https://raw.githubusercontent.com/Omi-Sachi/Hangman-w-Streamlit/main/images/Restartgame.png)
I felt it was important for me to speak about my usage of HTML as this wa my first timecoding with it and it showed me that if i wanted to develop web application, 
this is something i need to focus more time and effort on.
So i've taken the inituitive to start a course on html adn wanted explain someone the HTML that apears in my code to further deepen my learning.

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
The code above is a mixture of html and css used to create a scrollable container that will contain the table of loans.
The html acts as the container, and the css define how we want thin container to act. What causes the contianer to scroll is because of the line overflow-y: auto; 
which creates vertically crolling container. Another thing ot note is that setting the table width and th scrolable dv with to 100% allows the table to fill the container
making it look built in.

### Why deos df have to be turnt to html and markdown have to be used?

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

### Displayling loans using pandas

treamlit inherintly suppots dataframes whne displaying tables, so i solution to turning an database into a table that can be displayed is by using python.

### How to alert board was implemented
![Game StartPage](https://raw.githubusercontent.com/Omi-Sachi/Hangman-w-Streamlit/main/images/Matplotlib_grid.png)

Figuring out how to draw the hangman with the least amount of code was difficult, I was initially going to use conditions ( if statements ) and manually write out
what needs to be drawn for each wrong guess. I knew this would take too long, so instead I implemeted a list of coordinates and used a for loop to iterate through each element in the list up to 
the number of wrong tries. I would then call ax.plot(x, y), which takes tuples.

I was hesitant using this method because I have to redraw all components again with every rerun including if the guesses are wrong, which I feel to be inefficient.
So I plan on updateing my program to include conditionals on when to redraw everything and using session states to keep track of what already drawn.


## Future updates:
### A list of improvements:
1. There are a few function like delete_val and edit_val, whom i haven't encorporated into the webapplication, given the time i allocated to it i could finsih thoe bit by then.
Bu i will complete i and keep updating this system, i have to think alot into how to not over clutter the page with features and input bxes whihc i another reason why i ahven't
implemented it yet.
2. Allow multiple users, thi isn't built into streamlit and is an extenion i could have created a basic pasword system with the sql database but i wanted to do thing properly
understand more about encryption and how to keep password afe before attempting it but  did create a skeleton class called user, to try and simulate the creation of a loanmanager
for each user.

