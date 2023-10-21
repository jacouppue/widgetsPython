#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Posgradito Upp")

opcion = IntVar()

# Función para el botón de envío
def actualiza_radio(valor):
    Label(root, text=valor).pack()

#RadioButton
Radiobutton(root,
           text="Rojo", 
           variable=opcion, 
           value=1).pack()

Radiobutton(root,
           text="Azul",
           variable=opcion, 
           value=2).pack()

Radiobutton(root,
           text="Verde",
           variable=opcion, 
           value=3).pack()

Radiobutton(root,
           text="Amarillo",
           variable=opcion, 
           value=4).pack()

# Botón de envío
boton_envia = Button(root,
           text="Enviar",
           command=lambda: actualiza_radio(opcion.get())).pack()

#Bucle de ejecución
root.mainloop()