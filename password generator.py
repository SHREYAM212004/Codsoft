
from tkinter import *
from tkinter.ttk import Combobox
import random
import string
win=Tk()

win.title('PASSWORD GENERATOR')
win.geometry('390x400')


def sub():
    len_of_password=value.get()
    s1 = string.ascii_lowercase
    s2 = string.digits
    s3 = string.ascii_uppercase
    s4 = string.punctuation
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    text.set(''.join(s[0:len_of_password]))
label=Label(win,text='enter the length of password',height=2,width=25,font=('Arial',21),bg='navajo white').place(x=0,y=10)



digits=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
value=IntVar()

len_of_password=Combobox(win,textvariable=value,state='readonly',font=('Arial',13))
len_of_password['values']=[l for l in digits]
len_of_password.place(x=85,y=85)



button=Button(win,text='GENERATE PASSWORD',height=2,width=20,bg='dark salmon',command=sub).place(x=105,y=125)
text=StringVar()
display=Entry(win,textvariable=text,font=('Arial',28))
display.place(x=0,y=255)

label1=Label(win,text='your password is',height=2,width=28,bg='pink',font=('Arial',18)).place(x=0,y=185)



win.mainloop()



