import sqlite3
def show_overview():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    print("Expenses: \n")
    for row in cur.execute('SELECT * FROM finance ORDER BY name'):
        print(row)

    print("\n\nIncomes: \n")
    for row in cur.execute('SELECT * FROM income ORDER BY name'):
        print(row)

    print("\n\nContracts: \n")
    for row in cur.execute('SELECT * FROM contracts ORDER BY name'):
        print(row)


show_overview()