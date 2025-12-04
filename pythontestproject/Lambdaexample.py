'''
Created on Oct 24, 2025

@author: rharidas
'''
from inspect import Arguments
from mako.parsetree import Expression
from functools import reduce
from pygments.unistring import Po
"""
Lamda is anonymous functin and has no name It can take only one expression but any numer of Arguments
and it returns the expression
lamda arguments:Expression
used with sorted,map,filter,reduce
It is used when its used as input to another function
simpe fuctions used only one in the code
"""
x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(6,5))

x=lambda a,b,c:a+b+c
print(x(6,5,1))

square=lambda numbers:numbers*2
print(square([1, 2, 3, 4, 5, 6]))

numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
numbers1 = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))

numbers = [1, 2, 3, 4, 5, 6]
result = [x*x for x in numbers if x % 2 == 0]
print(result)

print(reduce(
    lambda a, b: a + b,
    map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers))
))

points2d=[(1,2),(9,4),(6,-5),(1,7)]
points2dsorted=sorted(points2d)#sort x only
points2dsortedy=sorted(points2d,key=lambda x:x[1])
#points2dsortedy=sorted(points2d,key=lambda x:x[1]+x[0]) according to sum
"""
by using a function
or def sort_by_y(x):
    return x[1]
points2dsortedy=sorted(points2d,key=lambda x:sort_by_y)
"""    
print(points2dsorted)
print(points2dsortedy)
"""
with map: transfrms each lement with a function
map(function,sequence) example map(function,list)
filter(function,sequence): function returns true or flase and filter function reurns all eements hich the funtion evealutaes to true
reduce(function,sequence): it repeatedly applies the function to the elements and returns a single value
"""
ab = [0, 18, 1]
bb = map(lambda x: x*2, ab)   # convert to list so results persist
print("map",list(bb))
d=[x*2 for x in ab]
print(d)
abb = [1, 18, 1]
bbb = filter(lambda x: x*2, abb)   # convert to list so results persist
print("filter",list(bbb))
dbbb=[x for x in abb if x%2 == 0]
print(dbbb)

a = [1, 9, 1]
b = list(map(lambda x: x*2, a))    # convert to list so results persist
print(b)

c = list(filter(lambda x: x % 2 == 0, b))
print(c)

"""reduce example"""
""" reduce always has 2 input variables IMPORTANT"""
a=[4,5,6]
prod= reduce(lambda x,y:x*y, a)
print(prod)





