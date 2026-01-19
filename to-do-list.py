#To‑Do List Manager
#Used dictionary to store the details
#Added features like Add, Remove, Marking a work as done, exit

do_list = {'Workout':{'Status': 'Pending'},
           'Studying':{'Status': 'Pending'}}

print('----TO DO LIST----')
print(do_list)

while True:
    input_task = input('Enter the task u would like to add to [do-list] or type [No] to exit: ').lower()
    cap = input_task.title()
    if cap != 'No':
        do_list.update({cap:{'Status': 'Pending'}})
    else:
        break

    print('----TO DO LIST----')
    print(do_list)

    task_item = input('Enter the [task] on which u would like to perform an operation or enter [No] to exit: ').lower()
    correction = task_item.title()

    if correction == 'No':
        break 

    if correction not in do_list:
        print(f'Error---The task is entered incorrectly {correction}')
        continue

    operation = input('Enter [Mark] to mark the task as done, [Delete] to remove a task (or) [No] to exit: ').lower()
    available_operation = ['Mark', 'Delete', 'No']
    operation_corr = operation.title()
    if operation_corr == 'No':
        break

    if operation_corr not in available_operation:
        print(f'ERROR---The operation is entered incorrectly {operation_corr}')
        continue

    if operation_corr == 'Mark':
        do_list[correction].update({'Status': 'Done'})

    elif operation_corr == 'Delete':
        do_list.pop(correction)


print('----Your Updated Do-List----')
print(do_list)






