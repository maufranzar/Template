import os

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f'{MESSAGE_COLOR}Creating a new project...{RESET_ALL}')
print(f"Proyect path:{os.getcwd()}{RESET_ALL}")