import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
import pyscrypt
#informing the user on what the program does
print("This is a password to key generator")
print("Enter a password below ")

#taking the input and converring it to bytes and storing it in a variable called password
password= input().encode()

print("Wait for a few seconds, it takes a while to generate key.") 
print("We apologise for the inconvenience")
#generating a salt of 16 bytes using the urandom function and storing it in a variable
salt = os.urandom(16) 


#using pyscrypt to generate a key. Pyscrypt is used here instead of pbkdf2 because pbkdf2 is not resistant to gpu and asic attacks

scrypt_key = pyscrypt.hash(
  password=password,
  salt= salt, 
  N= 1024,
  r= 8,
  p=1, 
  dkLen= 32
                          )

# making sure the key is url and file system safe by using a function from base64

key = base64.urlsafe_b64encode(scrypt_key)

print("Here's your key")
print(key)



