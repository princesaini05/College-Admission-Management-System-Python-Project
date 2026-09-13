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
    d=("SELECT admin,password,role FROM admin Where role!= 'SuperAdmin'")
    cur.execute(d)
    row=cur.fetchall()


    for row in row:
        admin=row[0]
        password=row[1]
        role=row[2]
        tree.insert("","end",values=(admin,password,role))


    
def delete():
    m=e10.get()
    if row=="":
        messagebox.showerror("Error", "Enter Admin Name")
        return
    for row in tree.get_children():
        tree.delete(row)
        
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    d=("SELECT role FROM admin where admin=%s")
    cur.execute(d,(m,))
    row=cur.fetchone()

    if row is None:
        messagebox.showerror("Error", "Admin not found")
        return
    
    if row[0]=="SuperAdmin":
        messagebox.showerror("Error","Super Admin cannot be delected.")
        return
    cur.execute("""DELETE FROM admin WHERE admin=%s""",(m,))

    db.commit()
    db.close()

    for row in row:
        admin=row[0]
        password=row[1]
        role=row[2]
        tree.insert("","end",values=(admin,password,role))

    e10.delete(0,END)
    messagebox.askyesno("Ask","Want to delete.")
    show()


def search():
    m=e10.get()
    for row in tree.get_children():
        tree.delete(row)
        
        
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db="clg")
    cur=db.cursor()
    d=("SELECT * FROM admin WHERE admin=%s")
    cur.execute(d,(m,))
    row=cur.fetchone()
    if row[2]=="SuperAdmin":
        messagebox.showerror("Error","Super Admin cannot be searched.")
        return

    for row in row:
        admin=row[0]
        password=row[1]
        role=row[2]
        tree.insert("","end",values=(admin,password,role))

    e10.delete(0,END)
    



def update_pannel():
    username=e10.get()
    if username=="":
        messagebox.showerror("Error","Enter Name to search")
        return
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Prince9084#',db='clg')
    cur=db.cursor()
    d=("""SELECT admin,password,role FROM admin WHERE admin=%s""")
    cur.execute(d,(username,))
    row=cur.fetchone()
    if row=="":
        messagebox.showerror("Error", "Record Not Found")
        return
    elif row[2]=="SuperAdmin":
        messagebox.showerror("Error","Super Admin cannot be update.")
        return
    
    admin=row[0]
    password=row[1]


    update=Toplevel()
    update.geometry("800x600")
    update.title("Update Data")

    L=Label(update,text="Update Admin details",fg="Black",font=("Arial 30 bold"))
    L.place(x=300,y=50)

    L1=Label(update,text="Admin Name",fg="black",font=("Arial 20 bold"))
    L1.place(x=100,y=150)
    e1=Entry(update,font=("arial 20 bold"))
    e1.place(x=300,y=150)

    L2=Label(update,text="Password",fg="Black",font=("Arial 20 bold"))
    L2.place(x=100,y=200)
    e2=Entry(update,font=("arial 20 bold"))
    e2.place(x=300,y=200)


    e1.insert(0,admin)
    e2.insert(0,password)

    def save_update():

        k=e1.get()
        k1=e2.get()

        import pymysql as sql
        db=sql.connect(host='localhost',user='root',password='Prince9084#',db='clg')
        cur=db.cursor()
        cur.execute("""UPDATE admin SET admin=%s,password=%s WHERE admin=%s""",(k,k1,admin))
        db.commit() 
        messagebox.showinfo("Success","Record Updated Successfully")
        update.destroy()
        show()

    e10.delete(0,END)


    B4=Button(update,text="Save",font=("arial 16 bold"),command=save_update)
    B4.place(x=300,y=500)



top=Tk()
top.geometry("1000x600")
top.title("WELCOME")


homeing = ImageTk.PhotoImage(file=r"C:\Users\Prince\Downloads\bg image.jpg")
L10=Label(top,image=homeing)
L10.pack()

tree=ttk.Treeview(top)
tree.place(x=380,y=150,width=500,height=300)
tree['columns']=("admin","password","role")

tree.column("#0",width=0,stretch=NO)

tree.column("admin",width=50,anchor=CENTER)
tree.column("password",width=100,anchor=CENTER)
tree.column("role",width=50,anchor=CENTER)

tree.heading("#0",text="")

tree.heading("admin",text="admin",anchor=CENTER)
tree.heading("password",text="password",anchor=CENTER)
tree.heading("role",text="role",anchor=CENTER)

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
B3.place(x=50,y=200)

B4=Button(top,text="Update",font=("arial 16 bold"),command=update_pannel)
B4.place(x=50,y=260)


top.config(bg="Yellow")
top.mainloop()