
class Person:

    def test(self):
        print("person class test calling")

class Harsh(Person):
    def test(self):
        print("harsh class test calling")

h  =Harsh()
h.test()