#Ra7oox

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("counter of words")
root.geometry("400x400")

label1=Label(root,text="enter a sentence")
label1.place(x=140,y=50)

input=Entry(root)
input.place(x=120,y=80)
def count():
    list_words=input.get().split(" ")
    
    messagebox.showinfo("words",f'the number of words is : {len(list_words)}')
    root.destroy()
    
button=Button(root,command=count,text="count",bg="green",border=0)
button.place(x=160,y=120)


root.mainloop()