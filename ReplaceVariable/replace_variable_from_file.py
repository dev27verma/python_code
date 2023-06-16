import os
import fileinput

def replace_variable(file_path, variable_name, new_value):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            if variable_name in line:
                line = line.replace(variable_name, new_value)
            print(line, end='')


def traverse_directories(folder_path, variable_name, new_value):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                replace_variable(file_path, variable_name, new_value)
                print(f'Replaced variable in: {file_path}')


# Get the folder path, variable name, and new value from the user
folder_path = input('Enter the folder path: ')
variable_name = input('Enter the variable name: ')
new_value = input('Enter the new value: ')

# Call the function to traverse directories and replace the variable
traverse_directories(folder_path, variable_name, new_value)
