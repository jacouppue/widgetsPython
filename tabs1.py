import tkinter as tk					 
from tkinter import ttk 
#import serial

#myPort  = serial.Serial('/dev/ttyUSB')
#print(myPort.name)
##myPort.write(b'\nHello')
#myPort.close()

root = tk.Tk() 
root.title("Tab Widget") 
root.attributes('-alpha',0.75)
tabControl = ttk.Notebook(root) 

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 

tabControl.add(tab1, text ='Calculadora Numerica') 
tabControl.add(tab2, text ='Calculadora de Razones Financieras') 
tabControl.pack(expand = 1, fill ="both") 

ttk.Label(tab1, 
		text ="Welcome to GeeksForGeeks").grid(
            column = 0, 
			row = 5, 
			padx = 30, 
			pady = 30) 
ttk.Label(tab2, 
		text ="Lets dive into the world of computers").grid(column = 0, 
            row = 0, 
			padx = 30, 
			pady = 30) 

#Definimos botones por PESTAÑA!!!
#TAB1
#boton1 = ttk.Button(tab1, text="boton1 tab1")
#definicion del area de trabajo
Entry_Text = ttk.Entry(tab1, background='gray', font=("Calibri 20"))
Entry_Text.grid(row=0, column=0, columnspan=1, padx=5, pady=5)

#  espacio.grid(row=0, column=0, columnspan=4, padx=50, pady=5)
boton_ON = ttk.Button(tab2, text="ON", width=5)

boton0 = ttk.Button(tab1, text="0", width=5)
boton1 = ttk.Button(tab1, text="1", width=5)
boton2 = ttk.Button(tab1, text="2", width=5)
boton3 = ttk.Button(tab1, text="3", width=5)
boton4 = ttk.Button(tab1, text="4", width=5)
boton5 = ttk.Button(tab1, text="5", width=5)
boton6 = ttk.Button(tab1, text="6", width=5)
boton7 = ttk.Button(tab1, text="7", width=5)
boton8 = ttk.Button(tab1, text="8", width=5)
boton9 = ttk.Button(tab1, text="9", width=5)

boton_clr = ttk.Button(tab1, text="AC", width=5)
boton_par1 = ttk.Button(tab1, text="(", width=52)
boton_par2 = ttk.Button(tab1, text=")", width=5)
boton_dot = ttk.Button(tab1, text=".", width=5)

boton_ADD = ttk.Button(tab1, text="+", width=5)
boton_SUB = ttk.Button(tab1, text="-", width=5)
boton_MULT = ttk.Button(tab1,text="*", width=5)
boton_DIV = ttk.Button(tab1, text="/", width=5)
boton_EQU = ttk.Button(tab1, text="=", width=5)

#boton2 = ttk.Button(tab2, text="boton 1 tab2")
#definimos zona de grid para colocar botones y controles
boton7.grid(column=0, row=1, padx=5, pady=5) 
boton8.grid(column=1, row=1, padx=5, pady=5)
boton9.grid(column=2, row=1, padx=5, pady=5)
boton_DIV.grid(column=3, row=1, padx=5, pady=5)

boton4.grid(column=0, row=2, padx=5, pady=5) 
boton5.grid(column=1, row=2, padx=5, pady=5)
boton6.grid(column=2, row=2, padx=5, pady=5)
boton_MULT.grid(column=3, row=2, padx=5, pady=5)

boton1.grid(column=0, row=3, padx=5, pady=5) 
boton2.grid(column=1, row=3, padx=5, pady=5)
boton3.grid(column=2, row=3, padx=5, pady=5)
boton_SUB.grid(column=3, row=3, padx=5, pady=5)

boton0.grid(column=0, row=4, padx=5, pady=5) 
boton_dot.grid(column=1, row=4, padx=5, pady=5)
boton_EQU.grid(column=2, row=4, padx=5, pady=5)
boton_ADD.grid(column=3, row=4, padx=5, pady=5)


root.mainloop() 
