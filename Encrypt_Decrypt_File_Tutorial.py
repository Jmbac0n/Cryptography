from cryptography.fernet import Fernet

def write_key():

    # Generates key to file

    key = Fernet.generate_key()

    with open("key2.key", "wb") as key_file:
        key_file.write(key)

def load_key():

    # Loads the key from the current dirct name 'key.key'

    return open("key2.key", "rb").read()

def encrypt(filename, key):

    # Given a filename + key it encrypts then writes it

    f = Fernet(key)

    with open(filename, "rb") as file:

        # Read all file data

        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    # Write encrypted file

    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):

    # Given a filename + key it decrypts then writes it

    f = Fernet(key)

    with open(filename, "rb") as file:

        # read the encrypted data

        encrypted_data = file.read()

    # decrypt data

    decrypted_data = f.decrypt(encrypted_data)

    #write the original file

    with open(filename, "wb") as file:

        file.write(decrypted_data)

write_key()
key = load_key()

file = "data.txt"

encrypt(file, key)