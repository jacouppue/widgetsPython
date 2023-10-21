
from tkinter import *

#se genera objeto ventana
ventana = Tk()
##### aqui se definen los elementos de la ventana
ventana.title("controles RadioButton")

#area de definicion VARIABLES Y FUNCIONES
opcion = IntVar()
opcion.set(1)

def OpcionSelect(valor):
    LabelOP["text"]= valor
    
#agregamos elementos a ventana
RadioRojo = Radiobutton(ventana, text="Rojo", variable=opcion, value=1)
RadioAzul = Radiobutton(ventana, text="Azul", variable=opcion, value=2)
RadioVerde= Radiobutton(ventana, text="Verde", variable=opcion, value=3)
RadioYellw= Radiobutton(ventana, text="Amarillo", variable=opcion, value=4)

SendButton = Button(ventana, text="enviar opcion seleccionada", 
                    command=lambda:OpcionSelect( opcion.get() ))
LabelOP = Label(ventana, text="")
# layaout
RadioRojo.pack()
RadioVerde.pack()
RadioAzul.pack()
RadioYellw.pack()
SendButton.pack()
LabelOP.pack()


###### se termina objeto ventana
ventana.mainloop()
