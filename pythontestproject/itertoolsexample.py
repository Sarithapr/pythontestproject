"""
collection of tools for handling iterators
itearators are data types that can be used in for loop eg:list"""
from itertools import product,permutations,combinations,accumulate,groupby,combinations_with_replacement,count,repeat,cycle
import operator
a=[1,2]
b=[3,4]
p = product(a,b,repeat=2)
print(list(p))
c=[1,2,3]
perm = permutations(c,3)#length is 2[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(list(perm))
d = [1,2,3]
comb = combinations(d,2)#length is 2[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]no combination of a=same argument
combrep = combinations_with_replacement(d,2)
print(list(comb))
print(list(combrep))
e= [2,5,3]
ac= accumulate(e,func=max)
acc= accumulate(e)
accu = accumulate(e,func=operator.mul)
print(list(ac))# 5 is greater than 3 so set as [2,5,5]
print(list(acc))
print(list(accu))#it adds 1, 1+2,3+3 = [1,3,6]
f= [1,2,3]
def smaller_than_3(x):
    return x<3
grp=groupby(f,key=smaller_than_3)
for key,value in grp:
    print(key,list(value))
grp1=groupby(f,key=lambda x:x<3)
for key,value in grp1:
    print(key,list(value))
person=[{'name':'test','age':40},{'name':'sd','age':41},{'name':'sdsdsd','age':40},{'name':'ty','age':24}]
per=groupby(person,key=lambda x:x['age'])
for key,value in per:
    print(key,list(value))
for i in count(10):
    print(i)
    if(i==15):
        break   
"""cyc=[1,2,3] will cycle 123123 infinitely
for i in cycle(a):
    print(i)"""
"""cyc=[1,2,3]
for i in repeat(1): will print1 infinitely repeat (1,4) will repeat one 4 times
    print(i)""" 
    
    
    
    