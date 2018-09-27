import math
a=eval(raw_input("enter an inteager:>>"))
c=0
for i in range(4):
    b=a%10
    a=a/10
    c=c+b*(math.pow(10,3-i))
print(c)
