import tkinter as tk


window = tk.Tk()
window.title('My App')
window.geometry("640x400+300+100")#가로x세로+x좌표+y좌표
window.resizable(False,False)
count=0
def countUP():
    global count
    count += 1
    label.config(text=str(count))
def countDOWN():
    global count
    count -= 1
    label.config(text=str(count))

def countdiv():
    global count
    count = count/2
    label.config(text=str(count))
def countmulti():
    global count
    count = count*2
    label.config(text=str(count))
def countclear():
    global count
    count=0
    label.config(text=str(count))

label = tk.Label(window,text='0',width=20,relief='solid')
label.pack()

btn = tk.Button(window,overrelief='solid',width=15,command=countUP,repeatdelay=1000,repeatinterval=100,text='+')
btn.pack()
btn2 = tk.Button(window,overrelief='solid',width=15,command=countDOWN,repeatdelay=1000,repeatinterval=100,text='-')
btn2.pack()
btn3 = tk.Button(window,overrelief='solid',width=15,command=countdiv,repeatdelay=1000,repeatinterval=100,text='/')
btn3.pack()
btn4 = tk.Button(window,overrelief='solid',width=15,command=countmulti,repeatdelay=1000,repeatinterval=100,text='*')
btn4.pack()
btn5 = tk.Button(window,overrelief='solid',width=15,command=countclear,repeatdelay=1000,repeatinterval=100,text='clear')
btn5.pack()

window.mainloop()