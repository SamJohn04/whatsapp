from tkinter import *
from pywhatkit import *
import time

root=Tk()
frame=Frame(root,width=600,height=500,padx=50,pady=50)
frame.pack()
t=time.localtime()

recilist=[]
reciglist=[]

def getList():
    recilist.clear()
    reciglist.clear()
    fn=open("numbers.txt","r")
    for no in fn:
        recilist.append(no)
    fg=open("groups.txt","r")
    for gp in fg:
        reciglist.append(gp)
    fn.close()
    fg.close()

def readList():
    read=Tk()
    reci=[]
    recig=[]
    e=Entry(read,width=15)
    e.grid(row=0,column=0,columnspan=3)
    def asN():
        reci.append(e.get())
        e.delete(0,END)
    def asG():
        recig.append(e.get())
        e.delete(0,END)
    addN=Button(read,text="Add as Number.",command=asN)
    addN.grid(row=1,column=0)
    addG=Button(read,text="Add as Group.",command=asG)
    addG.grid(row=1,column=2)
    read.mainloop()
    fn=open("numbers.txt","a")
    for n in reci:
        fn.write('\n')
        fn.write(n)
    fn.close()
    fg=open("groups.txt","a")
    for g in recig:
        fg.write('\n')
        fg.write(g)
    fg.close()
def greetbytime():
    getList()
    for n in recilist:
        if t.tm_hour<=10:
            sendwhatmsg_instantly(n, 'Good Morning!',4,True,2)
        elif t.tm_hour<13:
            sendwhatmsg_instantly(n,'Good Day!',4,True,2)
        elif t.tm_hour<17:
            sendwhatmsg_instantly(n,'Good Afternoon!',4,True,2)
        else:
            sendwhatmsg_instantly(n,'Good Evening!',4,True,2)
    for g in reciglist:
        if t.tm_hour<=10:
            sendwhatmsg_to_group_instantly(g, 'Good Morning!',4,True,2)
        elif t.tm_hour<13:
            sendwhatmsg_to_group_instantly(g,'Good Day!',4,True,2)
        elif t.tm_hour<17:
            sendwhatmsg_to_group_instantly(g,'Good Afternoon!',4,True,2)
        else:
            sendwhatmsg_to_group_instantly(g,'Good Evening!',4,True,2)

def justGreet():
    getList()
    for n in recilist:
        sendwhatmsg_instantly(n,'Hello!!',4,True,2)
    for g in reciglist:
        sendwhatmsg_to_group_instantly(g, 'Hello!',4,True,2)

def somethingElse():
    getList()
    read=Tk()
    e=Entry(read,width=15)
    e.grid(row=0,column=0,columnspan=3)
    def proceed():
        x=e.get()
        for n in recilist:
            sendwhatmsg_instantly(n,x,4,True,2)
        for g in reciglist:
            sendwhatmsg_to_group_instantly(g, x,4,True,2)
        e.delete(0,END)

    oke=Button(read,text="Ok!",command=proceed)
    oke.grid(row=1,column=1)
    read.mainloop()
add=Button(frame,text="Add Numbers and Groups.",command=readList)
add.grid(row=0,column=1)
gbt=Button(frame,text="Greet everyone based on Time",command=greetbytime)
gbt.grid(row=1,column=0)
jg=Button(frame,text="Just Greet 'Em!",command=justGreet)
jg.grid(row=1,column=1)
se=Button(frame,text="Send smthn else",command=somethingElse)
se.grid(row=1,column=2)
root.mainloop()
