from tkinter import*
import random
root=Tk()
root.geometry("400x400")
root.title("ASCII CONVERTER")
label1=Label(root,text="")
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
label2=Label(root, text="")
label2.place(relx= 0.5, rely=0.7, anchor=CENTER)
eeeee=["bottle","pencil","rock","paper","scissors"]
def pickitems():
    items=random.randint(0,4)
    label1["text"]=eeeee
    label2["text"]=eeeee[items]
button1=Button(root,text="WHAT ITEM SHOULD I PICK!!!111!!11!!",command=pickitems)
button1.place(relx=0.5, rely=0.8, anchor=CENTER)




root.mainloop()