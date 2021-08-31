from tkinter import ttk
import tkinter as tk
from Work_Interface import Work_Interface

class Interface():
    def __init__(self, Root):
        self.Root = Root
        self.pswFunctions = Work_Interface()
        self.Rdbtn = tk.IntVar(value = 0)


######## Basic Window settings #########  
    def setRootSettings(self):

        self.Root.config(background = "#302F30")
        self.Root.geometry("400x400")
        self.Root.resizable(False, False)
        self._setGuiTitle()
        self._setRadioButtons()
        self._setLengthPicker()
        self._setGeneratePsButton()


##########  Set a ttitle to GUI ############
    def _setGuiTitle(self):

        TitleFrame = tk.Frame(self.Root, bg = "#302F30")
        TitleFrame.pack(anchor=tk.CENTER, pady = 15)
        title = tk.Label(TitleFrame, text = "Password\nGenerator", fg = "#69EE41", font = ("Bahnschrift SemiBold", 30, "bold"), bg= "#302F30")
        title.pack()


######## GUI RadioButton selection ########### 
    def _setRadioButtons(self):

        self.WidgetsFrame = tk.Frame(self.Root, bg = "#302F30")
        self.WidgetsFrame.pack()
        rdbtnFrame = tk.Frame(self.WidgetsFrame, bg = "#302F30")
        rdbtnFrame.pack(anchor = "nw", side = tk.LEFT)
        
        rdbtnTitle = tk.Label(rdbtnFrame, 
                            text = "Select the password\nstrength level", 
                            font = ("Bahnschrift SemiBold", 13, "bold"), 
                            fg = "#DBE1DE", bg = "#302F30", 
                            justify="left")
        
        rdbtnTitle.pack(anchor = "nw")
        rdbtnWeakFrame = tk.Frame(rdbtnFrame, bg = "#302F30")
        rdbtnWeakFrame.pack(anchor = "nw")
        
        rdbtnWeak = tk.Radiobutton(rdbtnWeakFrame, variable = self.Rdbtn, value = 0, 
                                    bg ="#302F30", 
                                    command=lambda:self.pswFunctions.changeSpinBoxInterval(self.spinLength, 5, 9))
        
        rdbtnWeak.grid(row = 0, column = 0)
        rdbtnWeak.select()
        rdbtnWeaktxt = tk.Label(rdbtnWeakFrame, text = "Weak (5-9 chars)", bg ="#302F30", fg = "#DBE1DE").grid(row = 0, column = 1, pady = 3)
        rdbtnMedFrame = tk.Frame(rdbtnFrame, bg = "#302F30")
        rdbtnMedFrame.pack(anchor = "nw")
        
        rdbtnMed = tk.Radiobutton(rdbtnMedFrame, 
                                variable = self.Rdbtn, 
                                value = 1, bg = "#302F30", 
                                command=lambda:self.pswFunctions.changeSpinBoxInterval(self.spinLength, 10, 14)).grid(row = 0, column = 0)
        
        rdbtMedtxt = tk.Label(rdbtnMedFrame, text = "Medium (10-14 chars)", bg ="#302F30", fg = "#DBE1DE").grid(row = 0, column = 1)
        
        rdbtnMaxFrame = tk.Frame(rdbtnFrame, bg = "#302F30")    
        rdbtnMaxFrame.pack(anchor = "nw")

        rdbtnMax = tk.Radiobutton(rdbtnMaxFrame, 
                                variable = self.Rdbtn, 
                                value = 2, bg = "#302F30", 
                                command=lambda:self.pswFunctions.changeSpinBoxInterval(self.spinLength, 15, 25)).grid(row = 0, column = 0)
        
        rdbtMaxtxt = tk.Label(rdbtnMaxFrame, text = "Strong(15-25 chars)", bg ="#302F30", fg = "#DBE1DE").grid(row = 0, column = 1)  


########GUI Password Length Selection ############ 
    def _setLengthPicker(self):

        spinBoxFrame = tk.Frame(self.WidgetsFrame, bg = "#302F30")
        spinBoxFrame.pack(side = tk.LEFT, anchor="nw", padx = (55,0), pady = 5)

        spinBoxLabel = tk.Label(spinBoxFrame, text = "Pick out the password\nlength", 
                                font = ("Bahnschrift SemiBold", 13, "bold"), 
                                fg = "#DBE1DE", 
                                bg = "#302F30", 
                                justify="left")

        spinBoxLabel.pack()
        self.spinLength = ttk.Spinbox(spinBoxFrame, from_=5, to=9, width = 5, state="readonly", wrap=True)
        self.spinLength.pack(pady = 15)
        self.spinLength.set(5)


######## GUI Generate Password Button and label ############ 
    def _setGeneratePsButton(self):

        passwordtxt = tk.StringVar(value = "")
        GetPsButtonFrame = tk.Frame(self.Root, bg = "#302F30")
        GetPsButtonFrame.pack()
        
        GetPasswordBtn = tk.Button(GetPsButtonFrame, text = "Get Passsword", 
                                    bd = 0, bg = "#17B525", font = ("Bahnschrift SemiBold", 15, "bold"), 
                                    fg = "#DBE1DE", cursor="hand2", 
                                    command = lambda: self.pswFunctions.getPassword(self.Rdbtn.get(), int(self.spinLength.get()), passwordtxt))
        
        GetPasswordBtn.pack(pady = 10)
        
        passwordLabel = tk.Label(GetPsButtonFrame,
                        textvariable = passwordtxt, 
                        bg = "#302F30", 
                        font = ("Bahnschrift SemiBold", 15, "bold"), fg = "#DBE1DE")
        
        passwordLabel.pack(pady = 5)
        
Root = tk.Tk()
GrapUI = Interface(Root)
GrapUI.setRootSettings()
Root.mainloop() 