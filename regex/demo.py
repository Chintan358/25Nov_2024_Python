import re

# words = "Hello python, Hello java"
# k = re.findall("Hello1",words)
# print(k)235564

# words = "sun rises in east"
# # k = re.search('\Ain',words)
# # k = re.search(r"\bsun",words)
# print(k)

Nameage="""Rany is 454554 and Jeny is 65, Tom is 85 and Roy is 42 """
# name=re.findall('Rany',Nameage)
# age=re.findall(r'\d{1,2}',Nameage)
# names=re.findall(r'[A-Z][a-z]*',Nameage)
# names=re.findall(r'[A-Z][a-z]*',Nameage)

# print(names)

# name = "chauhan is Harsh a python developer"

# f = re.findall("Harsh",name)
# k = re.match("Harsh",name)
# c = re.search("Harsh",name)
# print(f)
# print(k)
# print(c)

# phone = "90996145"

# k = re.match("^[0-9]{10}$",phone)

# if k is None:
#     print("Invalid phone number")
# else:
#     print("Valid phone")

email = "topsg@gmial.comdd"
pettern = r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]{1,4}$"
k = re.match(pettern,email)
if k is None:
    print("Invalid formate")
else:
    print("Valid formate")   