from tkinter import *
from tkinter import messagebox
from auth import register, login
from expense import add_expense, get_expenses
from analytics import generate_chart
import csv

root = Tk()
root.title("Smart Expense Tracker")
root.geometry("600x600")

# ---------- LOGIN SECTION ----------

Label(root, text="Username").pack()
username_entry = Entry(root)
username_entry.pack()

Label(root, text="Password").pack()
password_entry = Entry(root, show="*")
password_entry.pack()

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if register(username, password):
        messagebox.showinfo("Success", "Registration Successful")
    else:
        messagebox.showerror("Error", "User already exists")

def login_user():
    username = username_entry.get()
    password = password_entry.get()

    if login(username, password):
        messagebox.showinfo("Success", "Login Successful")
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

Button(root, text="Register", command=register_user).pack(pady=5)
Button(root, text="Login", command=login_user).pack(pady=5)

# ---------- DASHBOARD ----------

def open_dashboard():

    dashboard = Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("600x600")

    Label(dashboard, text="Expense Title").pack()
    title_entry = Entry(dashboard)
    title_entry.pack()

    Label(dashboard, text="Amount").pack()
    amount_entry = Entry(dashboard)
    amount_entry.pack()

    Label(dashboard, text="Category").pack()
    category_entry = Entry(dashboard)
    category_entry.pack()

    Label(dashboard, text="Date").pack()
    date_entry = Entry(dashboard)
    date_entry.pack()

    def save_expense():
        add_expense(
            title_entry.get(),
            float(amount_entry.get()),
            category_entry.get(),
            date_entry.get()
        )

        messagebox.showinfo("Success", "Expense Added")

    Button(
        dashboard,
        text="Add Expense",
        command=save_expense
    ).pack(pady=10)

    def show_expenses():
        expenses = get_expenses()

        expense_window = Toplevel(dashboard)
        expense_window.title("All Expenses")

        for exp in expenses:
            Label(
                expense_window,
                text=str(exp)
            ).pack()

    Button(
        dashboard,
        text="View Expenses",
        command=show_expenses
    ).pack(pady=10)

    Button(
        dashboard,
        text="Generate Analytics",
        command=generate_chart
    ).pack(pady=10)

    def export_csv():
        expenses = get_expenses()

        with open(
            "exports/reports.csv",
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                ["ID", "Title", "Amount", "Category", "Date"]
            )

            writer.writerows(expenses)

        messagebox.showinfo(
            "Exported",
            "CSV Report Exported"
        )

    Button(
        dashboard,
        text="Export CSV",
        command=export_csv
    ).pack(pady=10)

root.mainloop()
