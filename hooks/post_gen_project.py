import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

subprocess.call(['tree'])

print(f"{MESSAGE_COLOR}Almost done!")
print("Actualiazndo Repositorio desde GitHub :D")
print(f"{MESSAGE_COLOR} powered by {RESET_ALL}")