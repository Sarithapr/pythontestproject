'''
Created on Oct 18, 2025

@author: rharidas
'''
#list is heterogenous data and we can add,remove list data dynamically and is similar to arrays. [] is the notation
print("creating a list")
list0=["sdfs","sfdf"]
print(list0)
list1=list([1,"abc",'a',True,10.5])
print(list1)
emptylist=list([])
print(emptylist)
list2=list("python")#['p', 'y', 't', 'h', 'o', 'n']
list3=list("reverse")
list3.reverse()
print(list3)
print(list2)
print("accessing elements from the list")
print(list1[0])
print(list1[-1])#prints last elemnt , same for tuple
print(list1[-2])#prints second last elemnt, same for tuple
print(list1[4])
print("operations in list")
print(1 in list1)#to check if 2 var has same refernce ie their id are same
print(1 not in list1)
print(list1+list2)
print(list1*2+list2*2)
print(len(list1))
list3 = [1,2,3]
print(min(list3))#TypeError: '<' not supported between instances of 'str' and 'int' for list 1 so creating another list
print(max(list3))
print(sum(list3))
for i in list3:
    print(i)
for i in list2:
    print(i)    
    
print("list slicing")
list4=[1,"abc",'for',234,"test"]
print(list4[2:4])#for',234\

print(list4[:2])#1,"abc"
print(list4[2:])#for',234,"test"
print(list4[2::2])#for,test here step count is 2
for i in list4:
    #print("values are {}".format(i)) it will print values are 1 values are abc
    #if we want to print the values it always adds next line by default. Give end="" to make it print in one line
    print(i,end=" ")

print("commonly used list methods with return type")
listmethods = [0,2,2,2,21,2,3,4,5,6,7,8,9,10]#[0,2,2,2,21,2,3,4,5,6,7,8,9,10] prints this
numbers=','.join(str(i) for i in listmethods) #converting to string format separated by comma i.e converts a list of interegets to a comma separated string
print(type(numbers))
print(numbers)#0,2,2,2,21,2,3,4,5,6,7,8,9,10
listmethods1 = [11,25,12,13,25]
listmethods2 = [14,15]
listmethods3 = [99,1000]
listmethods.append(11)
print("append result",listmethods)#adds to end
print(listmethods.count(2))#number of occurences of 2 in the list
listmethods.remove(5)#removes the element with value 5
print("remove result",listmethods)
listmethods.pop(2)#removes element in index 2/remove
print(listmethods)
listmethods.pop()#removes last element /append
print(listmethods)
print("combined list is ", listmethods+listmethods1)
print(f"combined list is {listmethods+listmethods1}" )
print(listmethods)
print(listmethods1)#The function extend is an in-place function i.e. it will make the changes to the original list itself. and Since it returns None, you should not re-assign it back to the list variable.
print(listmethods2)
print(listmethods3)
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
print("List comprehension")
list5=[x for x in range(10)]
print(list5)

list5=[x+1 for x in range(10)]
print(list5)

list5=[x for x in range(10) if x%2==0]
print(list5)

a = [19,20]
b = [21,22,23]
a.extend(b)
print(a)#[19, 20, 21, 22, 23] It mereges the contenets of b to a and a now has values of a and b. Applies on list,tuple and set
c=['a','b']
a.append(c)
print(a)#[19, 20, 21, 22, 23, ['a', 'b']] #It appends as a last in the end to a. It adds another list as an object

#Reversing a existing list and saving to another list
k=[0,9,8,7]
k.reverse()
print(k)
print(type(k))#OR
print(reversed(k))
p=list(reversed(k))
print("f p is ",p)
#sorting without changing original list
j=[0,7,1,5]
print(sorted(j))
print(j)#original list is unchanged
print(j.sort())
print(j)#original list is changed

#Get all anmes starting with j and same in new list
oldlist=["james","jack","agsdh","bsfd","jules"]
newlist=[y for y in oldlist if y[0]=="j" ]
print(newlist)
#shuffling list
listb4shuffle=[2,5,4]
from random import shuffle
shuffle(listb4shuffle)
print(listb4shuffle)
liststring= ["5","1","6"]#sortng a string list
listsorted=[int(x) for x in liststring]
listsorted.sort()
print(listsorted)

#iterator in list
a =[5,4,6]
iteratorlist=iter(a)
print(iteratorlist)
print(next(iteratorlist))
print(next(iteratorlist))
print(next(iteratorlist))
#Another example
ab =["abbbbbbb",1,True]
iteratorlist1=iter(ab)
while True:
    try:
        element = next(iteratorlist1)
        print(element)
    except StopIteration:
        break   
    

#print(next(iteratorlist))StopIteration exception
#Generator: they are executed when next() or for loop is called
# when called they exeute till the next yield statement and return and pauses the state. When the another next () is called then
#it resumes
#it is reurned as object and executes oly when next is called so when you simply print a you will get object as returned
#it raised stopIteration when there is no next yield statement.It can be used on list,set etc
#Generator can have multiple yeild statement s while iteratr doesnt
#generator used function where as iterator uses iter() and next()
#pauses and saves local variable state but iterator doesnts use any local variables
#Generator use () and is memry efficient compared to list but not better than iterator
def example():
    print("test1")
    yield 1
    print("test")
    yield 2
    print("test2")
    return 3
    print("test4")

g=example()
print(g)
print(next(g))
print(next(g))
print(next(g))