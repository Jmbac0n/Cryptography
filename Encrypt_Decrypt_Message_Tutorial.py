from cryptography.fernet import Fernet

def write_key():

    # Generates key to file

    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():

    # Loads the key from the current dirct name 'key.key'

    return open("key.key", "rb").read()

write_key()
key = load_key()

message = "Secret message".encode()

f = Fernet(key)

encrypted = f.encrypt(message)

print(encrypted)

decrypted_encrypted = f.decrypt(encrypted)

print(decrypted_encrypted)