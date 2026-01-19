#Expense Tracker (Basic)
#Add features like Add, Check, Change Expenses, Delete, Exit

expense_list = {'Utilities':{'Expenses-$': 5000},
                'Groceries':{'Expenses-$': 12437}}

print('---EXPENSES_LIST---')
print(expense_list)

while True:
    user_input = input('Enter the following: \n-[Add] to add an expense to the list \n-[Check] to check if an item exist in the list \n-[Change Expense] to change an price of an expense \n-[Delete] to delete an expense from the list \n-[NO] to exit from the list \n  ')
    input_correction = user_input.title()
    input_available = ['Add', 'Check', 'No', 'Change Expense', 'Delete']

    if input_correction == 'No':
        break

    if input_correction not in input_available:
        print(f'ERROR--- Incorrect entry [{input_correction}]')
        continue

    if input_correction == 'Add':
        name_entry = input('Enter the name of the expense: ').lower()
        name_entry_correction = name_entry.title()
        if not name_entry_correction.isalpha():
            print('ERROR--- Expense name can only be string')
            continue
        expense_entry  = input('Enter the expense amount: ')
        if not expense_entry.isdigit():
            print('ERROR--- The expense cannot be a string')
            continue
        else:
            int_expenses = int(expense_entry)
            expense_list.update({name_entry_correction:{'Expenses-$': int_expenses}})

    if input_correction == 'Check':
        checking = input('Enter the name of the Expense to check: ').lower()
        check_correction = checking.title()
        if check_correction not in expense_list:
            print('The Expense does not exist in the list')
        elif check_correction in expense_list:
            print(expense_list[check_correction])

    if input_correction == 'Change Expense':
        print(expense_list)
        exp_name = input('Enter the name to change the expense: ').lower()
        nam_correction = exp_name.title()
        if nam_correction not in expense_list:
            print(f'ERROR---{nam_correction} does not exist in the list')
            continue
        expense_cost = input(f'Enter the amount u wanna to change {nam_correction} to: ')
        if not expense_cost.isdigit():
            print('ERROR--- the amount cannot be a string')
            continue
        else:
            int_cost = int(expense_cost)
            expense_list[nam_correction].update({'Expenses-$': int_cost})
            print(expense_list)

    if input_correction == 'Delete':
        print(expense_list)
        delete_name = input('Enter the expense name to delete: ').lower()
        delete_correction = delete_name.title()
        if not delete_correction.isalpha():
            print('ERROR--- The name should be string not number ')
            continue
        elif delete_correction not in expense_list:
            print(f'ERROR--- {delete_correction} does not exist in the list')
            continue
        else:
            expense_list.pop(delete_correction)
            print(expense_list)


