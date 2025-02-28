from tkinter import *
import mysql.connector
from tkinter import messagebox,ttk
root = Tk()
root.geometry("700x500")

def addUser():
    uname = e1.get()
    email = e2.get()
    phone = e3.get()
    username = e1.get()
    email = e2.get()
    phone = e3.get()
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="25novpython")
    mycursor = mydb.cursor()
    qry = "insert into user values(%s,%s,%s,%s)"
    val = (0,username,email,phone)
    mycursor.execute(qry,val)
    mydb.commit()
    messagebox.showinfo("Message","User Inserted!!!")
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    for i in table.get_children():
        table.delete(i)
    show()

def show():
    mydb = mysql  .connector.connect(host="localhost",user="root",password="root",database="25novpython")
    mycursor = mydb.cursor()
    qry = "select * from user"
    mycursor.execute(qry)
    data = mycursor.fetchall()
    for i,(id,uname,email,phone)in enumerate(data,start=1):
        table.insert("","end",values=(id,uname,email,phone))

def getdata(self):
    rowid = table.selection()[0]
    data =  table.set(rowid)
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e.insert(0,data['Id'])
    e1.insert(0,data['Username'])
    e2.insert(0,data['Email'])
    e3.insert(0,data['Phone'])

l = Label(root,text="Id").place(x=100,y=70)
l1 = Label(root,text="Username").place(x=100,y=100)
l2 = Label(root,text="Email").place(x=100,y=130)
l3 = Label(root,text="Phone").place(x=100,y=160)

e=Entry(root)
e.place(x=170,y=70)
e1 = Entry(root)
e1.place(x=170,y=100)
e2 = Entry(root)
e2.place(x=170,y=130)
e3 = Entry(root)
e3.place(x=170,y=160)

b1 = Button(root,text="Add",command=addUser,width=8).place(x=100,y=190)
b2 = Button(root,text="Update",command=addUser,width=8).place(x=170,y=190)
b3 = Button(root,text="Delete",command=addUser,width=8).place(x=240,y=190)

cols = ("Id","Username","Email","Phone")
table = ttk.Treeview(root,columns=cols,show="headings")

for col in cols:
    table.heading(col,text=col)
    table.place(x=10, y=230)

show()

table.bind("<Double-Button-1>",getdata)


root.mainloop()