def fibonaci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
        
f= fibonaci(30)
for i in f:
    print(i)