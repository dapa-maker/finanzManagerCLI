import sqlite3


def enter_income():
    print("enter income")
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    ans_correct = False
    while not ans_correct:
        name = input('Name: \n')
        amount = input("Amount: \n")

        print(f"Name: {name}\n"
              f"Amount: {amount}\n")
        ans = input("correct? Y/N\n").lower()
        if ans == "y":
            ans_correct = True
    # Insert a row of data
    cur.execute("INSERT INTO income VALUES (? , ?)", (name, amount))

    # Save (commit) the changes
    con.commit()
    con.close()

