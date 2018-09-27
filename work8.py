import math
a,b,c=eval(raw_input("enter a,b,c:>>"))
d=b*b-4*a*c
if  d>0:
    r1=(-b+(math.sqrt(d)))/2*a
    r2=(-b-(math.sqrt(d)))/2*a
    print(r1,r2)
elif d==0:
    r1=(-b+(math.aqrt(d)))/2*a
    print(r1)
elif d<0:
    print(0)

