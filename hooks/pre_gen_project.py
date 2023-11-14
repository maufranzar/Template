import os
import sys
import subprocess

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m" # To change the terminal color
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f'{MESSAGE_COLOR}Iniciando Entorno...')

subprocess.call(['git', 'init'])
subprocess.call(['git', 'status'])
subprocess.call(['git', 'pull', 'origin', 'Data'])

if project_slug.startswith("x"):
    print(f'{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}')

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")