"""
test"""
'''
test'''
#jhkhkhk
import keyword
print (keyword.kwlist)
print("test")
x=5
y=2
a=10.5
name="abc"
name='abcghn'
print (x+y)
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

for i in range(8): #use any range from above
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

