#Contact Book (Basic)
#Used dictionary to store User name and their number
#Added the ability to [Add, remove] contacts, change number, change name, and exit

contact_book = {'Aryen':{'Number': 8235449183},
             'John':{'Number': 4316859603},
             'Sean':{'Number': 6025623462}}

print('-----CONTACT BOOK-----')
print(contact_book)
print('-------------------------')

print('Which operation would u like to perform: ')
print('Add=[ADD_CONTACT] Remove=[REMOVE_CONTACT] Change Num=[CHANGE_NUMBER] Change Name=[CHANGE_NAME] Exit=[EXIT]')

operation_available = ['Remove', 'Add', 'Change Num', 'Change Name']
while True:
    operation = input('Enter the operation to perform: ').lower()
    correction = operation.title()
    if correction == 'Exit':
        print('Program Exited')
        break

    if correction not in operation_available:
        print('ERROR-- Enter the proper operation')
        continue

    if correction == 'Add':
        name1 = input('Enter the name to add: ').lower()
        name_correction1 = name1.title()
        contact_add1 = int(input('Entre the number: '))
        contact_book.update({name_correction1:{'Number':contact_add1}})

    elif correction == 'Remove':
        name2 = input('Enter the name to remove: ').lower()
        name_correction2 = name2.title()

        if name_correction2 in contact_book:
            contact_book.pop(name_correction2)

        else:
            print('ERROR--- Enter the name properly')
            continue

    elif correction == 'Change Num':
        name_change1 = input('Enter the name for which number should be changed: ').lower()
        name_correction3 = name_change1.title()

        if name_correction3 in contact_book:
            num_change1 = int(input('Enter  the new number to replace with: '))
            contact_book[name_correction3].update({'Number':num_change1})

        else:
            print('ERROR--- Enter the correct name')
            continue

    elif correction == 'Change Name':
        name_change2 = input('Enter the name u want to change: ').lower()
        name_correction4 = name_change2.title()

        if name_correction4 in contact_book:
            replace = input(f'Enter the name to replace {name_correction4} : ').lower()
            name_replacement = replace.title()
            contact_book[name_replacement] = contact_book.pop(name_correction4)
            
        else:
            print('ERROR--- Enter the existing name properly')
        
print(contact_book)
