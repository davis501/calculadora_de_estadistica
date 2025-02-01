import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.dialog as dialog
from message import *
from menubar import Menu_Bar

class Master_Windows:
    windows = tk.Tk()
    windows.geometry("500x600")
    windows.title("Calculadora")
    windows.resizable(height=True,width=True)
    message = Messages()
    
    menu_bar = Menu_Bar(windows)

    sv = tk.StringVar()
    sv="Bienvenidos"
    insert_name=ttk.Entry(windows)
    welcome = ttk.Label()
    welcome.pack()
    
    ttk.Combobox(windows,values=["ff","ffs","ffdadf"]).pack()
    
    def __init__(self):     
        self.welcome.master=self.windows
        self.welcome.config(text=self.sv)
        self.insert_name.bind("<Key>",self.message.only_number_error)
        self.insert_name.pack()
        self.windows.mainloop()
          

    #windows.bind("<Key>",message.only_number_error)

    