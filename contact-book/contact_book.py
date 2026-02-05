print('Welcome to Contact Book.')

contacts = {}

def add_contact():
    name = input('Enter name: ')
    number = input('Enter phone number: ')
    contacts[name] = number
    print('Contact added successfully.')

def view_contacts():
    if len(contacts) == 0:
        print('No contacts found.')
    else:
        for name, number in contacts.items():
            print(f'{name} : {number}')

def search_contact():
    search_name = input('Enter name to search: ')
    found = False

    for name, number in contacts.items():
        if name.lower() == search_name.lower():
            print(f'{name} : {number}')
            found = True
            break

    if not found:
        print('Contact not found.')

while True:
    print('\n1. Add Contact')
    print('2. View Contacts')
    print('3. Search Contact')
    print('4. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Try again.')
