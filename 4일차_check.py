import tkinter as tk
import math
from math import *
window = tk.Tk()
window.title('My App')
window.geometry("360x280+300+100")#가로x세로+x좌표+y좌표
window.resizable(False,False)
entry = tk.Entry(window)



def func1():
    
    result=0
    if cv1.get()==1:
        result +=1200
    if cv2.get()==1:
        result +=1000
    
    label['text']='가격 : '+str(result)+'원'
    result+=1500
    label.text='가격:'+str(result)+''



cv1=tk.IntVar()
checkbutton1=tk.Checkbutton(window,text='컵라면',variable=cv1,command=func1)

cv2=tk.IntVar()
checkbutton2=tk.Checkbutton(window,text='삼각김밥',variable=cv2,command=func1)

label=tk.Label(window,text='가격 : 0원')

img1=tk.PhotoImage(file='img\컵라면.png').subsample(2)
label_img1=tk.Label(window,image=img1)

img2=tk.PhotoImage(file='img\삼김.png').subsample(1)
label_img2=tk.Label(window,image=img2)



label_img1.grid(row=0,column=0)
checkbutton1.grid(row=1,column=0)
label_img2.grid(row=0,column=1)
checkbutton2.grid(row=1,column=1)
label.grid(row=2,column=0,columnspan=2)






window.mainloop()