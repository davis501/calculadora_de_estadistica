import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.dialog as dialog

class Menu_Bar:
    def __init__(self,windows):
        self.menu = tk.Menu()
        self.file_menu=tk.Menu(self.menu,tearoff=False)
        self.config_menu=tk.Menu(self.menu,tearoff=False)
        self.file_menu.add_command(label="Nuevo Cálculo",command=self.new_calc)
        self.config_menu.add_command(label="Personalizar",command=lambda:print("sda"))
        self.menu.add_cascade(menu=self.file_menu,label="Archivo")
        self.menu.add_cascade(menu=self.config_menu,label="Configuración")
        self.windows = windows
        self.windows.config(menu=self.menu)

    def new_calc(self):
        print("newcalc")
        if messagebox.askyesno(title="Nuevo Cálculo",message="¿Desea realizar un nuevo cálculo?\nEsto limpiará los datos actuales."):
            print("yes")

        else:
            print("no")