import tkinter as tk


window = tk.Tk()
window.title('My App')
window.geometry("640x400+300+100")#가로x세로+x좌표+y좌표
window.resizable(False,False)



label = tk.Label(window,text='파이썬',width=10,height=5,fg='red',relief='solid',bg='blue')
label.pack()



window.mainloop()