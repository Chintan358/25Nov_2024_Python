
# def test():
#     try:
#         a = int(input("Enter number : "))
#         return 1
#     except Exception as e:
#         return 0
#     finally:
#         print("Program ended....")


# k = test()
# print(k)


try : 
    f = open("test.txt",'r')
    data = f.read()
    print(data)
   
except Exception as e:
    print(e)
finally:
     print(f)
     if(f!=None):
        f.close()