

class A:

    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(self.id,self.name)

class B(A):
    
    def __init__(self, id, name,email):
        self.email=email
        super().__init__(id, name)

    def show(self):
        print(self.id,self.name,self.email)



a  = A(10,"Harsh")
a.display()

b = B(10,"rashi","rashi@gmail.com")
b.show()