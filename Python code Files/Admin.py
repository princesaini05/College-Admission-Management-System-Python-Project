from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk

top=Tk()
top.geometry("1200x700")
top.title("WELCOME")

def admin_login():
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    cur.execute("select role from admin where admin=%s and password=%s",(e1.get(),e2.get()))
    row=cur.fetchone()

    if row:
       role=row[0]

       if role=="SuperAdmin":
          top.destroy()
          import SuperAdmin

       elif role=="admin":
           top.destroy()
           import Admin_dashboard
    else:
        messagebox.showinfo("Result","Password and username doesnot match")
    db.close()

homeing = ImageTk.PhotoImage(file=r"C:\Users\Prince\Downloads\bg image.jpg")
L10=Label(top,image=homeing)
L10.pack()

L=Label(top,text="Admin Log in",fg="Black",font=("Arial 30 bold"))
L.place(x=500,y=50)

L1=Label(top,text="Admin Name",fg="black",font=("Arial 20 bold"))
L1.place(x=100,y=150)
e1=Entry(top,font=("arial 20 bold"))
e1.place(x=350,y=150)

L2=Label(top,text="Admin Password",fg="black",font=("Arial 20 bold"))
L2.place(x=100,y=200)
e2=Entry(top,font=("arial 20 bold"),show="*")
e2.place(x=350,y=200)

def show_password():
    if e2.cget("show")=="*":
        e2.config(show="")
    else:
        e2.config(show="*")

B2=Checkbutton(top,text="Show Password",command=show_password)
B2.place(x=350,y=250)

B=Button(top,text="Login",font=("arial 18 bold"),command=admin_login)
B.place(x=500,y=300)

top.config(bg="Yellow")
top.mainloop()