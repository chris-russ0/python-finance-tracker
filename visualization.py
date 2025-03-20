import pandas as pd
import matplotlib.pyplot as plt

def generate_visualizations(transactions):
    df = pd.DataFrame(transactions)

    # Pie chart for category distribution
    category_distribution = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    category_distribution.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Expenses by Category')
    plt.ylabel('')
    plt.savefig('static/category_distribution.png')
    plt.close()

    # Line chart for income and expenses over time
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.groupby([df.index.to_period('M'), 'Type'])['Amount'].sum().unstack().plot(kind='line')
    plt.title('Income and Expenses Over Time')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.savefig('static/income_expenses_trend.png')
    plt.close()