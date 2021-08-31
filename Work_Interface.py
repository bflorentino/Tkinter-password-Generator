from PasswordClass import Password
from pyperclip import copy
from tkinter import messagebox

class Work_Interface():
    def __init__(self):
        self.password = Password(0, 0)
    

    def getPassword(self, strength: int, length: int, txtToSetPassword):
    # This method will get the password from the Password class 
        print(strength)
        self.password.setLength(length)
        self.password.setStrength(strength)
        txtToSetPassword.set(self.password.generatePassword())
        copy(txtToSetPassword.get())
        messagebox.showinfo("Copied password", "The Password has been copied to the clipboard")


    def changeSpinBoxInterval(self, spinBoxWidget, _from_: int, _to_:int):
    # Change the Spinbox range values according to the selected RadiButton
        spinBoxWidget.config(from_ = _from_)
        spinBoxWidget.config(to = _to_)
        spinBoxWidget.set(_from_)