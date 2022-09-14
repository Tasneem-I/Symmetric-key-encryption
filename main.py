import tkinter as tk
import base64
import os
import pyscrypt

root = tk.Tk()
root.title("Password Encryptor")

def submit():
    lab2= Label(root, text="Your password is being encrypted. Do you wish to see the key?", state=ENABLED)
    btn3= Button(root, text="Yes", command= yes(), state=ENABLED)
    btn4= Button(root, text="No", command= no(), state= ENABLED) 
    pwd= e1.get()
    pwd= pwd.encode()
    salt = os.urandom(16) 
    scrypt_key = pyscrypt.hash(
      password=password,
      salt= salt, 
      N= 1024,
      r= 8,
      p=1, 
      dkLen= 32)
    key = base64.urlsafe_b64encode(scrypt_key)
    global key

def clr_pwd():
    e1.delete(0, END)


def clr_key_and_pwd():
    e1.delete(0, END)
    e2.delete(0, END)


def yes():
    lab2= Label(root, text="Your password is being encrypted. Do you wish to see the key?", state=DISABLED)
    btn3= Button(root, text="Yes", command= yes(), state=DISABLED)
    btn4= Button(root, text="No", command= no(), state= DISABLED) 
    lab3= Label(root, text="Here's your key")
    e2= Entry(root, width= 50px, borderwidth= 5px, state=ENABLED)
    btn5 = Button(root, text="Clear All", command= clr_key_and_pwd(), state= ENABLED)
    e2.insert(key)


def no():
    lab2= Label(root, text="Your password is being encrypted. Do you wish to see the key?", state=DISABLED)
    btn3= Button(root, text="Yes", command= yes(), state=DISABLED)
    btn4= Button(root, text="No", command= no(), state= DISABLED)
    



