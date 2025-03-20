import pandas as pd

def calculate_summary(transactions):
    df = pd.DataFrame(transactions)
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    net_savings = total_income - total_expenses
    return total_income, total_expenses, net_savings