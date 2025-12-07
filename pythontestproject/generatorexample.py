def mygenerator():
    yield 3
    yield 2
    yield 4

g=mygenerator()
print(g)#<generator object mygenerator at 0x74000f311380>
"""
for i in g:#to rint values it should be lopped or used next() ubtil the stopIteration exception
    print(i)
"""
#print(sorted(g))#list of sorted elements [2,3,4]
print(sum(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))

def countdown(num):
    print("starting")
    while num>0:
        yield num
        num-=1

cd=countdown(4) # we need to call next() to access generator

value=next(cd)#this would print starting and reach till the first yield staetement with num=4 and returms 4 at the yeild statement and pauses at the yield num statement
print(value)#would print 4
print(next(cd)) #will continue to yield and remembeer the current number 4 an update the number to 3 via  num-=1 line and goes to while lopp and stops at yield and returns 3
#so while printing it prints 3

def first_gen(maxlimit):
    num=0
    while num<maxlimit:
        yield num
        num+=1
    
first=first_gen(4)
print(next(first))
print(next(first))
print(sum(first))



    

    