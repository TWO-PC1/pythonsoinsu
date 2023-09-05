import tkinter as tk
import math
from math import *
window = tk.Tk()
window.title('My App')
window.geometry("200x200+300+100")#가로x세로+x좌표+y좌표
window.resizable(False,False)
entry = tk.Entry(window)
def calc(event):

    result=str(eval(entry.get()))
    value=str(entry.get())
    entry.delete(0,len(entry.get()))
    entry.insert(0,result)
    label.config(text=value+'='+result)
   # label.config(text='결과'+str(eval(entry.get())))

entry.bind("<Return>",calc)
entry.grid(row=0,column=0,columnspan=4)
def funcClear():
    entry.delete(0,len(entry.get()))
def func0():
    entry.insert(len(entry.get()),'0')
def func1():
    entry.insert(len(entry.get()),'1')
def func2():
    entry.insert(len(entry.get()),'2')
def func3():
    entry.insert(len(entry.get()),'3')
def func4():
    entry.insert(len(entry.get()),'4')
def func5():
    entry.insert(len(entry.get()),'5')
def func6():
    entry.insert(len(entry.get()),'6')
def func7():
    entry.insert(len(entry.get()),'7')
def func8():
    entry.insert(len(entry.get()),'8')
def func9():
    entry.insert(len(entry.get()),'9')
def funcplus():
    entry.insert(len(entry.get()),'+')
def funcmin():
    entry.insert(len(entry.get()),'-')
def funcequal():
    result=str(eval(entry.get()))
    value=str(entry.get())
    entry.delete(0,len(entry.get()))
    entry.insert(0,result)
    label.config(text=value+'='+result)
def funcmulti():
    entry.insert(len(entry.get()),'*')
def funcdivision():
    entry.insert(len(entry.get()),'/')


label = tk.Label(window,text='0',width=20,relief='solid')
label.grid(row=1,column=0,columnspan=4)

btnwidth=4
btnheight=1



btn7=tk.Button(window,text='7',command=func7,width=btnwidth)
btn7.grid(row=2,column=0)

btn8=tk.Button(window,text='8',command=func8,width=btnwidth)
btn8.grid(row=2,column=1)

btn9=tk.Button(window,text='9',command=func9,width=btnwidth)
btn9.grid(row=2,column=2)

btnplus=tk.Button(window,text='+',command=funcplus,width=btnwidth)
btnplus.grid(row=2,column=3)




btn4=tk.Button(window,text='4',command=func4,width=btnwidth)
btn4.grid(row=3,column=0)

btn5=tk.Button(window,text='5',command=func5,width=btnwidth)
btn5.grid(row=3,column=1)

btn6=tk.Button(window,text='6',command=func6,width=btnwidth)
btn6.grid(row=3,column=2)

btnmin=tk.Button(window,text='-',command=funcmin,width=btnwidth)
btnmin.grid(row=3,column=3)



btn1=tk.Button(window,text='1',command=func1,width=btnwidth)
btn1.grid(row=4,column=0)

btn2=tk.Button(window,text='2',command=func2,width=btnwidth)
btn2.grid(row=4,column=1)

btn3=tk.Button(window,text='3',command=func3,width=btnwidth)
btn3.grid(row=4,column=2)

btnmulti=tk.Button(window,text='*',command=funcmulti,width=btnwidth)
btnmulti.grid(row=4,column=3)

btnc=tk.Button(window,text='C',command=funcClear,width=btnwidth)
btnc.grid(row=5,column=0)


btn0=tk.Button(window,text='0',command=func0,width=btnwidth)
btn0.grid(row=5,column=1)

btnequal=tk.Button(window,text='=',command=funcequal,width=btnwidth)
btnequal.grid(row=5,column=2)

btndivi=tk.Button(window,text='/',command=funcdivision,width=btnwidth)
btndivi.grid(row=5,column=3)

window.mainloop()