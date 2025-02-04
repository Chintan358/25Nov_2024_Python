
class Demo:

    id=0
    name="test"

    def __init__(self,id,name):
        self.id  = id
        self.name=name

    def show(self):
        print(self.id, self.name)
    
    def add(self,a,b):
        print(a+b)



d = Demo(10,"tech")
d.show()

d1 = Demo(11,"Khushabh")
d1.show()

# print(type(d))





