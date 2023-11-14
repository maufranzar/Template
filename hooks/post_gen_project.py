import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"
print(f"{MESSAGE_COLOR}Eliminando Git del Directorio!")
subprocess.call(['rm','-rf','.git'])
print(f"{MESSAGE_COLOR}Almost done!")
subprocess.call(['tree'])
print(f"{MESSAGE_COLOR}try: conda env create --file environment.yml {RESET_ALL}")