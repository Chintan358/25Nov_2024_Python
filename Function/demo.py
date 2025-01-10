
def display():
    print("running display")

def square(a):
    sq = a*a
    return sq

def add(a,b=10):
    c  =a+b
    print(c)

def user(name,email="test@gmail.com",phone="565656565"):
    print(name,email,phone)


display()
a = square(10)
print(a)
print(square(20))
add(10)
user("Harsh","h@gmailc.om","111111111")
user("Rashi",phone="111111111")