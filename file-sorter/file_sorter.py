import os
import shutil

print('Starting File Sorter...')

path = r"C:\Users\Umer Azmi\Downloads\Project"

try:
    file_name = os.listdir(path)
    print('\nFiles found:\n')
    print('\n'.join(file_name))
except:
    print('Invalid path.')
    quit()


folder_name = [
    'Image Folder',
    'PDF & Word Folder',
    'Spreadsheet Folder'
]


for loop in folder_name:
    folder_path = f'{path}\\{loop}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


for file in file_name:
    source = f'{path}\\{file}'

    if file.lower().endswith(('.jpg', '.img', '.png')) and not os.path.exists(f'{path}\\Image Folder\\{file}'):
        shutil.move(source, f'{path}\\Image Folder\\{file}')

    elif file.lower().endswith(('.pdf', '.docx')) and not os.path.exists(f'{path}\\PDF & Word Folder\\{file}'):
        shutil.move(source, f'{path}\\PDF & Word Folder\\{file}')

    elif file.lower().endswith(('.csv', '.xls', '.xlsx')) and not os.path.exists(f'{path}\\Spreadsheet Folder\\{file}'):
        shutil.move(source, f'{path}\\Spreadsheet Folder\\{file}')

print('\nFile sorting completed successfully.')