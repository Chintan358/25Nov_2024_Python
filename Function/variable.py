

a = 1

def test():
    global a
    a = 20
    print("Inside : ",a)


print("before calling : ",a)
test()
print("Outside : ",a)