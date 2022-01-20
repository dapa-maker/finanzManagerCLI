import sqlite3


def enter_income():
    again = True
    while again:
        print("enter income")
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        ans_correct = False
        while not ans_correct:
            name = input('Name: \n')
            amount = input("Betrag: \n")
            month = input("Monat(1-12): \n")

            print(f"Name: {name}\n"
                  f"Betrag: {amount}\n"
                  f"Monat: {month}\n")
            ans = input("Korrekt? Y/N\n").lower()
            if ans == "y":
                ans_correct = True

        cur.execute("INSERT INTO income VALUES (? , ?, ?)", (name, amount, month))
        con.commit()
        con.close()
        print("Einnahme hinzufgefügt!")
        ans2 = input("Weitere Einnahmen hinzufügen? Y/N").lower()
        if ans2 == "n":
            again = False

