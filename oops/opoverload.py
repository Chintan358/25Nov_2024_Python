

class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,obj):
        return self.a+obj.a,self.b+obj.b

    def __mul__(self,obj):
        return self.a*obj.a,self.b*obj.b



a = A(10,20)
b = A(20,30)

k = a+b
c  = a*b
print(c)
print(k)