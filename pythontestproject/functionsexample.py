'''
Created on Oct 20, 2025

@author: rharidas
'''
def myfunc():
    pass #to omit body of function
myfunc()

#sum of nos between start and end
def sum(start,end):
    if(start>end):
        print("start should be <end")
        return #none will be output and if a function is not having any return statement and just initialization then also it will give none
    result=0
    for i in range(start,end+1):
        result=result+i 
    return result
s=sum(12,4)
s=sum(2,4)
print(s)

#global and local variab;es
#Global not bound to ny function and can be accessed inside and outside the function
#Local variables are declared inside the function
print("next example")
globalvar=200
def func():
    localvar=5
    globalvar=500
    print(localvar,":",globalvar)#within functon it will be 500
    globalvar=700
print(globalvar)#hereit will be 200
func()


print("next example")
globalvar1=200
def func1():
    localvar=5
    global globalvar1
    globalvar1=500
    print(localvar,":",globalvar1)#within functon it will be 500
    globalvar1=700
print(globalvar1)#200
func1()
print(globalvar1)#hereit will be 700

#passing arguments to default value
print("next example")
def settingValue(i,j=100):
    print(i,j)
    
settingValue(1)
settingValue(50,2000)#new valye will be overwritten

"""passing values to function with positionl arguments (order is importnat),keyword arguments(order nt important),combination"""
print("next example")
def settingValue1(i,j):
    print(i,j)
    
settingValue1(1,2)#positionl arguments
settingValue1(i=3,j=2000)#keyword arguments
settingValue1(j=2000,i=3)#keyword arguments
settingValue1(10,j=3000)
#AFter keyword we cant pass positional argument. Once the keyword starts all should be keyword so below will error out
#so position if any should be first argument followed by keyword
#settingValue1(i=10,3000)#SyntaxError: positional argument follows keyword argument
#parameter without a default then parameter with a default should be the order

# we can return multiple values in pythn function and those are treated as tuple
print("next example")
def settingValue2(i,j):
    return i,j
s=settingValue2(1,2)
print(s)#prints (1, 2) here a function can return multiple values and the variable s can hold 2 values. The same doesnt work in java










