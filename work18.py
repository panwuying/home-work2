import math
a=eval(raw_input("enter>>"))
c=0
e=a
for i in range(3):
    b=a%10
    a=a/10
    c=c+(b*math.pow(10,2-i))
    print(c)
if c==e:
    print("yes")
else:
    print("no")
