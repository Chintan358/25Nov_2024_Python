
for i in range(100,1000):

    number = i
    temp  = number

    sum = 0

    while number !=0:
        rem = number%10
        sum =sum + rem**3  #153
        number = number//10


    if sum==temp:
        print(f"{temp} is armstrong")
    else:
        # print(f"{temp} is not armstrong")
        pass