from tkinter import *
from tkinter import messagebox
import valor



def si():
    
    root = Toplevel()
    root.geometry('280x300')
    root.configure(bg='black')
    img1 = PhotoImage(file='peru.png')
    select = IntVar()
    Label(root,image=img1,width=260,height=260).pack(padx=50,pady=50)
    Button(root,text='Salir',command=lambda root=root:quit(root),bg='pink').place(x=10,y=10)
    Button(root,text='Comenzar Prueba',command=prueba,bg='red').place(x=50,y=10)
    root.mainloop()


    



