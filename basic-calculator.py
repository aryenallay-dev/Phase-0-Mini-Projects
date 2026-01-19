#Basic Calculator
#Performs basic Arithmetic Operations

while True:
    num1 = int(input('Enter the first number: ')) 
    num2 = int(input('Enter the second number: ')) 
    operation = input('Enter the operation to be applied [+][-][*][/][%] or [exit] to exit: ').lower()
    available_operation = ['+', '-', '/', '*', '%','exit']
    if operation not in available_operation:
        print('-ERROR- pls enter the valid operation ')
        continue
    if operation in ['%', '/'] and num2 == 0:
        print('ERROR--- number cannot be [/] or [%] by 0')
        continue
    if operation == '+': 
        addition = num1 + num2 
        print(f'Addition: {addition}') 
    elif operation == '-':
        subtraction = num1 - num2 
        print(f'Subtraction: {subtraction}') 
    elif operation == '*': 
        multiplication = num1 * num2 
        print(f'Multiplication: {multiplication}') 
    elif operation == '/': 
        division = num1 / num2 
        print(f'Division: {division}') 
    elif operation == '%':
        modular = num1 % num2 
        print(f'Modular: {modular}')
    elif operation == 'exit':
        break


