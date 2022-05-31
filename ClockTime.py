
# Digital clock with dd/mm/yyyy using TKinter

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')
root.geometry('377x285')

def time():
    d = strftime('%d - %B - %Y')                                                        # %I --> Indian Format hour, %M --> minute, %S --> second, %p --> am/pm
    label0.config(text=d)                                                                   # Configured to show only the string which in case is the time
    
    w = strftime('<< %A >>')
    label1.config(text=w)
    
    t = strftime('\n%I:%M:%S %p')
    label2.config(text=t)
    label2.after(200, time)                                                                # Iterates after 1000ms (1sec) and loops time()

label0 = Label(root, font=('times', 36), background='black', foreground='yellow')
label0.pack(anchor='center', fill='x')
label1 = Label(root, font=('times', 40), background='black', foreground='orange')
label1.pack(anchor='center', fill='x')
label2 = Label(root, font=('ds-digital', 61), background='black', foreground='cyan')
label2.pack(anchor='center', fill='x')
time()

mainloop()