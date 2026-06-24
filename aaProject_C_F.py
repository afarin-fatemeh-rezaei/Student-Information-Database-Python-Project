from tkinter import Label,Entry,Button,Toplevel,ttk,Canvas,PhotoImage  # Importing necessary Libraries. 
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

with open('Number.txt',"a+") as f:    #To create and open my txt data files.  
               f.write(f"")
               
with open('Name.txt',"a+") as f:
               f.write(f"")
            
with open('Year.txt',"a+") as f:
               f.write(f"")
            
with open('Midterm.txt',"a+") as f:
               f.write(f"")
              
with open('Final.txt',"a+") as f:
               f.write(f"")


def number():      #To open and read my files except the first line.
       with open('Number.txt', 'r') as f:
         f.readline()
         c=f.read()
         return(c)
       
def name():
       with open('Name.txt', 'r') as f:
         f.readline()
         c=f.read()
         return(c)
      
def year():
      with open('Year.txt', 'r') as f:
         f.readline()
         c=f.read()
         return(c)
      
def midterm():
       with open('Midterm.txt', 'r') as f:
         f.readline()
         c=f.read()
         return(c)

def final():
       with open('Final.txt', 'r') as f:
         f.readline()
         c=f.read()
         return(c)
       
numberaa=number() #Calling functions in the begining of the code to open and read files except the first line.
nameaa=name()
yearaa=year()
midtermaa=midterm()
finalaa=final()

def error2():     #Used for creating a pop-up when the correct data was not entered.
   
       err=Toplevel()
       err.title("Error")
       err.geometry("250x110")
       err.resizable(width=False, height=False)
       err.configure(bg="#F0FFF0")
       icon="logo.png"
       if icon:
        try:
           img=PhotoImage(file=icon) 
           err.iconphoto(False,img)
        except:
            pass
       else:
        pass
       Label(err, text="Please enter the \ncorrect from for each data.",fg="#C71585", bg="#F0FFF0",font=("arial")).place(x=25,y=25)
       err.mainloop()       

def getitem(olist,indexes):#To search with indexes in a list and return their value.
       if olist is None or indexes  is None:
           error2()
       else: 
        items="".join([olist[i] for i in indexes])
        return items
    

class FileToList:      #Used for reading a file and adding its contents to a list of strings.
      def __init__ (self,filename):
             self.filename=filename
             self.lines=[]
      def converttolist(self):
         with open(self.filename,"r") as f:
            f.readline()
            self.lines=[line.strip() for line in f]
      def getline(self):
         return self.lines
      
class TxttoFloatList:   #Used for reading a file and turning its conntent from string to float then adding its contents to a list.
     def __init__(self,filename):
      self.filename=filename
      self.floatlist=[]
     def readfloat(self):
       with open(self.filename,"r") as f:
          f.readline()
          for line in f:
             try:
                self.floatlist.append(float(line.strip()))
             except ValueError:
                continue
     def getfloat(self):
       return self.floatlist
     
class ListSearch:    #Serches an entry in a list and returns its index in a list. If the item doesn't exist it shows an error text.
       def __init__(self,lst):
         self.lst=lst
       def findindex(self,item,t):
          if  item in self.lst:
           index=[index for index, value in enumerate(self.lst) if value==item]
           return index 
          else:
             Label(t, text="This name\ndoesn't exist.",  bg='#F0FFF0', fg="red", font=("arial",12)).place(x=380,y=65)

                  

sn=FileToList("Number.txt")   #Calling Class FileToList to read the files and add them in string form to a list.
sn.converttolist() 
ssn=sn.getline()
a=FileToList("Name.txt")
a.converttolist() 
b=a.getline()
c=FileToList("year.txt")
c.converttolist()
d=c.getline()
e=FileToList("Midterm.txt")
e.converttolist()
f=e.getline()
g=FileToList("Final.txt")
g.converttolist()
h=g.getline()
       



def creat1(): #Command for the first menu button to open a new window.
    t1=Toplevel()
    t1.geometry("500x500")
    t1.title("See the list of students")
    t1.configure()
    t1.resizable(width=False, height=False)

    numberaa=number() #Calling functions in the begining of the code to open and read files except the first line.
    nameaa=name()
    yearaa=year()
    midtermaa=midterm()
    finalaa=final()

    sn=FileToList("Number.txt")   #Calling Class FileToList to read the files and add them in string form to a list.
    sn.converttolist() 
    ssn=sn.getline()
    a=FileToList("Name.txt")
    a.converttolist() 
    b=a.getline()
    c=FileToList("year.txt")
    c.converttolist()
    d=c.getline()
    e=FileToList("Midterm.txt")
    e.converttolist()
    f=e.getline()
    g=FileToList("Final.txt")
    g.converttolist()
    h=g.getline()

    icon="logo.png"  #Adding the icon and making a failsafe for it.
    if icon:
        try:
           img=PhotoImage(file=icon) 
           t1.iconphoto(False,img)
        except:
            pass
    else:
        pass

    cnvs=Canvas(t1, width=500, height=500, bg="#F0FFF0") #Using Canvas for creating lines.
    cnvs.pack()
    cnvs.create_line(80,60,80,500, fill="black", width=2)
    cnvs.create_line(253,60,253,500, fill="black", width=2)
    cnvs.create_line(358,60,358,500, fill="black", width=2)
    cnvs.create_line(443,60,443,500, fill="black", width=2)

    Label(t1,text="List of students",fg="#C71585", bg='#F0FFF0', font=("arial",20)).place(x=150,y=5) #Labels for each section.
    Label(t1,text="Number",fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=5,y=60)
    Label(t1,text="Name",fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=85,y=60)
    Label(t1,text="Entry Year",fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=258,y=60)
    Label(t1,text="Midterm",fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=363,y=60)
    Label(t1,text="Final",fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=448,y=60)

    Label(t1,text=numberaa,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=5,y=100) #Labels to write the previously opend files.
    Label(t1,text=nameaa,fg="#0000CD", bg='#F0FFF0', font=("arial",12)).place(x=85,y=100)
    Label(t1,text=yearaa,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=258,y=100)
    Label(t1,text=midtermaa,fg="#0000CD", bg='#F0FFF0', font=("arial",12)).place(x=363,y=100)
    Label(t1,text=finalaa,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=448,y=100)

    t1.mainloop()






def creat2(): #Command for the second menu button to open a new window.
    t2=Toplevel()
    t2.geometry("500x500")
    t2.title("Add a student")
    t2.configure(bg="#F0FFF0")
    t2.resizable(width=False, height=False)
    
    numberaa=number() #Calling functions in the begining of the code to open and read files except the first line.
    nameaa=name()
    yearaa=year()
    midtermaa=midterm()
    finalaa=final()
   
    sn=FileToList("Number.txt")   #Calling Class FileToList to read the files and add them in string form to a list.
    sn.converttolist() 
    ssn=sn.getline()
    a=FileToList("Name.txt")
    a.converttolist() 
    b=a.getline()
    c=FileToList("year.txt")
    c.converttolist()
    d=c.getline()
    e=FileToList("Midterm.txt")
    e.converttolist()
    f=e.getline()
    g=FileToList("Final.txt")
    g.converttolist()
    h=g.getline()

    icon="logo.png"   #Adding the icon and making a failsafe for it. 
    if icon:
        try:
           img=PhotoImage(file=icon) 
           t2.iconphoto(False,img)
        except:
            pass
    else:
        pass

    Label(t2, text="Add a student",fg="#C71585", bg="#F0FFF0",font=("arial",20,)).place(x=150,y=0)  # Labels for Entries. 
    Label(t2, text="Number:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=100)
    Label(t2, text="Name:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=160)
    Label(t2, text="Entry Year:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=220)
    Label(t2, text="Midterm:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=280)
    Label(t2, text="Final:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=340)

    sn2=Entry(t2)     #Adding adequate Entries.
    sn2.place(x=130,y=105)
    a2=Entry(t2)
    a2.place(x=130,y=165)
    b2=Entry(t2)
    b2.place(x=130,y=225)
    c2=Entry(t2)
    c2.place(x=130,y=285)
    d2=Entry(t2)
    d2.place(x=130,y=345)
    
       
    def submit(): #Command for Button to save the entered data in each Entry.
     sn22=sn2.get()   
     bb=b2.get()      #Getting the entered value for each entry.
     cc=c2.get()
     dd=d2.get()
     try:      #Turning the needed values to float. if the values cannot be turned to float, failsafe is error2
      ccc=float(cc)    
      ddd=float(dd)
      sn222=float(sn22)
     except: error2()
     cccc=str(int(ccc))   #Turning the previous floats to string.
     dddd=str(int(ddd))
     sn2222=str(int(sn222))
     ra=np.arange(0,20.01 , 0.01) #Range for midten and final Entry.
     if bb and cc and dd and ccc in ra and  ddd in ra:    # If midterm, final, and year entry is in range; getting conformation from user then saving it. If not show the pop-up error2.
         if bb.isdigit() and int(bb) in range(1350,1430) and cccc.isdigit() and dddd.isdigit() and sn2222.isdigit():
          
             qw=Toplevel()  #Creating conformation pop-up.
             qw.title("Are you sure?")
             qw.geometry("250x110")
             qw.resizable(width=False, height=False)
             qw.configure(bg="#F0FFF0")
             qw.iconphoto(False,img)
             Label(qw, text="Are you sure you want to Submit?",fg="#C71585", bg="#F0FFF0",font=("arial")).place(x=5,y=5)
     
    
             def submit2():   #Command for conformation pop-up yes button to add the entered values to the end of each file.
              with open('Number.txt',"a+") as f:
               f.write(f"\n{sn2.get()}")
               sn2.delete(0, END)

              with open('Name.txt',"a+") as f:
               f.write(f"\n{a2.get()}")
               a2.delete(0, END)
 
              with open('Year.txt',"a+") as f:
               f.write(f"\n{b2.get()}")
               b2.delete(0, END)

              with open('Midterm.txt',"a+") as f:
               f.write(f"\n{c2.get()}")
               c2.delete(0, END)

              with open('Final.txt',"a+") as f:
               f.write(f"\n{d2.get()}")
               d2.delete(0, END) #Removing the typed value in Entries.
               qw.destroy() #Kill the pop-up.
     

             Button(qw, text="Yes", command=submit2, bg='#00BFFF', activebackground='#0000CD').place(x=60,y=50) #Pop-up Buttons to call submit2.
             Button(qw, text="No", command=qw.destroy, bg='#00BFFF', activebackground='#0000CD').place(x=150,y=50)  #Kills the pop-up.
             qw.mainloop()
          
         else:
             error2() #Failsafe pop-up error2
             
     else:
          error2() #Failsafe pop-up error2
          
 
    Button(t2, text="Add",command=submit, bg='#9ACD32', activebackground='#006400',font=("arial"), width=20).place(x=5,y=410) #Button to call submit.

    t2.mainloop()
    

    

       
  
 
def creat3(): #Command for the third menu button to open a new window.
   t3=Toplevel()
   t3.geometry("500x500")
   t3.title("Remove a student")
   t3.configure(bg="#F0FFF0")
   t3.resizable(width=False, height=False)

   numberaa=number() #Calling functions in the begining of the code to open and read files except the first line.
   nameaa=name()
   yearaa=year()
   midtermaa=midterm()
   finalaa=final()
   
   sn=FileToList("Number.txt")   #Calling Class FileToList to read the files and add them in string form to a list.
   sn.converttolist() 
   ssn=sn.getline()
   a=FileToList("Name.txt")
   a.converttolist() 
   b=a.getline()
   c=FileToList("year.txt")
   c.converttolist()
   d=c.getline()
   e=FileToList("Midterm.txt")
   e.converttolist()
   f=e.getline()
   g=FileToList("Final.txt")
   g.converttolist()
   h=g.getline()

   icon="logo.png"  #Adding the icon and making a failsafe for it.
   if icon:
        try:
           img=PhotoImage(file=icon) 
           t3.iconphoto(False,img)
        except:
            pass
   else:
        pass
   
   def submit3():    #Command for search button to search a student with their name and show the result. If not show an error text.
      ss=str(aa.get())   #Turning the Entery's entry value to string.
      sercher1=ListSearch(ssn)  #Calling List search class to search the entry and return its index in a list.
      serchitem=(ss)
      index1=sercher1.findindex(serchitem,t3) 
      mm11=getitem(ssn,index1)  #Calling the getitem function to search the values coresponding with the name searched in Entry.
      mm1=getitem(b,index1)
      mm2=getitem(d,index1)
      mm3=getitem(f,index1)
      mm4=getitem(h,index1)

      cnvs=Canvas(t3, width=500, height=60, bg="#F0FFF0", highlightbackground="#F0FFF0", highlightthickness=2, bd=2)  #Using Canvas for creating lines.
      cnvs.create_line(80,0,80,60, fill="black", width=1)
      cnvs.create_line(253,0,253,60, fill="black", width=1)
      cnvs.create_line(358,0,358,60, fill="black", width=1)
      cnvs.create_line(443,0,443,60, fill="black", width=1)
      cnvs.place(x=0,y=135)

      Label(t3,text="Number",fg="#800000", bg='#F0FFF0', font=("arial",14)).place(x=5,y=140) #Labels for each section.
      Label(t3,text="Name",fg="#800000", bg='#F0FFF0', font=("arial",14)).place(x=85,y=140)
      Label(t3,text="Entry Year",fg="#800000", bg='#F0FFF0', font=("arial",14)).place(x=258,y=140)
      Label(t3,text="Midterm",fg="#800000", bg='#F0FFF0', font=("arial",14)).place(x=363,y=140)
      Label(t3,text="Final",fg="#800000", bg='#F0FFF0', font=("arial",14)).place(x=448,y=140)
      Label(t3,text=mm11,fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=5,y=170)  #Labels to write the previously found values.
      Label(t3,text=mm1,fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=85,y=170)
      Label(t3,text=mm2,fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=258,y=170)
      Label(t3,text=mm3,fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=363,y=170)
      Label(t3,text=mm4,fg="#006400", bg='#F0FFF0', font=("arial",14)).place(x=448,y=170)
      Label(t3,text="                               \n                          ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=380,y=65) #Label to hide the error text.
      

   
   def delete():  #Command for remove button to create a conformation pop-up.
      qw=Toplevel()
      qw.title("Are you sure?")
      qw.geometry("250x110")
      qw.resizable(width=False, height=False)
      qw.configure(bg="#F0FFF0")

      icon="logo.png"  #Adding the icon and making a failsafe for it.
      if icon:
        try:
           img=PhotoImage(file=icon) 
           qw.iconphoto(False,img)
        except:
            pass
      else:
        pass
   
      Label(qw, text="Are you sure you want to delete?",fg="#C71585", bg="#F0FFF0",font=("arial")).place(x=5,y=5) #Adequate label.
      

      def del3 ():  #Command for conformation pop-up yes button in conformation pop-up to delete the value entered in entry by adding the files values to individual lists, deleteing the value then, rewriting them in each file.
       ss=str(aa.get()) #Turning the Entery's entry value to string.
      
       sercher1=ListSearch(ssn)  #Calling List search class to search the entry and return its index in a list.
       serchitem=(ss)
       index1=sercher1.findindex(serchitem,t3) 
    
       int_result = int(''.join(map(str, index1))) #Turning the index list to a int.

       del b[int_result] #Deleting the items based on the index of searched item.
       del d[int_result]
       del f[int_result]
       del h[int_result]
       del ssn[int_result]

       with open('Name.txt',"w+") as ff:  #Rewriting the files after removal.
                for item in b:
                 ff.write(f"\n{item}")

       with open('Year.txt',"w+") as ff:
                for item in d:
                 ff.write(f"\n{item}")
            
       with open('Midterm.txt',"w+") as ff:
                for item in f:
                 ff.write(f"\n{item}")

       with open('Final.txt',"w+") as ff:
               for item in h:
                 ff.write(f"\n{item}")
       with open('Number.txt',"w+") as ff:
               for item in ssn:
                 ff.write(f"\n{item}")

       aa.delete(0, END) #Removing the typed value in Entry.
       qw.destroy() #Kill the pop-up.

       Label(t3,text="                                                                                                                                               ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=0,y=130)  #Labels to hide the search results.
       Label(t3,text="                                                                                                                                                ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=0,y=140)
       Label(t3,text="                                                                                                                                                ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=0,y=150)
       Label(t3,text="                                                                                                                                                 ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=0,y=160)
       Label(t3,text="                                                                                                                                                  ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=0,y=170)
       Label(t3,text="                                                                                                                                                   ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=0,y=180)
   
 
                 
      Button(qw, text="Yes", command=del3, bg='#00BFFF', activebackground='#0000CD').place(x=60,y=50)   #Button to call del3 and remove the items.
      Button(qw, text="No", command=qw.destroy, bg='#00BFFF', activebackground='#0000CD').place(x=150,y=50) #Kills the pop-up.
      
      qw.mainloop()

   aa=Entry(t3)
   aa.place(x=160,y=70)
   Label(t3,text="Remove a student",fg="#C71585", bg='#F0FFF0', font=("arial",20)).place(x=130,y=5) #Needed labels.
   Label(t3, text="Search number:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=65)
   Button(t3, text="Search",  bg='#9ACD32', activebackground='#0000CD', font=("arial"), command=submit3).place(x=300,y=65) #Button to call submit3.
   Button(t3, text="Remove", bg='#9ACD32', activebackground='#006400', font=("arial"), command=delete, width=20).place(x=5,y=300)  #Button to call delete.

   t3.mainloop()

    




def creat4(): #Command for the forth second menu button to open a new window.
   t4=Toplevel()
   t4.geometry("500x500")
   t4.title("Change a student's info")
   t4.configure(bg="#F0FFF0")
   t4.resizable(width=False, height=False)

   numberaa=number() #Calling functions in the begining of the code to open and read files except the first line.
   nameaa=name()
   yearaa=year()
   midtermaa=midterm()
   finalaa=final()
   
   sn=FileToList("Number.txt")   #Calling Class FileToList to read the files and add them in string form to a list.
   sn.converttolist() 
   ssn=sn.getline()
   a=FileToList("Name.txt")
   a.converttolist() 
   b=a.getline()
   c=FileToList("year.txt")
   c.converttolist()
   d=c.getline()
   e=FileToList("Midterm.txt")
   e.converttolist()
   f=e.getline()
   g=FileToList("Final.txt")
   g.converttolist()
   h=g.getline()

   icon="logo.png"   #Adding the icon and making a failsafe for it.
   if icon:
        try:
           img=PhotoImage(file=icon) 
           t4.iconphoto(False,img)
        except:
            pass
   else:
        pass

   def submit3():    #Command for search button to search a student with their name and show the result. if not show an error text.
      ss=str(aa.get())  #Turning the Entery's entry value to string.
      sercher1=ListSearch(ssn) #Calling List search class to search the entry and return its index in a list.
      serchitem=(ss)
      index1=sercher1.findindex(serchitem,t4)
      
      mm11=getitem(ssn,index1)  #Calling the getitem function to search the values coresponding with the name searched in Entry.
      mm1=getitem(b,index1)
      mm2=getitem(d,index1)
      mm3=getitem(f,index1)
      mm4=getitem(h,index1)

      cnvs=Canvas(t4, width=500, height=60, bg="#F0FFF0", highlightbackground="#F0FFF0", highlightthickness=2, bd=2)  #Using Canvas for creating lines.
      cnvs.create_line(80,0,80,60, fill="black", width=1)
      cnvs.create_line(253,0,253,60, fill="black", width=1)
      cnvs.create_line(358,0,358,60, fill="black", width=1)
      cnvs.create_line(443,0,443,60, fill="black", width=1)
      cnvs.place(x=0,y=105)

      Label(t4,text="Number",fg="#800000", bg='#F0FFF0', font=("arial",12)).place(x=5,y=110)  #Labels for each section.
      Label(t4,text="Name",fg="#800000", bg='#F0FFF0', font=("arial",12)).place(x=85,y=110)
      Label(t4,text="Entry Year",fg="#800000", bg='#F0FFF0', font=("arial",12)).place(x=258,y=110)
      Label(t4,text="Midterm",fg="#800000", bg='#F0FFF0', font=("arial",12)).place(x=363,y=110)
      Label(t4,text="Final",fg="#800000", bg='#F0FFF0', font=("arial",12)).place(x=448,y=110)
      Label(t4,text=mm11,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=5,y=140)  #Labels to write the previously found values.
      Label(t4,text=mm1,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=85,y=140)
      Label(t4,text=mm2,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=258,y=140)
      Label(t4,text=mm3,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=363,y=140)
      Label(t4,text=mm4,fg="#006400", bg='#F0FFF0', font=("arial",12)).place(x=448,y=140)
      Label(t4,text="                               \n                          ",fg='#F0FFF0', bg='#F0FFF0', font=("arial",12)).place(x=380,y=65)  #Label to hide the error text.


   def error(): #Command for Combobox that shoes an error text if no option is selected and the change button was pushed.
    rl=Label(t4, text="Choose an item.",font=("Arial",12),  bg='#F0FFF0', fg="red")
    rl.place(x=290,y=210)


   def oncomboboxselect(event): #command for Combobox to associate each option with a group of commands.
      selectedvalue=cm.get()  #Getting the Combobox's value and putting it in a variable.
      ss=str(aa.get()) #Turning the Entery's entry value to string.
      sercher1=ListSearch(ssn) #Calling List search class to search the entry and return its index in a list.
      serchitem=(ss) 
      index1=sercher1.findindex(serchitem,t4) 
      int_result = int(''.join(map(str, index1))) #Turning the index list to a int.


      Label(t4, text="                                        ",font=("Arial",12),  bg='#F0FFF0', fg="red").place(x=290,y=210) #labels to delete previous unnecessary Labels.
      Label(t4, text='            ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)

      av=0 #Defining arbitrary value to use for our if and Combobox result.
      if selectedvalue=="Name": #Conditions for each Combobox value. Value="Name"
            av=1
            Label(t4, text='                                                                                     ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=265) #To hide and change text.
            Label(t4, text='                                    ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            Label(t4, text="Change name:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            e2.place(x=140,y=290, width=100)
            e3.place(x=260,y=290, width=100)
            e4.place(x=380,y=290, width=100)
            e2.place_forget()
            e3.place_forget()
            e4.place_forget()
            
      elif selectedvalue=="Entry year": #Conditions for each Combobox value. Value="Entry year"
            av=2
            Label(t4, text='                                                                                          ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=265) #To hide and change text.
            Label(t4, text='                                    ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            Label(t4, text="Change entry year:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            e2.place(x=140,y=290, width=100) #If the Value="Change all the above" and the other 3 Entries were executed then you want to execute another option, it hides them.
            e3.place(x=260,y=290, width=100)
            e4.place(x=380,y=290, width=100)
            e2.place_forget()
            e3.place_forget()
            e4.place_forget()

      elif selectedvalue=="Midterm": #Conditions for each Combobox value. Value="Midterm"
            av=3
            Label(t4, text='                                                                                         ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=265) #To hide and change text.
            Label(t4, text='                                    ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            Label(t4, text="Change midterm:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            e2.place(x=140,y=290, width=100) #If the Value="Change all the above" and the other 3 Entries were executed then you want to execute another option, it hides them.
            e3.place(x=260,y=290, width=100)
            e4.place(x=380,y=290, width=100)
            e2.place_forget()
            e3.place_forget()
            e4.place_forget()
            
      elif selectedvalue=="Final": #Conditions for each Combobox value. Value="Final"
            av=4
            Label(t4, text='                                                                                           ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=265) #To hide and change text.
            Label(t4, text='                                    ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            Label(t4, text="Change final:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            e2.place(x=140,y=290, width=100) #If the Value="Change all the above" and the other 3 Entries were executed then you want to execute another option, it hides them.
            e3.place(x=260,y=290, width=100)
            e4.place(x=380,y=290, width=100)
            e2.place_forget()
            e3.place_forget()
            e4.place_forget()
            
      elif selectedvalue=="Change all the above": #Conditions for each Combobox value. Value="Change all the above"
            av=5
            Label(t4, text='                                    ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240) #To hide and change text.
            Label(t4, text="Change all the above:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240)
            Label(t4,text="Name:",fg="#800000", bg='#F0FFF0', font=("arial",10)).place(x=20,y=265)
            Label(t4,text="Entry Year:",fg="#800000", bg='#F0FFF0', font=("arial",10)).place(x=140,y=265)
            Label(t4,text="Midterm:",fg="#800000", bg='#F0FFF0', font=("arial",10)).place(x=260,y=265)
            Label(t4,text="Final:",fg="#800000", bg='#F0FFF0', font=("arial",10)).place(x=380,y=265)
            e2.place(x=140,y=290, width=100) #Adequte Entry.
            e3.place(x=260,y=290, width=100)
            e4.place(x=380,y=290, width=100)
            

            
        
      

      def submit4(): #Command for change button to create a pop-up.
          
          qw=Toplevel()
          qw.title("Are you sure?")
          qw.geometry("250x110")
          qw.resizable(width=False, height=False)
          qw.configure(bg="#F0FFF0")

          icon="logo.png"  #Adding the icon and making a failsafe for it.
          if icon:
            try:
              img=PhotoImage(file=icon) 
              qw.iconphoto(False,img)
            except:
              pass
          else:
           pass
          
          Label(qw, text="Are you sure you want to\nchange the data?",fg="#C71585", bg="#F0FFF0",font=("arial")).place(x=35,y=5) #Pop-up Label.
          ch1=e1.get() #Getting Entry value.
          
          def del2(): #Command for conformation pop-up yes Button to change the data and save it.
             ra=np.arange(0,20.01 , 0.01) #Range for midterm and final.
             if m==1: #Condition to get the Entry value and Replacing it in the appropriate list based on arbitrary value m=av=1.
                     b[int_result]=ch1
                    
             elif m==2: #Condition to get the Entry value and replacing it in the appropriate list based on arbitrary value m=av=2 and range for the Entry value with failsafe of error2.
               ch11=float(ch1)
               ch111=str(int(ch11))
               if ch1 :
                  if ch1.isdigit() and int(ch1) in range(1350,1430) :
                     d[int_result]=ch1
                  else:
                     error2()
               else:
                     error2()
            
             elif m==3: #Condition to get the Entry value and replacing it in the appropriate list based on arbitrary value m=av=3 and range for the Entry value with failsafe of error2.
               ch11=float(ch1)
               ch111=str(int(ch11))
               if  ch1  and ch11 in ra :
                  if ch111.isdigit() :
                     f[int_result]=ch1
                  else:
                     error2()
               else:
                     error2()
             
             elif m==4:#Condition to get the Entry value and replacing it in the appropriate list based on arbitrary value m=av=4 and range for the Entry value with failsafe of error2.
               ch11=float(ch1)
               ch111=str(int(ch11))
               if  ch1  and  ch11 in ra:
                  if ch111.isdigit():
                     h[int_result]=ch1
                  else:
                     error2()
               else:
                     error2()
            
             elif m==5:#Condition to get the Entry values and replacing it in the appropriate list based on arbitrary value m=av=5 and range for the Entry values with failsafe of error2.
                ch2=e2.get()
                ch3=e3.get()
                ch4=e4.get()
                ch33=float(ch3)
                ch44=float(ch4)
                ch333=str(int(ch33))
                ch444=str(int(ch44))
                if ch2 and ch3 and ch4 and ch33 in ra and  ch44 in ra:
                  if ch2.isdigit() and int(ch2) in range(1350,1430) and ch333.isdigit() and ch444.isdigit(): 
                     b[int_result]=ch1
                     d[int_result]=ch2
                     f[int_result]=ch3
                     h[int_result]=ch4
                  else:
                     error2()
                else:
                     error2()

             bb=b #Putting the new lists in arbitrary variabels.
             dd=d
             ff=f
             hh=h
      
             with open('Name.txt',"w+") as file: #Rewriting the files.
                for item in bb:
                 file.write(f"\n{item}")

             with open('Year.txt',"w+") as file:
                for item in dd:
                 file.write(f"\n{item}")
            
             with open('Midterm.txt',"w+") as file:
                for item in ff:
                 file.write(f"\n{item}")

             with open('Final.txt',"w+") as file:
                for item in hh:
                 file.write(f"\n{item}")

             
             if m==5: #Removing the unnecessary Entries after submitting.
               e2.delete(0, END)
               e3.delete(0, END)
               e4.delete(0, END)
               e2.place_forget()
               e3.place_forget()
               e4.place_forget()
             else:
               aa.delete(0, END)
               e1.delete(0, END)
             Label(t4, text='                                                                                     ', fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=265) #Labels for hiding previous texts.
             Label(t4,text="                                                                                                                                             ", font=50,bg="#F0FFF0").place(x=0,y=105)
             Label(t4,text="                                                                                                                                             ", font=50,bg="#F0FFF0").place(x=0,y=115)
             Label(t4,text="                                                                                                                                             ", font=50,bg="#F0FFF0").place(x=0,y=125)
             Label(t4,text="                                                                                                                                             ", font=50,bg="#F0FFF0").place(x=0,y=135)
             Label(t4,text="                                                                                                                                             ", font=50,bg="#F0FFF0").place(x=0,y=145)
             qw.destroy() #Kill the pop-up
        
                 
          Button(qw, text="Yes", command=del2, bg='#00BFFF', activebackground='#0000CD').place(x=60,y=60) #Button to call del2 to change the data.
          Button(qw, text="No", command=qw.destroy, bg='#00BFFF', activebackground='#0000CD').place(x=150,y=60) #Kill the pop-up
      
          qw.mainloop()

   

      m=av #Associating av with arbitrary variable m.

      Button(t4, text="Change", bg='#9ACD32', activebackground='#006400', font=("arial"), command=submit4, width=20).place(x=5,y=400)  #Button to call submit 4 to make the pop-up.

   
   aa=Entry(t4) #Adding an Entry for search part.
   aa.place(x=150,y=72)
   e1=Entry(t4) #Setting the Entries.
   e1.place(x=20,y=290, width=100)
   e2=Entry(t4)
   e3=Entry(t4)
   e4=Entry(t4)
   

   Label(t4, text="What do you want to change?", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=180) #Pop-up label.
   
   cm=ttk.Combobox(t4, values=["Name","Entry year","Midterm","Final","Change all the above"]) #Setting Combobox.
   cm.place(x=280,y=185)
   cm.current("0")
   cm.bind("<<ComboboxSelected>>",oncomboboxselect) #binding combo box results to its seclected value.

   Label(t4, text="Change name:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=240) #Adequate Labels 
   Label(t4,text="Change a student's information",fg="#C71585", bg='#F0FFF0', font=("arial",20)).place(x=55,y=5)
   Label(t4, text="Search number:", fg="#0000CD", bg='#F0FFF0', font=("arial",14)).place(x=5,y=65)
   Button(t4, text="Search",  bg='#9ACD32', activebackground='#0000CD', font=("arial"), command=submit3).place(x=300,y=65) #Button to call submit3 to show the information searched
   Button(t4, text="Change", bg='#9ACD32', activebackground='#006400', font=("arial"), command=error, width=20).place(x=5,y=400)  #Button to call error to overwrite the itself with another Button..

   t4.mainloop()







def creat5(): #Command for the fifth menu button to open a new window.
    t5=Toplevel()
    t5.geometry("500x500")
    t5.title("See the student's information on plot")
    t5.configure(bg="#F0FFF0")
    t5.resizable(width=False, height=False)

    numberaa=number() #Calling functions in the begining of the code to open and read files except the first line.
    nameaa=name()
    yearaa=year()
    midtermaa=midterm()
    finalaa=final()
   
    sn=FileToList("Number.txt")   #Calling Class FileToList to read the files and add them in string form to a list.
    sn.converttolist() 
    ssn=sn.getline()
    a=FileToList("Name.txt")
    a.converttolist() 
    b=a.getline()
    c=FileToList("year.txt")
    c.converttolist()
    d=c.getline()
    e=FileToList("Midterm.txt")
    e.converttolist()
    f=e.getline()
    g=FileToList("Final.txt")
    g.converttolist()
    h=g.getline()

    icon="logo.png" #Adding the icon and making a failsafe for it.
    if icon:
        try:
           img=PhotoImage(file=icon) 
           t5.iconphoto(False,img)
        except:
            pass
    else:
        pass
       
    cc=TxttoFloatList("year.txt") #Calling Class TxttoFloatList to read the txt file for year, midterm, and final and addthem to a list as floats.
    cc.readfloat()
    dd=cc.getfloat()
    ee=TxttoFloatList("Midterm.txt")
    ee.readfloat()
    ff=ee.getfloat()
    gg=TxttoFloatList("Final.txt")
    gg.readfloat()
    hh=gg.getfloat()

    intdd=[int(value) for value in dd] #Turning them from float to int.
    intff=[int(value) for value in ff]
    inthh=[int(value) for value in hh]

    def radiolist(): #Command for the first show button to set the values needed for a histogram and showing the plot.
         value=selectop.get() #Get value of Radiobutton.
         if value=="op1": #Conditions for Radiobutton values that uses the correct set of information to draw the plot. Also, Styling the plot.
            list1=intdd
            def intervalplt(data):
                bin=list(range(1350,1430))
                fig, ax =plt.subplots() #Setting up the histogram and its pop-up
                ax.hist(data, bins=bin, color="#006400") #Styling the histogram.
                ax.set_ylabel("Number").set_color("#0000CD")
                ax.set_xlabel("Year").set_color("#0000CD")
                ax.set_title("Number of students in each year",fontsize = 20).set_color("#C71585")
                ax.tick_params( colors='#0000CD')
                ax.spines['bottom'].set_color('#0000CD')
                ax.spines['top'].set_color('#0000CD') 
                ax.spines['right'].set_color('#0000CD')
                ax.spines['left'].set_color('#0000CD')
                fig.patch.set_facecolor("#F0FFF0") #Styling the background.
                ax.set_facecolor("#F0FFF0")
                plt.show()
            intervalplt(list1)

         elif value=="op2": #Conditions for Radiobutton values that uses the correct set of information to draw the plot. Also, Styling the plot.
            list1=intff
            def intervalplt(data):
                bin=list(range(0,21))
                fig, ax =plt.subplots() #Setting up the histogram and its pop-up
                ax.hist(data, bins=bin, color="#006400") #Styling the histogram.
                ax.set_ylabel("Number").set_color("#0000CD")
                ax.set_xlabel("Midterm").set_color("#0000CD")
                ax.set_xticks(range(0,21))
                ax.set_title("Midterm marks in intervals of 1",fontsize = 20).set_color("#C71585")
                ax.tick_params( colors='#0000CD')
                ax.spines['bottom'].set_color('#0000CD')
                ax.spines['top'].set_color('#0000CD') 
                ax.spines['right'].set_color('#0000CD')
                ax.spines['left'].set_color('#0000CD')
                fig.patch.set_facecolor("#F0FFF0") #Styling the background.
                ax.set_facecolor("#F0FFF0")
                plt.show()
            intervalplt(list1)

         elif value=="op3": #Conditions for Radiobutton values that uses the correct set of information to draw the plot. Also, Styling the plot.
            list1=inthh
            def intervalplt(data):
                bin=list(range(0,21))
                fig1, ax1 =plt.subplots() #Setting up the histogram and its pop-up
                ax1.hist(data, bins=bin, color="#006400") #Styling the histogram.
                ax1.set_ylabel("Number").set_color("#0000CD")
                ax1.set_xlabel("Final").set_color("#0000CD")
                ax1.set_xticks(range(0,21))
                ax1.set_title("Final marks in intervals of 1",fontsize = 20).set_color("#C71585")
                ax1.tick_params( colors='#0000CD')
                ax1.spines['bottom'].set_color('#0000CD')
                ax1.spines['top'].set_color('#0000CD') 
                ax1.spines['right'].set_color('#0000CD')
                ax1.spines['left'].set_color('#0000CD')
                fig1.patch.set_facecolor("#F0FFF0") #Styling the background.
                ax1.set_facecolor("#F0FFF0")
                plt.show()
            intervalplt(list1)
         

    def uniqueyear(yearlist): #Function for finding unique items in list and putting them in a list.
           uniqueyearlist=list(set(yearlist))
           return uniqueyearlist
       
    def uniquefindindex(a,b): #Function for finding unique items, getting their index, putting each unique item(keys) and its indexes(values) in a dictionary element.
        repeated_indexes={}
        for item in a:
            for item in b:
                indexes=[i for i, x in enumerate(b) if x==item]
                if indexes:
                    repeated_indexes[item]=indexes
        return repeated_indexes
    

    def avaragedict(indexdict, c): #Function for searcing the dictionary of indexes in any list and giving back the avarage of searched values in a dictionary of unique items(keys) and avarage(values).
         if indexdict is dict:
               pass
         else:
               pass
         avgdict={}
         for item, indexes in indexdict.items():
             value=[c[i] for i in indexes]
             if value:
                 avg=sum(value)/len(value)
                 avgdict[item]=avg
         return avgdict
        
    
    unidd=uniqueyear(dd) #Calling uniqueyear function for years.
    uniddindex=uniquefindindex(unidd,dd) #Calling uniquefindindex function for years.
    avgff=avaragedict(uniddindex,ff) #Calling avaragedict function for years(keys) and midterm(values).
    avghh=avaragedict(uniddindex,hh) #Calling avaragedict function for years(keys) and final(values).
    intunidd=[int(value) for value in unidd] #Turning the list of years unique values to a list of ints.

    
    def radiolist1(): #Command for the second show button to set the needed values(x,y) and show the plot.
         value=selectop1.get() #Get the value of Radiobutton
         if value=="op11": #Conditions for Radio button based on its value=="op11", setting x,y, showing te plot.
            y=list(avgff.values()) #Setting x,y
            x=list(avgff.keys())
            x1=np.array(x) #Sorthing the data based on the values of x
            y1=np.array(y)
            sorted=np.argsort(x1)
            xs=x1[sorted]
            ys=y1[sorted]
            def intervalplt(): 
                fig, ax =plt.subplots() #Setting up the plot and its pop-up
                ax.plot(xs, ys, color="#006400", marker="o", linewidth=("2"),linestyle=("-."))#Styling the plot
                for i, (xsi, ysi) in enumerate(zip(xs, ys)):
                 plt.annotate(f'({xsi}, {ysi})', (xsi, ysi), textcoords="offset points", xytext=(0, 10), ha='center').set_color("#006400")
                ax.set_ylabel("Year").set_color("#0000CD")
                ax.set_xlabel("Avarage of midterms").set_color("#0000CD")
                ax.set_title("Avarage of midterms in each year",fontsize = 20).set_color("#C71585")
                ax.tick_params( colors='#0000CD')
                ax.spines['bottom'].set_color('#0000CD')
                ax.spines['top'].set_color('#0000CD') 
                ax.spines['right'].set_color('#0000CD')
                ax.spines['left'].set_color('#0000CD')
                fig.patch.set_facecolor("#F0FFF0")#Styling the background.
                ax.set_facecolor("#F0FFF0")
                plt.show()
            intervalplt()

         elif value=="op22":   #Command for the second show button to set the needed values(x,y) and show the plot.
            x=x=list(avghh.keys())  #Setting x,y
            y=list(avghh.values())
            x1=np.array(x)  #Sorthing the data based on the values of x
            y1=np.array(y)
            sorted=np.argsort(x1)
            xs=x1[sorted]
            ys=y1[sorted]
            def intervalplt1():
                fig, ax =plt.subplots() #Setting up the plot and its pop-up
                ax.plot(xs, ys, color="#006400", marker="o", linewidth=("2"),linestyle=("-."))#Styling the plot
                for i, (xsi, ysi) in enumerate(zip(x, y)):
                 plt.annotate(f'({xsi}, {ysi})', (xsi, ysi), textcoords="offset points", xytext=(0, 10), ha='center').set_color("#006400")
                ax.set_ylabel("Year").set_color("#0000CD")
                ax.set_xlabel("Avarage of finals").set_color("#0000CD")
                ax.set_title("Avarage of finals in each year",fontsize = 20).set_color("#C71585")
                ax.tick_params( colors='#0000CD')
                ax.spines['bottom'].set_color('#0000CD')
                ax.spines['top'].set_color('#0000CD') 
                ax.spines['right'].set_color('#0000CD')
                ax.spines['left'].set_color('#0000CD')
                fig.patch.set_facecolor("#F0FFF0")#Styling the background.
                ax.set_facecolor("#F0FFF0")
                plt.show()
            intervalplt1()
            
   
    selectop=StringVar(value="op1") #Setting up the first set of Radiobuttons.
    Radiobutton(t5, text="Year", variable=selectop, value="op1", fg="#006400", bg="#F0FFF0",font=("arial",12)).place(x=20,y=130)
    Radiobutton(t5, text="Midterm", variable=selectop, value="op2", fg="#006400", bg="#F0FFF0",font=("arial",12)).place(x=120,y=130)
    Radiobutton(t5, text="Final", variable=selectop, value="op3", fg="#006400", bg="#F0FFF0",font=("arial",12)).place(x=220,y=130)
    Button(t5,text="Show", bg='#9ACD32', activebackground='#006400', font=("arial"), command=radiolist, width=15).place(x=30,y=190) #Button to call radio list and show the plot.
    selectop1=StringVar(value="op11") #Setting up the first set of Radiobuttons.
    Radiobutton(t5, text="Midterm", variable=selectop1, value="op11", fg="#006400", bg="#F0FFF0",font=("arial",12)).place(x=20,y=320)
    Radiobutton(t5, text="Final", variable=selectop1, value="op22", fg="#006400", bg="#F0FFF0",font=("arial",12)).place(x=120,y=320)
    Button(t5,text="Show", bg='#9ACD32', activebackground='#006400', font=("arial"), command=radiolist1, width=15).place(x=30,y=380) #Button to call radio list and show the plot.
    Label(t5,text="See the student's information on plot",fg="#C71585", bg="#F0FFF0",font=("arial",20)).place(x=25,y=0) #Adequate Labels.
    Label(t5,text="Number of students based on:", fg="#0000CD", bg="#F0FFF0",font=("arial",18)).place(x=5,y=90)
    Label(t5,text="Annual avarage of: ", fg="#0000CD", bg="#F0FFF0",font=("arial",18)).place(x=5,y=270)
    
    t5.mainloop()


 
 

     