import sqlite3


def enter_expense():
    again = True
    while again:
        ans_correct = False
        while not ans_correct:
            name = input('Name: \n')
            category = input("Kategorie(1-6): \n"
                             "1) Lebensmittel\n"
                             "2) Haushalt\n"
                             "3) Freizeit\n"
                             "4) Mobilität\n"
                             "5) Restaurants\n"
                             "6) Bildung\n")
            price = input("Preis: \n")
            month = input("Monat(1-12): \n")
            print(f"Name: {name}\n"
                  f"Kategorie: {category}\n"
                  f"Preis: {price}\n"
                  f"Monat: {month}\n")
            ans = input("Korrekt? Y/N\n").lower()
            if ans == "y":
                ans_correct = True

        con = sqlite3.connect('database.db')
        cur = con.cursor()

        cur.execute("INSERT INTO expenses VALUES (? , ?, ?, ?)", (name, category, price, month))
        con.commit()
        con.close()
        print("Ausgabe hinzufgefügt!")
        ans2 = input("Weitere Ausgaben hinzufügen? Y/N").lower()
        if ans2 == "n":
            again = False

