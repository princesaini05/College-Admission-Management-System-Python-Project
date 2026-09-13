from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk

def show():

    for row in tree.get_children():
        tree.delete(row)
        
        
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    d=("SELECT student_id,name,age,contact,course,status FROM registration")
    cur.execute(d)
    results=cur.fetchall()

    for row in results:
        id=row[0]
        name=row[1]
        age=row[2]
        contact=row[3]
        course=row[4]
        status=row[5]
        tree.insert("","end",values=(id,name,age,contact,course,status))



    
def delete():
    m=e10.get()
    for row in tree.get_children():
        tree.delete(row)
        
        
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    d=("DELETE FROM registration where name=%s")
    cur.execute(d,m)
    results=cur.fetchall()
    db.commit()

    for row in results:
        id=row[0]
        name=row[1]
        age=row[2]
        contact=row[3]
        course=row[4]
        tree.insert("","end",values=(id,name,age,contact,course))

    e10.delete(0,END)
    

def search():
    m=e10.get()
    for row in tree.get_children():
        tree.delete(row)
        
        
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    d=("SELECT * FROM registration WHERE name=%s")
    cur.execute(d,m)
    results=cur.fetchall()

    for row in results:
        id=row[0]
        name=row[1]
        age=row[2]
        contact=row[3]
        course=row[4]
        tree.insert("","end",values=(id,name,age,contact,course))
    e10.delete(0,END)

def add_course():
    course=Toplevel()
    course.title("Add Couse")
    course.geometry("800x800")
    C=Label(course,text="Add course",font=("arial 18 bold"))
    C.pack(pady=10)

    C1=Label(course,text="Course Name",font=("arial 18 bold"))
    C1.place(x=100,y=200)
    E4=Entry(course,font=("arial 18 bold"))
    E4.place(x=300,y=200)

    C2=Label(course,text="Price",font=("arial 18 bold"))
    C2.place(x=100,y=300)
    E5=Entry(course,font=("arial 18 bold"))
    E5.place(x=300,y=300)

    def course_name():
        k=E4.get()
        k1=E5.get()

        import pymysql as sql
        db=sql.connect(host="localhost",user="root",password="Prince9084#",db="clg")
        cur=db.cursor()
        cur.execute("""INSERT INTO course(course_name,price) VALUES(%s,%s)""",(k,k1))
        db.commit()
        db.close()

    e10.delete(0,END)

    messagebox.showinfo("Success","Course Added")
    
    B1=Button(course,text="Save",font="arial 16 bold",command=lambda:[course_name(),course.destroy()])
    B1.place(x=350,y=400)
    



def update_pannel():
    username=e10.get()
    if username=="":
        messagebox.showerror("Error","Enter Name to search")
        return
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db='clg')
    cur=db.cursor()
    d=("""SELECT student_id,name,age,contact,course FROM registration WHERE name=%s""")
    cur.execute(d,(username,))
    row=cur.fetchone()
    if row=="":
        messagebox.showerror("Error", "Record Not Found")
        return
    
    id=row[0]
    name=row[1]
    age=row[2]
    contact=row[3]
    course=row[4]


    update=Toplevel()
    update.geometry("800x600")
    update.title("Update Data")

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

    L=Label(update,text="Update details",fg="Black",font=("Arial 30 bold"))
    L.place(x=300,y=50)

    L1=Label(update,text="Student Id",fg="black",font=("Arial 20 bold"))
    L1.place(x=100,y=150)
    e1=Entry(update,font=("arial 20 bold"))
    e1.place(x=250,y=150)

    L2=Label(update,text="Name",fg="Black",font=("Arial 20 bold"))
    L2.place(x=100,y=200)
    e2=Entry(update,font=("arial 20 bold"))
    e2.place(x=250,y=200)
  
    L3=Label(update,text="Age",fg='black',font=("arial 20 bold"))
    L3.place(x=100,y=250)
    e3=Entry(update,font=("arial 20 bold"))
    e3.place(x=250,y=250)

    L4=Label(update,text="Contact",fg='black',font=("arial 20 bold"))
    L4.place(x=100,y=300)
    e4=Entry(update,font=("arial 20 bold"))
    e4.place(x=250,y=300)

    L6=Label(update,text="Course",fg="black",font=("arial 20 bold"))
    L6.place(x=100,y=350)

    cb1=ttk.Combobox(update,value=categories,font=("arial 20 bold"))
    cb1.place(x=250,y=350)

    e1.insert(0,id)
    e2.insert(0,name)
    e3.insert(0,age)
    e4.insert(0,contact)
    cb1.set(course)

    def save_update():

        k=e1.get()
        k1=e2.get()
        k2=e3.get()
        k3=e4.get()
        k4=cb1.get()

        import pymysql as sql
        db=sql.connect(host='localhost',user='root',password='Prince9084#',db='clg')
        cur=db.cursor()
        cur.execute("""UPDATE registration SET student_id=%s,name=%s,age=%s,contact=%s,course=%s WHERE student_id=%s""",(k,k1,k2,k3,k4,k))
        db.commit()
        messagebox.showinfo("Success","Record Updated Successfully")
        update.destroy()
        show()

    e10.delete(0,END)


    B4=Button(update,text="Save",font=("arial 16 bold"),command=save_update)
    B4.place(x=300,y=500)


def approve_student():
    name=e10.get()

    if name=="":
        messagebox.showerror("Error","Enter Student Name")
        return
    
    import pymysql as sql
    db=sql.connect(host="localhost",user="root",password="Prince9084#",db="clg")
    cur=db.cursor()
    d=("""UPDATE registration SET status='Approved' WHERE name=%s""")
    cur.execute(d,(name,))
    db.commit()
    db.close()
    e10.delete(0,END)

    messagebox.showinfo("Succes","Approved succesfully")
    show()


def reject_student():
    name=e10.get()

    if name=="":
        messagebox.showerror("Error","Enter Student Name")
        return
    
    import pymysql as sql
    db=sql.connect(host="localhost",user="root",password="Prince9084#",db="clg")
    cur=db.cursor()
    d=("""UPDATE registration SET status='Rejected' WHERE name=%s""")
    cur.execute(d,(name,))
    db.commit()
    db.close()
    e10.delete(0,END)

    messagebox.showinfo("Succes","Rejected succesfully")
    show()



top=Tk()
top.geometry("1000x600")
top.title("WELCOME")


homeing = ImageTk.PhotoImage(file=r"C:\Users\Prince\Downloads\bg image.jpg")
L10=Label(top,image=homeing)
L10.pack()

tree=ttk.Treeview(top)
tree.place(x=380,y=150,width=500,height=300)
tree['columns']=("student_id","name","age","contact","course","status")

tree.column("#0",width=0,stretch=NO)

tree.column("student_id",width=50,anchor=CENTER)
tree.column("name",width=100,anchor=CENTER)
tree.column("age",width=50,anchor=CENTER)
tree.column("contact",width=100,anchor=CENTER)
tree.column("course",width=100,anchor=CENTER)
tree.column("status",width=100,anchor=CENTER)

tree.heading("#0",text="")

tree.heading("student_id",text="student_id",anchor=CENTER)
tree.heading("name",text="name",anchor=CENTER)
tree.heading("age",text="age",anchor=CENTER)
tree.heading("contact",text="contact",anchor=CENTER)
tree.heading("course",text="course",anchor=CENTER)
tree.heading("status",text="status",anchor=CENTER)

L=Label(top,text="Welcome Admin",fg="Black",font=("Arial 30 bold"))
L.place(x=450,y=50)

e10=Entry(top,font=("arial 18 bold"))
e10.place(x=500,y=470)

B=Button(top,text="Log out",font=("arial 16 bold"),command=lambda:[top.destroy(),top.deiconify()])
B.place(x=50,y=440)

B1=Button(top,text="Show Data",font=("arial 16 bold"),command=show)
B1.place(x=50,y=140)

B2=Button(top,text="Search",font=("arial 16 bold"),command=search)
B2.place(x=580,y=520)

B3=Button(top,text="Delete",font=("arial 16 bold"),command=delete)
B3.place(x=50,y=290)

B4=Button(top,text="Update",font=("arial 16 bold"),command=update_pannel)
B4.place(x=50,y=340)

B5=Button(top,text="Add course",font=("arial 16 bold"),command=add_course)
B5.place(x=50,y=390)

B6=Button(top,text="Approve",font=("arial 16 bold"),command=approve_student)
B6.place(x=50,y=190)

B7=Button(top,text="Reject",font=("arial 16 bold"),command=reject_student)
B7.place(x=50,y=240)


top.config(bg="Yellow")
top.mainloop()