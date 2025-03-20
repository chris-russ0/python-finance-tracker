# Expense and Income Tracker

This is a simple web application built with Flask to track expenses and incomes. It allows users to add, view, and manage financial transactions, providing insights through visualizations.

## Features

- Add and delete transactions (expenses and incomes).
- Categorize transactions for better organization.
- View transaction history.
- Generate visualizations for financial insights.

## Technologies Used

- Python
- Flask
- Pandas
- Matplotlib
- HTML/CSS

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/expense-income-tracker.git
   cd expense-income-tracker

2. **Create a virtual environment**
3. **Activate the virtual environment**
    On Windows:
    venv\Scripts\activate

   on macOS and Linux:
   source venv/bin/activate
4. **Install dependencies**
     pip install -r requirements.txt
5. **Set up environment variables**
   USERNAME=your_username
   PASSWORD=your_password
6. **Run the application**
   python app.py
7. **Open the Application**
   Open your web browser and go to http://127.0.0.1:5000/

## Project structure
expense-income-tracker/
│
├── app.py
├── requirements.txt
├── .env
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── summary.html
│   ├── history.html
│   ├── login.html
├── transactions.csv
├── analysis.py
├── finance_data.py
├── finance_tracker.py
├── new.py
└── visualization.py

## License
This project is licensed under the MIT License. See the LICENSE file for details.

