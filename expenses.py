import sqlite3


def test_data():
    print("Lol so easy!")


def enter_expense():
    ans_correct = False
    while not ans_correct:
        name = input('Name: \n')
        category = input("Category: \n")
        price = input("Price: \n")
        print(f"Name: {name}\n"
              f"Category: {category}\n"
              f"Price: {price}\n")
        ans = input("correct? Y/N\n").lower()
        if ans == "y":
            ans_correct = True

    con = sqlite3.connect('database.db')
    cur = con.cursor()
    # cur.execute('''CREATE TABLE finance
    #              (name text, category text, price real)''')



    # Insert a row of data
    cur.execute("INSERT INTO finance VALUES (? , ?, ?)", (name, category, price))

    # Save (commit) the changes
    con.commit()
    con.close()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

