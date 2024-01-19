#imports tkinter module
from tkinter import *

#imports pyperclip module to copy generated password to clipboard
import pyperclip

#random module will be used to generate random passwords
import random

#initialize tkinter
root = Tk()

#sets width and height of the GUI
root.geometry('400x400')

# declares a variable of str tyoe and this variable will be used to store the password generated
passStr = StringVar()

# declares a variable of int type which will be used to store the len of password generated
passLen = IntVar()

# sets length of password to zero initially
passLen.set(0)

#fxn to generate password
def generate():
    # storing the keys in a list which will be used to generate the password
    pass1 = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m'
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
        'A','B','C','D','E','F','G','H','I','J','K','L','M'
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        '1','2','3','4','5','6','7','8','9','0','@','#','$'
        '%','^','&','*'
    ]

    #declares empty string
    password = ''

    #loop to generate random password of the length entered by user
    for x in range(passLen.get()):
        password = password + random.choice(pass1)

    #sets password to entry widget
    passStr.set(password)


#fxn to copy password to clipboard
def copytoclipboard():
    random_password = passStr.get()
    pyperclip.copy(random_password)

#creates a text label widget
Label(root,text='Password Generator Application', font='calibri 20 bold').pack()

#creates a text label widget
Label(root, text='Enter password length').pack(pady=3)

#creates an entry widget to take password length entered by user
Entry(root,textvariable=passLen).pack(pady=3)

#button to call the generate fxn
Button(root,text='Generate Password', command=generate).pack(pady=7)

#entry widget to show the generated 
Entry(root,textvariable=passStr).pack(pady=3)

# button to call the copytoclipboard fxn
Button(root,text='Copy to clipboard',command=copytoclipboard).pack()

#mainloop() is an infinite loop used to run an app when it's in ready state
root.mainloop()
