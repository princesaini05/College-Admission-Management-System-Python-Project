from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk

top=Tk()
top.geometry("1200x700")
top.title("WELCOME")
def login():
    username=e1.get()
    password=e2.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    cur.execute("select * from registration where Name=%s and Password=%s and status='Approved'",(username,password))
    row=cur.fetchone()
    db.close()

    if row is None:
        messagebox.showerror("Result","Password and username doesnot match")
        return
    
    status=row[6]

    if status=="Approved":
       top.destroy()
       import welcome
       welcome.open_dash(username)
    
    elif status=='Pending':
        messagebox.showerror("Error","Your admission is awaiting approval.")
    elif status=="Rejected":
        messagebox.showerror("Rejected","Your Amission has been rejected.")

homeing = ImageTk.PhotoImage(file=r"C:\Users\Prince\Downloads\bg image.jpg")
L10=Label(top,image=homeing)
L10.pack()

L=Label(top,text="Log in",fg="Black",font=("Arial 30 bold"))
L.place(x=500,y=50)

L1=Label(top,text="Name",fg="black",font=("Arial 20 bold"))
L1.place(x=100,y=150)
e1=Entry(top,font=("arial 20 bold"))
e1.place(x=250,y=150)

L2=Label(top,text="Password",fg="black",font=("Arial 20 bold"))
L2.place(x=100,y=200)
e2=Entry(top,font=("arial 20 bold"),show="*")
e2.place(x=250,y=200)


B=Button(top,text="Login",font=("arial 18 bold"),command=login)
B.place(x=500,y=300)

top.config(bg="Yellow")
top.mainloop()