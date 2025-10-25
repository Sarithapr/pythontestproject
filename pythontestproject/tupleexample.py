'''
Created on Oct 20, 2025

@author: rharidas
'''
tuple1=tuple([1,"abc",'a',True,10.5])
print(tuple1)
tuple6= (4,5,6)
print(tuple6)
emptylist=tuple()
print(emptylist)
tuple2=tuple("python")
print(tuple2)
#accessing elements from the list
print(tuple1[0])
print(tuple1[4])
#operations in list
print(1 in tuple1)
print(1 not in tuple1)
print(len(tuple1))
print("all operations")
tuple3 = tuple([1,2,3])
print(min(tuple3))#TypeError: '<' not supported between instances of 'str' and 'int' for list 1 so creating another list
print(max(tuple3))
print(sum(tuple3))
for i in tuple1:
    print(i)
for i in tuple1:
    print(i)    
    
#list slicing
tuple1=([1,"abc",'for',234,"test"])
print(tuple1[2:4])#for',234
print(tuple1[:2])#1,"abc"
print(tuple1[2:])#for',234,"test"

for i in tuple1:
    #print("values are {}".format(i)) it will print values are 1 values are abc
    #if we want to print the values it always adds next line by default. Give end="" to make it print in one line
    print(i,end=" ")
