import sqlite3



def contract():
    again = True
    while again:
        ans_correct = False
        while not ans_correct:
            name = input('Name: \n')
            month_or_an = input("Monatlich/Jährlich: \n")
            amount = input("Betrag: \n")
            print(f"Name: {name}\n"
                  f"Monatlich/Jährlich: {month_or_an}\n"
                  f"Betrag: {amount}\n")
            ans = input("Korrekt? Y/N\n").lower()
            if ans == "y":
                ans_correct = True

        con = sqlite3.connect('database.db')
        cur = con.cursor()
        # Insert a row of data
        cur.execute("INSERT INTO contracts VALUES (? , ?, ?)", (name, month_or_an, amount))
        con.commit()
        con.close()
        print("Vertrag hinzufgefügt!")
        ans2 = input("Weiteren Vertrag hinzufügen? Y/N").lower()
        if ans2 == "n":
            again = False

