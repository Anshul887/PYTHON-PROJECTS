import pandas as pd
import matplotlib.pyplot as plt
from expense import get_expenses

def generate_chart():
    data = get_expenses()

    if not data:
        print("No expenses found")
        return

    df = pd.DataFrame(
        data,
        columns=["ID", "Title", "Amount", "Category", "Date"]
    )

    category_sum = df.groupby("Category")["Amount"].sum()

    category_sum.plot(
        kind="pie",
        autopct="%1.1f%%",
        figsize=(6,6)
    )

    plt.title("Expense Distribution")
    plt.ylabel("")

    plt.savefig("charts/expense_chart.png")
    plt.show()
