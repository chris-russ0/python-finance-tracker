import pandas as pd
from datetime import datetime

def add_transaction(transactions, amount, category, transaction_type):
    date = datetime.now().strftime('%Y-%m-%d')
    transactions.append({
        'Date': date,
        'Amount': amount,
        'Category': category,
        'Type': transaction_type
    })

def delete_transaction(transactions, index):
    if 0 <= index < len(transactions):
        transactions.pop(index)

def save_transactions(transactions, filename='transactions.csv'):
    df = pd.DataFrame(transactions)
    df.to_csv(filename, index=False)

def load_transactions(filename='transactions.csv'):
    try:
        return pd.read_csv(filename).to_dict('records')
    except FileNotFoundError:
        return []