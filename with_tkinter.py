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
  e2.insert(key)

def clr_pwd():
  e1.delete(0, END)


def clr_key_and_pwd():
  e1.delete(0, END)
  e2.delete(0, END)




lab1= Label(root, text= "Enter your password:")
lab2= Label(root, text="Here's your key")
lab_spc = Label(root, text= "")
e1= Entry(root, width= 50px, borderwidth=5px)
e2= Entry(root, width= 50px, borderwidth= 5px)

btn1= Button(root, padx= 15px, pady= 10px, text= "Submit", command= submit())
btn2= Button(root, padx= 15px, pady= 10px, text= "Clear", command= clr_pwd())
btn3= Button(root, padx= 15px, pady= 10px, text="Clear All", command= clr_key_and_pwd())

lab1.grid(row= 0,column= 0, columnspan=2)
e1.grid(row= 1, column= 0)
btn1.grid(row= 1, column= 1)
btn2.grid(row= 1,column= 2)
lab_spc.grid(row=2, column=0, rowspan=3)
lab2.grid(row= 4,column= 0, columnspan= 2)
e2.grid(row=5, column = 0)
btn3.grid(row= 5,column= 1,columnspan= 2)

root.mainloop()

