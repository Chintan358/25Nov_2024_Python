from tkinter import *
import mysql.connector
root = Tk()
root.geometry("500x500")

# b1 = Button(root,text="left")
# b2 = Button(root,text="right")
# b3 = Button(root,text="top")
# b4 = Button(root,text="bottom")

#place
#grid
#pack

# b1.pack(side=LEFT)
# b2.pack(side=RIGHT)
# b3.pack(side=TOP)
# b4.pack(side=BOTTOM)

# b1.grid(row=1,column=1)
# b2.grid(row=2,column=1)
# b3.grid(row=1,column=2)
# b4.grid(row=2,column=2)

# b1.place(x=100,y=100)
# b2.place(x=100,y=150)
# b3.place(x=200,y=100)
# b4.place(x=200,y=150)

def adduser():
    username = e1.get()
    email = e2.get()
    phone = e3.get()
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="25novpython")
    mycursor = mydb.cursor()
    qry = "insert into user values(%s,%s,%s,%s)"
    val = (0,username,email,phone)
    mycursor.execute(qry,val)
    mydb.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
l1 = Label(root,text="Username")
l2 = Label(root,text="Email")
l3 = Label(root,text="Phone")

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

btn = Button(root,text="Submit", command=adduser,width=15,font= ("Helvetica", 12))

l1.place(x=100,y=100)
l2.place(x=100,y=150)
l3.place(x=100,y=200)

e1.place(x=200,y=100)
e2.place(x=200,y=150)
e3.place(x=200,y=200)

btn.place(x=200,y=250)



root.mainloop()

