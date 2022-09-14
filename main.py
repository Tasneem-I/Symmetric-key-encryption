from cryptography.fernet import Fernet

string = str(input()) 

print("your input: " , string)

key = Fernet.generate_key()

fernet = Fernet(key)

enc = fernet.encrypt(string.encode())

print("encrypted input: " , enc)

dec = fernet.decrypt(enc).decode()

print("decrypted input: " , dec)