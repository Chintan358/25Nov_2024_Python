
# a = [10,20,30,40,50,60,70,30]
# sub = ["Python","Java","Php"]
# l = [True, False]
# all =[10,20,20.33,"Tops",True]
# k = list((10,20,30,40))

# print(a)
# print(len(a))
# print(type(all))
# print(k)

# Access LIST item

# sub = ["Python","Java","Php","Node","React"]

# print(sub[0])
# print(sub[-2])
# print(sub[2:4])
# print(sub[-3:-1])
# print(sub[:5])
# print(sub[2:])
# print("Java" in sub)

# change list item

# list1 = [10,20,30,40,50,60]

# # list1[1] = 200
# # list1[2:5]=[300,400]
# list1.insert(1,1000)
# print(list1)


# Add list item

# l = ["A","B","C","D","E"]
# m = [10,20,30]
# l.append("X")
# l.extend(m)
# l.extend("Tops")
# print(l)

# Remove item

# l = ["A","B","C","D","E"]

# l.remove("B")
# l.pop(3)
# del l[1]
# del l
# l.clear()
# print(l)

# loop list 

l = ["A","B","C","D","E"]

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# [print(i) for i in l]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# # for i in fruits:
# #     if "a" in i:
# #         newlist.append(i)

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

fruits = ["apple", "apple","banana", "cherry", "kiwi","orange","mango",]
flowers = ["rose","lotus","sun-flower","jasmin","lily"]
# fruits.sort(reverse=True)
# fruits.reverse()

# k = fruits.copy()
# k = list(flowers)
# k = fruits[::-1]
# k = fruits+flowers
# print(k)

print(fruits.count("apple"))