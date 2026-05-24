from database import execute_query, fetch_query

def add_expense(title, amount, category, date):
    execute_query(
        "INSERT INTO expenses(title,amount,category,date) VALUES(?,?,?,?)",
        (title, amount, category, date)
    )

def get_expenses():
    return fetch_query("SELECT * FROM expenses")
