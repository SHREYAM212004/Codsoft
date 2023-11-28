from tkinter import *
from tkinter import messagebox
import json

wi=Tk()

wi.title('TODO-LIST')
wi.geometry('395x450')
wi.configure(bg='black')

task=''
date=''
time=''

def add_task():
    global task
    task=entry.get()
    if task!='':
        entry.delete(0,END)
    else:
        messagebox.showwarning(title='warning!',message='enter the task')


def add_date():
    global date
    date=entry.get()
    if date!='':
        entry.delete(0,END)
    else:
        messagebox.showwarning(title='warning!',message='enter the date')

def load_task():
        file=open('D:\\PASSWORD.txt','r')
        listbox.delete(0,END)
        TASK=file.readlines()
        for tas in TASK:
            listbox.insert(END,tas)



def add_time():
    global time
    time=entry.get()
    if time!='':
        entry.delete(0,END)
    else:
        messagebox.showwarning(title='warning!',message='enter the time')



def sub():
    global task
    global date
    global time
    det=(task,date,time)
    listbox.insert(END,det)

def save():
    global task
    global date
    global time
    det=[task,date,time]
    file=open('D:\\PASSWORD.txt','a')
    file.write(json.dumps(det)+'\n')
    file.close()

def dele():
    items=listbox.curselection()

    for i in items[::-1]:
        listbox.delete(i)



label1=Label(wi,text='enter the task here',anchor=CENTER,height=4,width=50,font=('Arial',10))
label1.place(x=0,y=0)

value=StringVar()
entry=Entry(wi,textvariable=value,font=('Arial',28))
entry.place(x=0,y=60)

btask=Button(wi,text='add task',height=3,width=18,bg='coral',command=add_task)
btask.place(x=0,y=105)

bdate=Button(wi,text='add date',height=3,width=17,bg='lemon chiffon',command=add_date)
bdate.place(x=135,y=105)

btime=Button(wi,text='add time',height=3,width=17,bg='gold',command=add_time)
btime.place(x=265,y=105)

bsub=Button(wi,text='sub',height=3,width=15,bg='pale green',command=sub)
bsub.place(x=0,y=395)


bdel=Button(wi,text='delete',height=3,width=15,bg='sky blue',command=dele)
bdel.place(x=100,y=395)

bsave=Button(wi,text='save',height=3,width=15,bg='light pink',command=save)
bsave.place(x=200,y=395)

bload=Button(wi,text='load task',height=3,width=15,bg='light grey',command=load_task)
bload.place(x=300,y=395)

listbox=Listbox(wi,width=50,height=10,selectmode=MULTIPLE,font=('Arial',15))
listbox.place(x=0,y=150)





wi.mainloop()
