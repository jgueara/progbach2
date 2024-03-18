import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:
    def __init__(self):
        # Defino la ventana
        self.ventana1=tk.Tk()

        # Defino la barra de menú
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1) # Configuro el menú con la barra de menú

        # Única opción del menú dentro de la barra de menú
        opciones1 = tk.Menu(menubar1)

        # Primera opción
        opciones1.add_command(label="Dimensionar", command=self.fijartamano)

	# Agregamos separador
        opciones1.add_separator()  

        # Segunda opción del menú     
        opciones1.add_command(label="Salir", command=self.finalizar)

        # Título del menú
        menubar1.add_cascade(label="Opciones", menu=opciones1)

	# Definimos la etiqueta Ancho y el cuadro de texto entry1
        self.label1=ttk.Label(text="Ancho:")
        self.label1.grid(column=0, row=0)

	# Definimos la variable asociada al cuadro de texto
        self.ancho=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=10, textvariable=self.ancho)
        self.entry1.grid(column=1, row=0)      

        # Definimos la etiqueta Alto y el cuadro de texto entry2 
        self.label2=ttk.Label(text="Alto:")
        self.label2.grid(column=0, row=1)

	# Definimos la variable asociada al cuadro de texto
        self.alto=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, width=10, textvariable=self.alto)
        self.entry2.grid(column=1, row=1)        

        self.ventana1.mainloop()

    def fijartamano(self):
        self.ventana1.geometry(self.ancho.get()+"x"+self.alto.get())

    def finalizar(self):
        sys.exit()

aplicacion1=Aplicacion()
