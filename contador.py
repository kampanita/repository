import tkinter

contador=0
ventana=tkinter.Tk()
etiqueta=tkinter.Label(ventana,text=str(contador))
etiqueta.pack()

def suma_uno():
    global contador
    contador=contador+1
    etiqueta["text"]=str(contador)
    etiqueta.pack()

def suma_medio():
    global contador
    contador=contador+0.5
    etiqueta["text"]=str(contador)
    etiqueta.pack()

def resta_uno():
    global contador
    contador=contador-1
    etiqueta["text"]=str(contador)
    etiqueta.pack()

def resta_medio():
    global contador
    contador=contador-0.5
    etiqueta["text"]=str(contador)
    etiqueta.pack()


boton1=tkinter.Button(ventana,text="Suma 1",command=suma_uno)
boton2=tkinter.Button(ventana,text="Suma 1/2",command=suma_medio)
boton3=tkinter.Button(ventana,text="Resta 1",command=resta_uno)
boton4=tkinter.Button(ventana,text="Resta 1/2",command=resta_medio)

boton1.pack()
boton2.pack()
boton3.pack()
boton4.pack()

ventana.mainloop()