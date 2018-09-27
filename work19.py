a,b,c=eval(raw_input("enter three edge:>>"))
a1=a+b
b1=b+c
c1=a+c
a2=a1-c
b2=b1-a
c2=c1-b
if a2>0 and b2>0 and c2>0:
    print(a+b+c)
else:
    print(2)
