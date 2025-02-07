#parent, base, super
class Pen:

    price = 10
    color = "Red"
    def __init__(self):
        pass
    
    def toWrite(self):
        print(self.price," : ", self.color)
#child, derived, sub
class Notebook(Pen):

    pages = 100
    def display(self):
        print(self.price," ",self.color," ",self.pages)

#multilevel
# class Salt(Notebook):
#     pass

#hierachical
# class Salt(Pen):
#     pass

# multiple
# class Salt(Pen,Notebook)
#     pass



p = Pen()
p.toWrite()

n = Notebook()
n.price=5656
n.display()