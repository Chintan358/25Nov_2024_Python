
class Demo:

    def __init__(self,id, name):
        self.id = id
        self.name = name

    # def display(self):
    #     print(self.id, self.name)
    #     print("Running display...")

    # def show(self,a):
    #     print("show method calling",a)

    def printdata(self):
        print(self.id,self.name)


# d  = Demo()
# d.display()
# d.show(10)

d1 = Demo(10,"tops")
d1.printdata()