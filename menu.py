#!/usr/bin/env python
from tkinter import *
import tkinter as tk
import socket
import getpass
from cc_gen import *
from si import *

#codigo espagetti
#consumidor de recursos 2.0

class bc():#bacajr

    def __new__(self):
        #funcion informacion del usuario
        import ipinfo
        username = getpass.getuser()#nombre de usuario
        hostname = socket.gethostname()#nombre de la maqina
        maquinaIP = socket.gethostbyname(hostname)#ip del usuario
        
        access_token = '6da13029b22db7'#key de la api
        handler = ipinfo.getHandler(access_token)#obtenrer acceso a ala api
        details = handler.getDetails()#creacion de la variable details para obtener informacion[capa8]

        print("\nMI NUEVA VICTIMA :",username)
        print("Nombre de la maquina :",hostname)
        print('IP del la  maquina :',maquinaIP)
        print("IP Privada"+":   ",details.ip)
        print("Ciudad"+": ",details.city)
        print("Geolocacion"+" :",details.loc)
        x = details.all
        for k,v in x.items():
            print("[¡]",k,v)
        print('\n[¡]'+"TENGO TU DIRECCION NENE, AHORA PUEDO IR POR TUS PATAS")
        
def xd():#boton sorpresa 
    bin_muestra = "450911xxxxxxxxxx"
    num = Generar_tarjeta(bin_muestra,16,True)
    json = num.json()
    while True:
        print("\n[*]Quieres poner tu propio Binsito :")
        print("[*]Si\n[*]No")
        user_input = input(":")
        if user_input == "si":
            try:
                print("\n[¡] EJEMPLO: 450911xxxxxxxxxx [¡]SON 16 DIGITOS[¡]")
                bin_muestra = input("ingrese aqui solo numeros[0-9] y 'x' :")
                num = Generar_tarjeta(bin_muestra,16,True)
                json = num.json()
            except ValueError:
                print("\n[¡] FALTARON NUMEROS Ó INGRESO MAL ALGO :")
            finally:
                pass
        elif user_input == "no":
            root = Tk()
            root.geometry('150x150')
            root.configure(bg='black')
            
            Button(root,width=5,height=5,text='SALIR',command=lambda root=root:quit(root)).place(x=10,y=10)
            Button(root,width=5,height=5,text='NUEVO',command=xd).place(x=100,y=10)
            root.mainloop()
        else:
            print("\n")
            
        
def quit(root):#funcion para salir //uso de lambda
    c = 'ni_modo,'*5
    for i in range(len(c)):
        print(c,c)
    root.destroy()
   

##____ventana principal____
root = Tk()
root.title('ConchaTuMadre')
root.geometry('260x520')
root.resizable(False,False)
root.configure(bg='black')

## test para saber si eres peruano V1.0(chipiada)
iframe = Frame()
iframe.pack()
iframe.configure(bg='Lightblue')
iframe.config(cursor="pirate")
Label(iframe,text='¿ Comensar Test Para saber si usted es Peruano?').pack(fill=X, padx=4, pady=4)
Button(iframe,text='SI',command=si,bg='Lightgreen').pack(fill=X, padx=5, pady=5)
Button(iframe,text='No',command=lambda root=root:quit(root),bg='Lightgreen').pack(fill=X, padx=6, pady=6)
Button(iframe,text='No shabon shó le voi al Boca',command=bc,bg='Lightyellow').pack(fill=X, padx=7, pady=7)

#premio
Button(iframe,text='[¡]No precionar[¡]',command=xd,bg='pink').pack(fill=X,padx=8,pady=8)
img1 = PhotoImage(file='ooo.png')
i_f = Label(iframe,image=img1).pack(padx=10, pady=10)

root.mainloop()


#__shit__
#fill=X, padx=5, pady=5
#salir de la ventana
#def quit(root):
#    root.destroy()
#Button(iframe,text='No',command=lambda root=root:quit(root))
