from tkinter import *
calc=Tk()
calc.title('simple calculctor')
calc.configure(bg='black')


eq = StringVar()

entry=Entry(calc,textvariable=eq,font=('Arial',21)).grid(row=0,column=0,columnspan=50)


exp=''

def on_click(t):
    global exp
    exp=exp+str(t)
    eq.set(exp)

def equal():
    global exp
    try:
        result=str(eval(exp))
        eq.set(result)
    except:
        eq.set('error')
        exp=''

def clear():
    global exp
    exp=''
    eq.set(exp)

def one_clear():
    global exp
    exp=exp[:-1]+''
    eq.set(exp)

zero=Button(calc,text='0',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(0),fg='white')
zero.grid(row=5,column=0)


button1=Button(calc,text='1',activebackground='pink',width=10,bg='green',command=lambda:on_click(1),height=5,fg='white')
button1.grid(row=2,column=0)


button2=Button(calc,text='2',activebackground='pink',width=10,bg='green',command=lambda:on_click(2),height=5,fg='white')
button2.grid(row=2,column=1)


button3=Button(calc,text='3',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(3),fg='white')
button3.grid(row=2,column=2)


button4=Button(calc,text='4',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(4),fg='white')
button4.grid(row=3,column=0)


button5=Button(calc,text='5',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(5),fg='white')
button5.grid(row=3,column=1)


button6=Button(calc,text='6',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(6),fg='white')
button6.grid(row=3,column=2)


button7=Button(calc,text='7',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(7),fg='white')
button7.grid(row=4,column=0)


button8=Button(calc,text='8',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(8),fg='white')
button8.grid(row=4,column=1)


button9=Button(calc,text='9',activebackground='pink',width=10,height=5,bg='green',command=lambda:on_click(9),fg='white')
button9.grid(row=4,column=2)


plus=Button(calc,text='+',activebackground='pink',width=11,height=5,bg='green',command=lambda:on_click('+'),fg='white')
plus.grid(row=2,column=3)


minus=Button(calc,text='-',activebackground='pink',width=11,height=5,bg='green',command=lambda:on_click('-'),fg='white')
minus.grid(row=3,column=3)


mul=Button(calc,text='*',activebackground='pink',width=11,height=5,bg='green',command=lambda:on_click('*'),fg='white')
mul.grid(row=4,column=3)


div=Button(calc,text='/',activebackground='pink',width=11,height=5,bg='green',command=lambda:on_click('/'),fg='white')
div.grid(row=5,column=3)

equal_button=Button(calc,text='=',activebackground='pink',width=45,height=5,bg='green',fg='white',command=lambda:equal())
equal_button.grid(row=6,columnspan=22)

clear_button=Button(calc,text='CLEAR',activebackground='pink',width=10,height=5,bg='green',fg='white',command=lambda:clear())
clear_button.grid(row=5,column=2)




b1clear=Button(calc,text='DELETE',activebackground='pink',width=10,height=5,bg='green',fg='white',command=lambda:one_clear())
b1clear.grid(row=5,column=1)
calc.mainloop()
