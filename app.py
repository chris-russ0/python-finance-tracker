from flask import Flask, request, render_template, redirect, url_for, flash, session
from transactions import load_transactions, save_transactions, add_transaction, delete_transaction
from analysis import calculate_summary
from visualization import generate_visualizations
from finance_data import get_currency_exchange_rate, get_stock_prices
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Load environment variables
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    transactions = load_transactions()

    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        transaction_type = request.form['type']
        add_transaction(transactions, amount, category, transaction_type)
        save_transactions(transactions)
        flash('Transaction added successfully!')
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/summary')
def summary():
    if 'username' not in session:
        return redirect(url_for('login'))

    transactions = load_transactions()
    total_income, total_expenses, net_savings = calculate_summary(transactions)
    generate_visualizations(transactions)
    return render_template('summary.html', total_income=total_income, total_expenses=total_expenses, net_savings=net_savings)

@app.route('/history')
def history():
    if 'username' not in session:
        return redirect(url_for('login'))

    transactions = load_transactions()
    return render_template('history.html', transactions=transactions)

@app.route('/delete/<int:index>')
def delete(index):
    if 'username' not in session:
        return redirect(url_for('login'))

    transactions = load_transactions()
    delete_transaction(transactions, index)
    save_transactions(transactions)
    flash('Transaction deleted successfully!')
    return redirect(url_for('history'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/finance')
def finance():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Example: Get exchange rate from USD to EUR
    exchange_rate = get_currency_exchange_rate('USD', 'EUR')

    # Example: Get stock prices for multiple symbols
    stock_symbols = ['AAPL', 'GOOGL', 'MSFT']  # Add more symbols as needed
    stock_prices = get_stock_prices(stock_symbols)

    return render_template('finance.html', exchange_rate=exchange_rate, stock_prices=stock_prices)

if __name__ == '__main__':
    app.run(debug=True)