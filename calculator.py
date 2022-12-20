from dataclasses import replace
import string
from tkinter import *
from tokenize import String

root=Tk()
root.title("Calculator")
root.geometry("280x300")
root.iconbitmap(".\Calculator.ico")
root.configure(bg="grey")
scvalue= StringVar()
scvalue.set("")
frame1=Frame(root, bg="#383838")
frame1.pack()
screen=Entry(frame1, textvariable=scvalue, font="Lucida 25 bold", borderwidth=5, justify='right', bg="#282828", foreground="white" )
screen.pack(fill=X, pady=10, padx=10, ipady=5, ipadx=2 )

def symbolChange(string):
    list=[]
    list[:0]=scvalue.get()
    print(list)
    print(list[-1])
    if list[-1]=="+":
        list.remove(list[-1])
        list.append(string)
        tempString=""
        for i in list:
            tempString+=i
        print(tempString)
        scvalue.set(tempString)
    elif list[-1]=="-":
        list.remove(list[-1])
        list.append(string)
        tempString=""
        for i in list:
            tempString+=i
        print(tempString)
        scvalue.set(tempString)
    elif list[-1]=="*":
        list.remove(list[-1])
        list.append(string)
        tempString=""
        for i in list:
            tempString+=i
        print(tempString)
        scvalue.set(tempString)
    elif list[-1]=="/":
        list.remove(list[-1])
        list.append(string)
        tempString=""
        for i in list:
            tempString+=i
        print(tempString)
        scvalue.set(tempString)
    else:
        scvalue.set(scvalue.get() + string)
    

# def noRepeatation(string):
#     list=[]
#     list[:0]=scvalue.get()
#     if not list[-1]==string:
#         scvalue.set(scvalue.get() + string)

def click(event):
    text=event.widget.cget("text")    #to take text from any string
    
    if text=="C":
        scvalue.set("")
    elif text=="=":
        try:
            if "**" in scvalue.get():
                scvalue.set("ERROR")
                screen.upadate()
            scvalue.set(eval(scvalue.get()))    
        except Exception as e:
            scvalue.set("INFINITY")  
    elif text=="9":
        scvalue.set(scvalue.get() + "9")
    elif text=="8":
        scvalue.set(scvalue.get() + "8")
    elif text=="7":
        scvalue.set(scvalue.get() + "7")
    elif text=="6":
        scvalue.set(scvalue.get() + "6")
    elif text=="5":
        scvalue.set(scvalue.get() + "5")
    elif text=="4":
        scvalue.set(scvalue.get() + "4")
    elif text=="3":
        scvalue.set(scvalue.get() + "3")
    elif text=="2":
        scvalue.set(scvalue.get() + "2")
    elif text=="1":
        scvalue.set(scvalue.get() + "1")
    elif text=="0":
        scvalue.set(scvalue.get() + "0")
    elif text=="+":
        #noRepeatation("+")
        symbolChange("+")
    elif text=="-":
        #noRepeatation("-")
        symbolChange("-")
    elif text=="*":
        #noRepeatation("*")
        symbolChange("*")
    elif text=="/":
        #noRepeatation("/")
        symbolChange("/")
    elif text==".":
        scvalue.set(scvalue.get() + ".")

screen.update()

frame=Frame(root, bg="#282828", padx=10)

b=Button(frame, text="9", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES,  )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="8", font="Lucida 15 bold",padx=20, bg="black", foreground="white")
b.pack(side=LEFT, fill=BOTH, expand=YES,  )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="7", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT, fill=BOTH, expand=YES,  )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="+", font="Lucida 15 bold",padx=20, bg="#202020", foreground="white" )
b.pack(side=LEFT, fill=BOTH, expand=YES, padx=2  )
b.bind("<ButtonRelease-1>", click)
frame.pack(fill=BOTH, expand=YES)

frame=Frame(root, bg="#282828", padx=10)

b=Button(frame, text="6", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="5", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="4", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="-", font="Lucida 15 bold",padx=20, bg="#202020", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES, padx=2 )
b.bind("<ButtonRelease-1>", click)
frame.pack(fill=BOTH, expand=YES)

frame=Frame(root, bg="#282828", padx=10)

b=Button(frame, text="3", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="2", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="1", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="*", font="Lucida 15 bold",padx=20, bg="#202020", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES, padx=2 )
b.bind("<ButtonRelease-1>", click)
frame.pack(fill=BOTH, expand=YES)

frame=Frame(root, bg="#282828", padx=10)
b=Button(frame, text="C", font="Lucida 15 bold",padx=18.5, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="0", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text=".", font="Lucida 15 bold",padx=20, bg="black", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES )
b.bind("<ButtonRelease-1>", click)
b=Button(frame, text="/", font="Lucida 15 bold",padx=20, bg="#202020", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES, padx=2 )
b.bind("<ButtonRelease-1>", click)
frame.pack(fill=BOTH, expand=YES, )

frame=Frame(root, bg="#282828", padx=10)
b=Button(frame, text="=", font="Lucida 15 bold",padx=20, bg="#202020", foreground="white" )
b.pack(side=LEFT,fill=BOTH, expand=YES, padx=2 )
b.bind("<ButtonRelease-1>", click)
frame.pack(fill=BOTH, expand=YES, pady=1)



root.mainloop()



