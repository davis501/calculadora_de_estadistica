import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox


class Messages:    
    def __init__(self):
        messagebox.showinfo(title="Bienvenido",message="Bienvenido a la calculadora de Estadística")

    def only_number_error(self,event):  
        if not event.keysym.isdigit() and event.keysym != "period" and event.keysym != "BackSpace":
            messagebox.showwarning(title="Alerta",message="No puedes ingresar texto en este campo")
        else:
            print(False)


        