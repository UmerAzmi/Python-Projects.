print('Welcome to Expense Tracker.')

expenses = []

def add_expense():
    name = input('Enter expense name: ')
    try:
        amount = float(input('Enter amount: '))
        expenses.append((name, amount))
        print('Expense added.')
    except:
        print('Invalid amount.')

def view_expenses():
    if not expenses:
        print('No expenses recorded.')
    else:
        for name, amount in expenses:
            print(f'{name} : {amount}')

def total_expense():
    total = sum(amount for _, amount in expenses)
    print(f'Total expense: {total}')

while True:
    print('\n1. Add Expense')
    print('2. View Expenses')
    print('3. Total Expense')
    print('4. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expense()
    elif choice == '4':
        print('Thank you!')
        break
    else:
        print('Invalid choice.')
