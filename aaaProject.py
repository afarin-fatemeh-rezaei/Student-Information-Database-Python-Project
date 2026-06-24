from tkinter import Tk,Label,Button,PhotoImage,PhotoImage # Importing necessary Libraries. 
from tkinter import *
import aaProject_C_F as f #Imporing Classes and functions.

t=Tk() #Setting up the main window.
t.geometry("500x500")
t.title("Student Information Database")
t.configure(bg="#F0FFF0")
t.resizable(width=False, height=False)

icon="logo.png"  #Adding the icon and making a failsafe for it.
if icon:
        try:
           img=PhotoImage(file=icon) 
           t.iconphoto(False,img)
        except:
            pass
else:
        pass

Label(t,text="Student Information Database",fg="#C71585", bg="#F0FFF0",font=("arial",20)).place(x=60,y=0) #Needed Labels.
Label(t,text="Menu", fg="#006400", bg="#F0FFF0",font=("arial",18)).place(x=5,y=70)


Button(t, text="1. See the list of students", font=("arial",14), fg="#0000CD", bg='#F0FFF0',  borderwidth=0, activebackground='#F0FFF0',command=f.creat1).place(x=0,y=120) #Button to call create1 to pen a new window.
Button(t, text="2. Add a student", font=("arial",14), fg="#0000CD", bg='#F0FFF0',  borderwidth=0, activebackground='#F0FFF0',command=f.creat2).place(x=0,y=180) #Button to call create2 to pen a new window.
Button(t, text="3. Remove a student", font=("arial",14), fg="#0000CD", bg='#F0FFF0',  borderwidth=0, activebackground='#F0FFF0',command=f.creat3).place(x=0,y=240) #Button to call create3 to pen a new window.
Button(t, text="4. Change a student's info", font=("arial",14), fg="#0000CD", bg='#F0FFF0',  borderwidth=0, activebackground='#F0FFF0',command=f.creat4).place(x=0,y=300) #Button to call create4 to pen a new window.
Button(t, text="5. See the student's information on plot", fg="#0000CD", font=("arial",14), bg='#F0FFF0',  borderwidth=0, activebackground='#F0FFF0',command=f.creat5).place(x=0,y=360) #Button to call create5 to pen a new window.

t.mainloop()
