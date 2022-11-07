from tkinter import*
from tkinter import ttk
import random
import datetime
from tkinter import messagebox
import mysql.connector
from tkinter.filedialog import askopenfile
root=Tk()
root.title("ONLINE RESUME BUILDER")
root.geometry("1200x800+0+0")
root.configure(background='blanchedAlmond')

#--------------------------FUNCTIONS------------------------------------------
def exitt():
    root.destroy()

def change():
    f=open("RESUME.txt","w")
    f.write(Namevalue.get())
    f.write("\n")
    f.write(str(lbvalue.get()))
    f.write("\n")
    f.write(lbvalue2.get())
    f.write("\n")
    f.write(lbvalue66.get())
    f.write("\n")
    f.write(str(lbvalue3.get()))
    f.write("\n")
    f.write((lbvalue4.get()))
    f.write("\n")
    f.write(str(lbvalue5.get()))
    f.write("\n")
    f.write(lbvalue6.get())
    f.write("\n")
    f.write(str(lbvalue7.get()))
    f.write("\n")
    f.write(lbvalue8.get())
    f.write("\n")
    f.write(lbvalue9.get())
    f.write("\n")
    f.write(lbvalue10.get())
    f.write("\n")
    f.write(lbvalue11.get())
    f.write("\n")
    f.write(lbvalue12.get())
    f.write("\n")
    f.write(lbvalue13.get())
    f.write("\n")
    f.write(lbvalue14.get())
    f.write("\n")
    f.write(lbvalue15.get())
    f.write("\n")
    f.write(lbvalue16.get())
    f.write("\n")
    f.write(lbvalue17.get())
    f.write("\n")
    f.write(lbvalue18.get())
    f.write("\n")
    f.write(str(lbvalue19.get()))
    f.write("\n")
    f.write(lbvalue20.get())
    f.write("\n")
    I=T.get("1.0","end-1c")
    f.write(I)
    f.write("\n")
    f.close()
    
def resett():
    Namevalue.set("")
    lbvalue.set(0)
    lbvalue2.set("")
    lbvalue66.set("")
    lbvalue3.set(0)
    lbvalue4.set("")
    lbvalue5.set(0)
    lbvalue6.set("")
    lbvalue7.set(0)
    lbvalue8.set("") 
    lbvalue9.set("")
    lbvalue10.set("")
    lbvalue11.set("")
    lbvalue12.set("")
    lbvalue13.set("")
    lbvalue14.set("")
    lbvalue15.set("")
    lbvalue16.set("")
    lbvalue17.set("")
    lbvalue18.set("")
    lbvalue19.set(0)
    lbvalue20.set("")
#------------------------------------------------------------------------------

lb=Label(root,bd=20,relief=RAISED,text="ONLINE  RESUME  BUILDER",fg="navy",bg="white",font=("times new roman",40,"bold"))
lb.grid(row=0,column=5)

f=Frame(root,relief=FLAT,width=1100,height=400,background='blanchedAlmond')
f.grid(row=1,column=5)

fl=LabelFrame(f,bd=10,relief=RAISED,padx=10,font=("times new roman",20,"bold"),text="Personal Details",width=1500,height=350)
fl.grid(row=5,column=5)

b=Frame(root,bd=20,relief=RAISED,width=1500,height=70)
b.grid(row=9,column=5)

df=Frame(root,bd=20,width=1500,height=400,background='blanchedAlmond')
df.grid(row=7,column=5)

#************************ PERSONAL DETAILS************************************ 

Name=Label(fl,font=("Arial",12,"bold"),text="Name",padx=2)
Name.grid(row=0,column=0,sticky=W)
Namevalue=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=Namevalue)
tex.grid(row=0,column=1)

lb0=Label(fl,font=("Arial",12,"bold"),text="Age",padx=2)
lb0.grid(row=1,column=0,sticky=W)
lbvalue=IntVar()
tex1=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue)
tex1.grid(row=1,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="Email-ID",padx=2)
lb1.grid(row=2,column=0,sticky=W)
lbvalue2=StringVar()
tex2=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue2)
tex2.grid(row=2,column=1)

lb2=Label(fl,font=("Arial",12,"bold"),text="Current Qualification",padx=2,pady=6)
lb2.grid(row=3,column=0,sticky=W)
lbvalue66=StringVar()

ln=ttk.Combobox(fl,state="readonly",font=("Arial",12,"bold"),width=33,textvariable=lbvalue66)
ln["value"]=("12th","UnderGraduate","PostGraduate")
ln.current(0)
ln.grid(row=3,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="10th Percentage",padx=2)
lb1.grid(row=4,column=0,sticky=W)
lbvalue3=IntVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue3)
tex.grid(row=4,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="Institution of passing 10th",padx=2)
lb1.grid(row=5,column=0,sticky=W)
lbvalue4=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue4)
tex.grid(row=5,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="12th Percentage",padx=2)
lb1.grid(row=6,column=0,sticky=W)
lbvalue5=IntVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue5)
tex.grid(row=6,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="Institution of passing 12th",padx=2)
lb1.grid(row=7,column=0,sticky=W)
lbvalue6=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue6)
tex.grid(row=7,column=1)
lb1=Label(fl,font=("Arial",12,"bold"),text="College CGPA",padx=2)
lb1.grid(row=8,column=0,sticky=W)
lbvalue7=IntVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue7)
tex.grid(row=8,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="Institution of passing Graduation",padx=2)
lb1.grid(row=9,column=0,sticky=W)
lbvalue8=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue8)
tex.grid(row=9,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="Degree",padx=2)
lb1.grid(row=10,column=0,sticky=W)
lbvalue9=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue9)
tex.grid(row=10,column=1)

lb1=Label(fl,font=("Arial",12,"bold"),text="Skill 1",padx=2)
lb1.grid(row=0,column=2,sticky=W)
lbvalue10=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue10)
tex.grid(row=0,column=3)

lb1=Label(fl,font=("Arial",12,"bold"),text="Skill 2",padx=2)
lb1.grid(row=1,column=2,sticky=W)
lbvalue11=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue11)
tex.grid(row=1,column=3)

lb1=Label(fl,font=("Arial",12,"bold"),text="Skill 3",padx=2)
lb1.grid(row=2,column=2,sticky=W)
lbvalue12=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue12)
tex.grid(row=2,column=3)

lb1=Label(fl,font=("Arial",12,"bold"),text="Achievement 1",padx=2)
lb1.grid(row=3,column=2,sticky=W)
lbvalue13=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue13)
tex.grid(row=3,column=3)

lb1=Label(fl,font=("Arial",12,"bold"),text="Achievement 2",padx=2)
lb1.grid(row=4,column=2,sticky=W)
lbvalue14=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue14)
tex.grid(row=4,column=3)

lb1=Label(fl,font=("Arial",12,"bold"),text="Achievement 3",padx=2)
lb1.grid(row=5,column=2,sticky=W)
lbvalue15=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue15)
tex.grid(row=5,column=3)

lb=Label(fl,font=("Arial",12,"bold"),text="Project 1",padx=2)
lb.grid(row=6,column=2,sticky=W)
lbvalue16=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue16)
tex.grid(row=6,column=3)

lb=Label(fl,font=("Arial",12,"bold"),text="Project 2",padx=2)
lb.grid(row=7,column=2,sticky=W)
lbvalue17=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue17)
tex.grid(row=7,column=3)

lb=Label(fl,font=("Arial",12,"bold"),text="Project 3",padx=2)
lb.grid(row=8,column=2,sticky=W)
lbvalue18=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue18)
tex.grid(row=8,column=3)

lb=Label(fl,font=("Arial",12,"bold"),text="Contact Number",padx=2)
lb.grid(row=9,column=2,sticky=W)
lbvalue19=IntVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue19)
tex.grid(row=9,column=3)

lb=Label(fl,font=("Arial",12,"bold"),text="Permanent Address",padx=2)
lb.grid(row=10,column=2,sticky=W)
lbvalue20=StringVar()
tex=Entry(fl,font=("Arial",12,"bold"),width=35,textvariable=lbvalue20)
tex.grid(row=10,column=3)

f2=LabelFrame(df,bd=10,relief=RAISED,padx=10,font=("times new roman",20,"bold"),text="Work Experience",width=1100,height=250)
f2.grid(row=7,column=10)
lbvalue21=StringVar()
T=Text(f2,fg="black",font=("Arial",19,"bold"),width=75,height=5)
T.grid(row=7,column=10)

# ***********************************************************************

#************************ BUTTONS************************************ 

btn1_=Button(b,text="SUBMIT",bg="dark violet",fg="white",font=("Arial",19,"bold"),width=13,height=1,command=lambda:change())
btn1_.grid(row=0,column=2)

btn2_=Button(b,text="UPDATE",bg="firebrick2",fg="white",font=("Arial",19,"bold"),width=13,height=1,command=change)
btn2_.grid(row=0,column=3)

btn3_=Button(b,text="SHOW",bg="magenta4",fg="white",font=("Arial",19,"bold"),width=13,height=1,command=exitt)
btn3_.grid(row=0,column=4)

btn4_=Button(b,text="RESET",bg="green2",fg="white",font=("Arial",19,"bold"),width=13,height=1,command=resett)
btn4_.grid(row=0,column=5)

btn5_=Button(b,text="EXIT",bg="deep pink",fg="white",font=("Arial",19,"bold"),width=13,height=1,command=exitt)
btn5_.grid(row=0,column=6)

root.mainloop()