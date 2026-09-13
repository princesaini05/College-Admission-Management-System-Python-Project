from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


top=Tk()
top.geometry("1200x700")
top.title("WELCOME")

def showlogin():
    top.destroy()
    import login

def showadmin():
    top.destroy()
    import Admin

def insert():
    k=int(e1.get())
    k2=e2.get()
    k3=int(e3.get())
    k4=int(e4.get())
    k5=e5.get()
    k6=cb.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    s="insert into registration values(%s,%s,%s,%s,%s,%s,%s)"
    result=cur.execute(s,(k,k2,k3,k4,k5,k6,"Pending"))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    cb.set("")

    if (result>0):
        messagebox.showinfo("Result","Record insert successfully")
    else:
        messagebox.showinfo("Result","Record not inserted")
    db.commit()
    db.close()

homeing = ImageTk.PhotoImage(file=r"C:\Users\Prince\Downloads\bg image.jpg")
L10=Label(top,image=homeing)
L10.pack()

import pymysql as sql
db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
cur=db.cursor()
s="SELECT course_name,price FROM course"
cur.execute(s)
t=cur.fetchall()
categories=["Select"]
for row in t:
    categories.append(row[0])
db.close()

def price(event):
    h=cb.get()
    
    import pymysql as sql
    db=sql.connect(host="localhost",user="root",password="Prince9084#",db="clg")
    cur=db.cursor()
    cur.execute("""SELECT price FROM course WHERE course_name=%s""",(h,))
    row=cur.fetchone()
    e7.config(state="normal")
    e7.delete(0,END)
    if row:
        e7.insert(0,row[0])
    e7.config(state="readonly")
    db.commit()
    db.close()

L=Label(top,text="Registration",fg="Black",font=("Arial 30 bold"))
L.place(x=500,y=50)

L1=Label(top,text="Student Id",fg="black",font=("Arial 20 bold"))
L1.place(x=100,y=150)
e1=Entry(top,font=("arial 20 bold"))
e1.place(x=250,y=150)

L2=Label(top,text="Name",fg="Black",font=("Arial 20 bold"))
L2.place(x=100,y=200)
e2=Entry(top,font=("arial 20 bold"))
e2.place(x=250,y=200)

L3=Label(top,text="Age",fg='black',font=("arial 20 bold"))
L3.place(x=100,y=250)
e3=Entry(top,font=("arial 20 bold"))
e3.place(x=250,y=250)

L4=Label(top,text="Contact",fg='black',font=("arial 20 bold"))
L4.place(x=100,y=300)
e4=Entry(top,font=("arial 20 bold"))
e4.place(x=250,y=300)

L5=Label(top,text="Password",fg="black",font=("Arial 20 bold"))
L5.place(x=100,y=350)
e5=Entry(top,font=("arial 20 bold"),show="*")
e5.place(x=250,y=350)

def password_button():
    if e5.cget("show")=="*":
        e5.config(show="")
    else:
        e5.config(show="*")

B4=Checkbutton(top,text="Show Password",command=password_button)
B4.place(x=250,y=400)

L6=Label(top,text="Course",fg="black",font=("arial 20 bold"))
L6.place(x=100,y=450)

cb=ttk.Combobox(top,value=categories,state="readonly",font=("arial 20 bold"))
cb.place(x=250,y=450)

cb.bind("<<ComboboxSelected>>",price)

L7=Label(top,text="price",fg="black",font=("arial 20 bold"))
L7.place(x=600,y=450)
e7=Entry(top,font=("arial 20 bold"),state="readonly")
e7.place(x=700,y=450)


B=Button(top,text="Submit",font=("arial 18 bold"),command=insert)
B.place(x=100,y=550)

B2=Button(top,text="Login",font=("arial 18 bold"),command=showlogin)
B2.place(x=250,y=550)

B3=Button(top,text="Admin  Login",font=("arial 14 bold"),command=showadmin)
B3.place(x=800,y=100)


top.config(bg="Yellow")
top.mainloop()