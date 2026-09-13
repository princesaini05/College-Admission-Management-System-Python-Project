from tkinter import*
from PIL import Image,ImageTk

def open_dash(username):
    top=Tk()
    top.geometry("800x600")
    top.title("Student Dashboard")


    homeing = ImageTk.PhotoImage(file=r"C:\Users\Prince\Downloads\bg image.jpg")
    L10=Label(top,image=homeing)
    L10.pack()

    L=Label(top,text="Student Details",fg="Black",font=("Arial 30 bold"))
    L.place(x=250,y=100)


    import pymysql as sql
    db=sql.connect(host="localhost",user="root",password="Prince9084#",db="clg")
    cur=db.cursor()
    d=("""SELECT name,course,status FROM registration WHERE name=%s""")
    cur.execute(d,(username,))
    row=cur.fetchone()
    db.commit()
    db.close()

    if row:
        name=row[0]
        course=row[1]
        Admission=row[2]

    L1=Label(top,text=f"Welcome:{name}",font="arial 20 bold")
    L1.place(x=400,y=200,anchor=CENTER)

    L2=Label(top,text=f"Course Name:{course}",font="arial 20 bold")
    L2.place(x=400,y=250,anchor=CENTER)

    L3=Label(top,text=f"Admission Status:{Admission}",font="arial 20 bold")
    L3.place(x=400,y=300,anchor=CENTER)

    top.config(bg="Yellow")
    top.mainloop()