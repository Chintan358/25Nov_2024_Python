
print("program started")

# try : 
#     a = 10
#     b = a/2
#     print(b)
# except Exception as e:
#     # print(e)
#     pass


try : 
    # a  =int(input("Enter number : "))
    # print(a)
    a = 10/2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("okay")
finally:
    print("always executable block")


print("program ended")
