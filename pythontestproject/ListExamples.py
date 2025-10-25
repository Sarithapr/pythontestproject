'''
Created on Oct 18, 2025

@author: rharidas
'''
#list is heterogenous data and we can add,remove list data dynamically and is similar to arrays. [] is the notation
#creating a list
list1=list([1,"abc",'a',True,10.5])
print(list1)
emptylist=list([])
print(emptylist)
list2=list("python")#['p', 'y', 't', 'h', 'o', 'n']
print(list2)
#accessing elements from the list
print(list1[0])
print(list1[4])
#operations in list
print(1 in list1)
print(1 not in list1)
print(list1+list2)
print(list1*2+list2*2)
print(len(list1))
list3 = list([1,2,3])
print(min(list3))#TypeError: '<' not supported between instances of 'str' and 'int' for list 1 so creating another list
print(max(list3))
print(sum(list3))
for i in list3:
    print(i)
for i in list2:
    print(i)    
    
#list slicing
list4=[1,"abc",'for',234,"test"]
print(list4[2:4])#for',234
print(list4[:2])#1,"abc"
print(list4[2:])#for',234,"test"

for i in list4:
    #print("values are {}".format(i)) it will print values are 1 values are abc
    #if we want to print the values it always adds next line by default. Give end="" to make it print in one line
    print(i,end=" ")

#commonly used list methods with return type
listmethods = [0,2,2,2,21,2,3,4,5,6,7,8,9,10]
listmethods1 = [11,25,12,13,25]
listmethods2 = [14,15]
listmethods3 = [99,1000]
listmethods.append(11)
print("append result",listmethods)#adds to end
print(listmethods.count(2))#number of occurences of 2 in the list
listmethods.remove(5)#removes the element with value 5
print("remove result",listmethods)
listmethods.pop(2)#removes element in index 2
print(listmethods)
listmethods.pop()#removes last element
print(listmethods)
print(listmethods+listmethods1)
print(listmethods)
print(listmethods1)#The function extend is an in-place function i.e. it will make the changes to the original list itself. and Since it returns None, you should not re-assign it back to the list variable.
listmethods2.extend(listmethods3)
print(listmethods2.extend(listmethods3))#prints none
print(listmethods2)
print(listmethods2.insert(1,345))#inserts 345 to first position
print(listmethods2)
listmethods1.remove(25)#removes the first 25
print(listmethods1)
listmethods1.reverse()
print(listmethods1)
listmethods1.sort()
print(listmethods1)
#List comprehension
list5=[x for x in range(10)]
print(list5)

list5=[x+1 for x in range(10)]
print(list5)

list5=[x for x in range(10) if x%2==0]
print(list5)








