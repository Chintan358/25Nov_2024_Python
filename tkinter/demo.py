from tkinter import *
import mysql.connector

root  = Tk()
root.geometry("500x500")

# l1 = Button(root,text="Left").pack(side=LEFT)
# l2 = Button(root,text="Right").pack(side=RIGHT)
# l3 = Button(root,text="Top").pack(side=TOP)
# l4 = Button(root,text="Bottom").pack(side=BOTTOM)


# l1 = Label(root,text="Username").grid(row=1,column=1)
# l2 = Label(root,text="Email").grid(row=2,column=1)
# l3 = Label(root,text="Phone").grid(row=3,column=1)

# e1 = Entry(root).grid(row=1,column=2)
# e2 = Entry(root).grid(row=2,column=2)
# e3 = Entry(root).grid(row=3,column=2)

# b = Button(root,text="submit").grid(row=4, column=2)

def getdata():
    uname = e1.get()
    email = e2.get()
    phone = e3.get()
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="25novpython")
    cursor = mydb.cursor()
    qry = "insert into user values(%s,%s,%s,%s)"
    val = (0,uname,email,phone)
    cursor.execute(qry,val)
    mydb.commit()
    print("data inserted !!!")
    

l1 = Label(root,text="Username").place(x=100,y=100)
l2 = Label(root,text="Email").place(x=100,y=130)
l3 = Label(root,text="Phone").place(x=100,y=160)

e1 = Entry(root)
e1.place(x=170,y=100)
e2 = Entry(root)
e2.place(x=170,y=130)
e3 = Entry(root)
e3.place(x=170,y=160)

b = Button(root,text="submit",command=getdata,width=15).place(x=170,y=190)



root.mainloop()