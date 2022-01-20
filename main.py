from overview import show_overview
from expenses import enter_expense
from income import enter_income
from contracts import contract


def main():
    correct_ans = False
    while not correct_ans:
        print('Choose an option:')
        print('1. Show overview \n'
              '2. Enter expenses\n'
              '3. Enter income\n'
              '4. Contracts\n')
        ans = input()

        if ans == "1":
            show_overview()

        elif ans == "2":
            enter_expense()

        elif ans == "3":
            enter_income()

        elif ans == "4":
            contract()

        elif ans == "end":
            correct_ans = True


if __name__ == '__main__':
    main()
