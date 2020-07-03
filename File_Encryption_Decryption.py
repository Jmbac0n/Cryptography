import os
from cryptography.fernet import Fernet


# Load key

def load_key(key_to_use):

    return open(key_to_use, "rb").read()

# Encrypt chosen file 

def encrypt_file(filename, key):

    f = Fernet(key)

    with open(filename, "rb") as file:

        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):

    f = Fernet(key)

    with open(filename, "rb") as file:

        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:

        file.write(decrypted_data)

# Main body for operating script

def main():

    print("File Encryption/Decryption\n")

    # Input a file and a key to use

    print("Enter file location: ")
    file_loc = input()

    print("Select key to use: ")
    key_loc = input()

    key = load_key(key_loc)
    

    print("""\

        Select an Option:

        [1] Encrypt file
        [2] Decrypt file
        [3] Exit

    """)

    option = input()

    if option == "1":
        encrypt_file(file_loc, key)
    if option == "2":
        decrypt_file(file_loc, key)
    if option == "3":
        quit()
    

main()

#TODO

#Break down main into sub functions so that the user can decide to enter new file locations and keys or change them if incorrect
#Tbf probably best to ask option first then encrypt/decrypt
