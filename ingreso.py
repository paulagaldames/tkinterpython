from tkinter import *
import pandas as pd
from tkinter import ttk


def impuesto():
    precio = float (ingreso_e.get())
    impuesto = precio * 0.20
    calculo = precio + impuesto
    return vari.set(calculo)

def exporta():
    campo1 = nombre_e.get()
    campo2 = apellido_e.get()
    campo3 = rut_e.get()
    campo4 = sexo_e.get()
    campo5 = ingreso_e.get()
    campo6 = impuesto_e.get()
    registro=[campo1, campo2, campo3, campo4, campo5, campo6]
    registro = pd.DataFrame(registro)
    registro.to_csv('CalculoDeimpuesto.csv')




ventana = Tk()
vari=StringVar()
ventana.title('Impuesto a la renta')
ventana.geometry('500x500')
ventana.resizable(FALSE, FALSE)
principal_label = Label(text='Impuesto al sueldo', font=('Cambria', 14, 'bold'), justify='center', fg ='Black', width=50, height=1)
principal_label.place(x=0, y=0)

nombre_t = Label(text='Nombre', font=('Cambria', 14, 'bold'), fg ='Black')
nombre_t.place(x=0, y=100)

apellido_t= Label(text='Apellido', font=('Cambria', 14, 'bold'), fg ='Black')
apellido_t.place(x=0, y=150)

rut_t= Label(text='Rut', font=('Cambria', 14, 'bold'), fg ='Black')
rut_t.place(x=0, y=200)

sexo_t= Label(text='Sexo', font=('Cambria', 14, 'bold'), fg ='Black')
sexo_t.place(x=0, y=250)

ingreso_t= Label(text='Ingreso', font=('Cambria', 14, 'bold'), fg ='Black')
ingreso_t.place(x=0, y=300)

impuesto_t= Label(text='Impuesto', font=('Cambria', 14, 'bold'), fg ='Black')
impuesto_t.place(x=0, y=350)

#campos de entrada

nombre_e = StringVar()
apellido_e = StringVar()
rut_e = StringVar()
ingreso_e= float()
impuesto_e = StringVar()



nombre_e= Entry(width=40, textvariable=nombre_e)
nombre_e.place(x=200, y=105)

apellido_e = Entry(width=40, textvariable=apellido_e)
apellido_e.place(x=200, y=155)

rut_e = Entry(width=40, textvariable=rut_e)
rut_e.place(x=200, y=205)

sexo_e=ttk.Combobox(width=40)
sexo_e.place(x=200, y=255)
opciones_sexo=['Masculino', 'Femenino']
sexo_e['values']=opciones_sexo

ingreso_e = Entry(width=40, textvariable=ingreso_e)
ingreso_e.place(x=200, y=305)

impuesto_e = Entry(width=40, textvariable=impuesto_e)
impuesto_e.place(x=200, y=355)

boton = Button(text='Total a pagar con impuesto', command=impuesto)
boton.place(x=200, y=400)

boton = Button(text='Exportar', command=exporta)
boton.place(x=370, y=400)

calcu=Label(width=20, textvariable=vari)
calcu.place(x=200, y=450)

mainloop()