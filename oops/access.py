#public
# class Demo:

#     def __init__(self,id,name):
#         self.id  =id
#         self.name = name
    
#     def disp(self):
#         print(f"my name id {self.name} and id is {self.id}")

# d = Demo(10,"Harsh")
# # d.name="Rashi"
# # d.disp()
# print(dir(d))

#protected

# class Demo:

#     _id = None
#     _name=None

#     def __init__(self,id,name):
#         self._id  =id
#         self._name = name
    
#     def disp(self):
#         print(f"my name is {self._name} and id is {self._id}")

# d = Demo(10,"Harsh")
# print(d._id)
# d.disp()
# print(dir(d))


class Demo:

    __id = None
    __name=None

    def __init__(self,id,name):
        self.__id  =id
        self.__name = name
    
    def disp(self):
        print(f"my name is {self._name} and id is {self._id}")

d = Demo(10,"Harsh")
print(d._Demo__id)
# d.disp()