a,b,c=eval(raw_input("shuru tree>>"))
if a<b:
    t=b;
    b=a;
    a=t;
if b<c:
    t=c;
    c=b;
    b=t;
if a<b:
    t=b;
    b=a;
    a=t;
print (a,b,c)
