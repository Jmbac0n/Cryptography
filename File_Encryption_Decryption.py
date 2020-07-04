import os
from cryptography.fernet import Fernet

file_loc = ""
global_key = ""

# Enter location of file

def enter_file_location():

    global file_loc

    print("Enter file location: ")
    file_loc = input()

# Load key

def load_key():

    global global_key

    print("Select key to use: ")
    key_to_use = input()
    
    global_key = open(key_to_use, "rb").read()

# Encrypt chosen file 

def encrypt_file():

    filename = file_loc
    key = global_key

    f = Fernet(key)

    with open(filename, "rb") as file:

        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Decrypt chosen file

def decrypt_file():

    filename = file_loc
    key = global_key

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
    
    print("""\

        Select an Option:

        [1] Load file
        [2] Select key
        [3] Encrypt
        [4] Decrypt
        [5] Exit

    """)

    print("Loaded file: " + file_loc)
    print("Loaded key: " + (str(global_key))) # Loads actual key not the key loc

    option = input()

    if option == "1":
        enter_file_location()
        main()
    if option == "2":
        load_key()
        main()
    if option == "3":
        encrypt_file()
        main()
    if option == "4":
        decrypt_file()
        main()
    if option == "5":
        quit()
    

main()

#TODO

#Break down main into sub functions so that the user can decide to enter new file locations and keys or change them if incorrect
#Tbf probably best to ask option first then encrypt/decrypt
