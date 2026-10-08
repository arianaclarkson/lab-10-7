
from zipfile import ZipFile, BadZipFile
import zlib

with open("Ashley-Madison.txt") as file:
    passwords = file.readlines()

for count, password in enumerate(passwords, start=1):
    password = password.strip()

    if count % 10000 == 0:
        print(count, password)

    try:
        with ZipFile("whitehouse_secrets.zip") as zf:
            zf.extractall(pwd=password.encode())
    except (RuntimeError, BadZipFile, zlib.error):
        continue

    print("Password found:", password)
    break
