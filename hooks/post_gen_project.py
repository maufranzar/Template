import subprocess

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f'{ERROR_COLOR} Template created!{RESET_ALL}')
subprocess.call(['tree'])
print(f"{MESSAGE_COLOR}Initializing Git...{RESET_ALL}")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'branch','-M', 'main'])
subprocess.call(['git', 'add', '.gitignore'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', '"First Commit!"'])
print(f"{ERROR_COLOR}First Commit... Done{RESET_ALL}")
print(f'{ERROR_COLOR}Dont forget configure Git!! {RESET_ALL}')

print(f"{MESSAGE_COLOR}Now, create your environment with conda:{RESET_ALL}")
print(f'conda env create --file environment.yml {RESET_ALL}')