import sqlite3
from datetime import datetime


today = datetime.today().month

print(f"Aktueller Monat ({today}): \n")


def show_overview():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    chosen_month = [today]
    expenses = 0.0
    incomes = 0.0

    for name, category, price, month in cur.execute('SELECT * FROM expenses WHERE month =?', chosen_month):
        expenses += price

    for name, amount, month in cur.execute('SELECT * FROM income WHERE month=?', chosen_month):
        incomes += amount





    difference = incomes - expenses

    print(f"Einnahmen: {incomes}€")
    print(f"Ausgaben: -{round(expenses, 2)}€")
    print(f"Differenz: {difference}€")

    print("\nContracts:")
    for name, period, amount in cur.execute('SELECT * FROM contracts ORDER BY name'):
        print(f"{name}: {amount}€ pro {period}")

    input("\n"
          "Presse Enter um fortzufahren...")
