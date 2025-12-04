"""
test"""
from pygments.unistring import Lo
'''
test'''
#jhkhkhk
import keyword
import sys
print(sys.version)

print (keyword.kwlist)
print("test")
o=5
l=o
print("refcount")
print(sys.getrefcount(o))#no of ref poiting to a particulr object incl its own reference.Here x is referred by x,y and gerrefcount() itslef
a=10.5
name="abc"
name='abcghn'
print (o+l)
#mutiplr values to multiple variables and it can be number,string,boolean,float,tuple,list,dictionary
a,b,c=100,"test",100.5
print(type(a))#<class 'int'>
print(a,b,c)
a,b,c=10,10,10
print(a,b,c)
a=b=c=6
print(a,b,c)
z=1
q=2
q,z=z,q
print(z,q)
if True:#or 1 or some condition like 20>10
    print("true cind")
else:
    print("false cind")

print("outside if")
a=10
if a==10:#or 1 or some condition like 20>10
    print("Ten")
elif a==20:
    print("20")
elif a==30:
    print("30")
else:#this is optional and if none matches it comes here and if we omit this nothing will be printed
    print("else")
print("test")if 1 else print("false")
print("test")if 0 else print("false")
{print("test"),print("test1")}if 1 else {print("false1"),print("false")}

print(list(range(10)))
print(list(range(2,10,2)))#initialvalue,increent or decrement till,increment by. It will print  i.e >mid value second value-1 even nubers
print(list(range(1,10,1)))#odd numbers
print(list(range(10,1,-1)))
print(list(range(-10,-3,2)))

for i in range(8): #use any range from above..here it starts from 0 till 7
    print(i)

i=1
while(i<10):
    print(i)
    i=i+1
    
for i in range(8): #use any range from above
    if(i==5):
        break
    print("break",i)    

for i in range(8): #use any range from above and it returns lst
    if(i==5):
        continue
    print("continue",i)
    
##NUmbersmax
print(max(80,-10,10000))
print(min(80,-10,10000)) 

name,age,sal= "test",33,77000
print(name,sal,age)
print("name is ",name)
print("sal is ",sal)
print("age is ",age)

#type based
print("name is %s and age is %d and sal is %g" % (name,age,sal))

#value and order based based
print("name is {} and age is {} and sal is {}" .format(name,age,sal))

#value and index based
print("name is {0} and age is {1} and sal is {2}" .format(name,age,sal))

a=10,20,30
print(a)

c=int(2.5)
print(c)#prints 2
d=float(2.5)
print(d)
e=int(2)
print(e)
g=float(2)
print(g)
"""
Python errors
name error: del a and print(a) throws name eeror
type error: 5+"name" throws type error
value error: int("2.5") ValueError: invalid literal for int() with base 10: '2.5'
Index error
IO error accessing a file that doesnt exits
Keyerror:Invalid key used to accessa value in dictionary
"""
"""
built in type
listdictionar,set:mutable
string and tuple and numbers are immutable

package contain dir,subpackage,module and sub directory and another modules"""
import random
print(random.random())#0.6950059970178014 float number between 0 and 1
"""print date and time"""
import time
localtime=time.asctime(time.localtime(time.time()))
print(localtime)


