print('Welcome to To-Do List App.')

tasks = []

def add_task():
    task = input('Enter a new task: ')
    tasks.append(task)
    print('Task added.')

def view_tasks():
    if len(tasks) == 0:
        print('No tasks available.')
    else:
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')

def remove_task():
    view_tasks()
    try:
        task_no = int(input('Enter task number to remove: '))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f'Task "{removed}" removed.')
        else:
            print('Invalid task number.')
    except:
        print('Please enter a valid number.')

while True:
    print('\n1. Add Task')
    print('2. View Tasks')
    print('3. Remove Task')
    print('4. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice.')
