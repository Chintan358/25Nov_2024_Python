import sqlite3

db = sqlite3.connect("data.db")

# db.execute("create table student(id int primary key,name varchar(20),email varchar(50))")

# db.execute("insert into student values(3,'Parth','parth@gmail.com')")
# db.commit()

# db.execute("update student set email='harsh@yahoo.com' where id=1")
# db.commit()

# db.execute("delete from student where id=3")
# db.commit()

data =  db.execute("select * from student")
  
for i in data.fetchall():
    print(i)