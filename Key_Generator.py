import shutil, os
from cryptography.fernet import Fernet

# Set Source and Destination file locations

file_source = "D://MyScripts//Cryptography//" 
file_dest = "D://MyScripts//Keys"

# Generate key with user created name

print("Encryption Key Generator")
print("----------------------------\n")

print("Input a name for key: ")
key_name = input()

def write_key(keyname):

    key = Fernet.generate_key()

    with open(keyname, "wb") as key_file:
        key_file.write(key)
        print("Key generated in: " + file_source)
        
# Move key to Keys folder

def move_keys(keyname):
    
    source = file_source + (str(keyname))
    dest = file_dest

    shutil.move(source, dest)
    print("Successfuly moved to: " + file_dest)

write_key(key_name)
move_keys(key_name)