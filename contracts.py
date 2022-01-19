import sqlite3


def contract():
    ans_correct = False
    while not ans_correct:
        name = input('Name: \n')
        month_or_an = input("Monthly/Annually: \n")
        amount = input("Price: \n")
        print(f"Name: {name}\n"
              f"Monthly/Annually: {month_or_an}\n"
              f"Amount: {amount}\n")
        ans = input("correct? Y/N\n").lower()
        if ans == "y":
            ans_correct = True

    con = sqlite3.connect('database.db')
    cur = con.cursor()
    # Insert a row of data
    cur.execute("INSERT INTO contracts VALUES (? , ?, ?)", (name, month_or_an, amount))

    # Save (commit) the changes
    con.commit()
    con.close()
contract()