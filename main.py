from overview import show_overview
from expenses import enter_expense
from income import enter_income
from contracts import contract


def main():
    print('Choose an option:')
    print('1. Show overview \n'
          '2. Enter expenses\n'
          '3. Enter income\n'
          '4. Contracts\n')

    correct_ans = False
    while not correct_ans:

        ans = input()

        if ans == "1":
            show_overview()
            correct_ans = True

        elif ans == "2":
            enter_expense()
            correct_ans = True

        elif ans == "3":
            enter_income()
            correct_ans = True

        elif ans == "4":
            contract()
            correct_ans = True

        else:
            print('Please enter a valid answer!')


if __name__ == '__main__':
    main()
