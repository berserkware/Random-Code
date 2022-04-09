from tkinter import *
import time
import tkinter.font as tkFont


one = False
two = False
three = False
four = False

root = Tk()
root['bg'] = "#2f3540"

root.title("SmortOS")
root.geometry('480x320')

fontStyle = tkFont.Font(family="Arial", size=20)

tab1 = Label(root, text=" APPS ", fg="#2f3540", bg= "#17b000", font=fontStyle)
tab2 = Label(root, text=" GAMES ", fg="#17b000", bg= "#2f3540", font=fontStyle)
tab3 = Label(root, text=" TIME ", fg="#17b000", bg= "#2f3540", font=fontStyle)
tab4 = Label(root, text=" SETTINGS ", fg="#17b000", bg= "#2f3540", font=fontStyle)

apps = ["calculator", "notepad", "photos", "music", "maps"]

games = ["Click-a-Nut", "Break Out", "Cheeky Kiwi", "Street Fighter"]

a = [Label] * len(apps)
b = [Label] * len(games)

def Apps():
    for x in range(len(apps)):
        if(one == False):
            a[x] = Label(root, text=apps[x])
            a[x].config(bg = "#2f3540", fg = "#17b000")
            a[x].grid(column=0, row=x + 1)




Apps()

def Games():
    for x in range(len(games)):
        if(one == False):
            b[x] = Label(root, text=games[x])
            b[x].config(bg = "#2f3540", fg = "#17b000")
            b[x].grid(column=0, row=x + 1)


    for x in range(len(a)):
        a[x].destroy()
def Time():
    for x in range(len(a)):
        a[x].destroy()

    for x in range(len(b)):
        b[x].destroy()
        
def Settings():
    for x in range(len(a)):
        a[x].destroy()

    for x in range(len(b)):
        b[x].destroy()    
    

def AP(event):
    tab1.config(fg="#2f3540", bg= "#17b000")
    tab2.config(fg="#17b000", bg= "#2f3540")
    tab3.config(fg="#17b000", bg= "#2f3540")
    tab4.config(fg="#17b000", bg= "#2f3540")
    Apps()
    one = True
    two = False
    three = False
    four = False
def SP(event):
    tab2.config(fg="#2f3540", bg= "#17b000")
    tab1.config(fg="#17b000", bg= "#2f3540")
    tab3.config(fg="#17b000", bg= "#2f3540")
    tab4.config(fg="#17b000", bg= "#2f3540")
    Games()
    one = False
    two = True
    three = False
    four = False
def DP(event):
    tab3.config(fg="#2f3540", bg= "#17b000")
    tab2.config(fg="#17b000", bg= "#2f3540")
    tab1.config(fg="#17b000", bg= "#2f3540")
    tab4.config(fg="#17b000", bg= "#2f3540")
    Time()
    one = False
    two = False
    three = True
    four = False
def FP(event):
    tab4.config(fg="#2f3540", bg= "#17b000")
    tab2.config(fg="#17b000", bg= "#2f3540")
    tab3.config(fg="#17b000", bg= "#2f3540")
    tab1.config(fg="#17b000", bg= "#2f3540")
    Settings()
    one = False
    two = False
    three = False
    four = True

root.bind("a",AP)
root.bind("s",SP)
root.bind("d",DP)
root.bind("f",FP)

tab1.grid(column=0, row=0)
tab2.grid(column=1, row=0)
tab3.grid(column=2, row=0)
tab4.grid(column=3, row=0)

root.mainloop()