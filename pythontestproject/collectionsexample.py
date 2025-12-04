from collections import Counter,namedtuple,OrderedDict,defaultdict,deque
""" provides additional functionalities in addition to built in continers like tuples,list and dictionaries"""
import struct
from _ctypes import Structure
from _dbus_bindings import Dictionary
from pip._internal.resolution.resolvelib.found_candidates import _iter_built_with_inserted
from _collections import defaultdict

a="aaaabbc" #this can also be list
counterexample=Counter(a)#saves elements as dict key and theit cout as dixtionary values
print(counterexample)#it prints as key value pair with number of occurencces Counter({19: 3, 5: 2, 9: 1})
print(counterexample.keys())#dict_keys([5, 9, 19])
print(counterexample.values())#dict_values([2, 1, 3])
print(counterexample.items())#dict_items([(5, 2), (9, 1), (19, 3)])
print(counterexample.most_common(1))#onw most common type
print(counterexample.most_common(2))#[('a', 4), ('b', 2)]
# to get the tuple at index 0
print(counterexample.most_common(1)[0])
print(counterexample.most_common(1)[0])#to get the most common element
print(counterexample.most_common(1)[0][0])#to get a
print(counterexample.elements())#<itertools.chain object at 0x7d13eb468ac0>
print(list(counterexample.elements()))#['a', 'a', 'a', 'a', 'b', 'b', 'c'] 

"""
named tuple is easy to create similar to struct
for example below we create 2d Structure"""
Point=namedtuple('Point', 'x,y')#created a class named Point with 2 fields x and y. Point is anme of the class. x and y are fileds separated by comma or space 
pt=Point(1,5)
print(pt)#Point(x=1, y=5)
print(pt.x,pt.y)
"""
ordered Dictionary""
Just like regular dictionary but they remember the order items were inserted. From3.7 we get these in regula dictionary as well but not in older version"""
orderdictexample= OrderedDict() #since its python 2.7 if you pass orderdictexample= {} then order is remebered
orderdictexample['b']=1
orderdictexample['c']=1
orderdictexample['d']=1
orderdictexample['a']=1
print(orderdictexample)#prints in the order in which the values are inserted OrderedDict({'b': 1, 'c': 1, 'd': 1, 'a': 1})
"""default dict: is no value is passed then the deafualy value is taken"""
defdictexample= defaultdict(int) #you specify the deafult type as int and if any value is not passed then its set as 0
defdictexample['b']=1
defdictexample['c']=1
defdictexample['d']=1
print(defdictexample)#defaultdict(<class 'int'>, {'b': 1, 'c': 1, 'd': 1, 'a': 0}), a is set 0 by default
print(defdictexample['b'])#prints 1
print(defdictexample['a'])#prints default value as 0 as its int and if float its 0.0   and if its list it will be [] and with 
#normal dictionary it will give keyerror if we pass defdictexample= {}
"""
deque double ended queeuto add and remove elemet from both ends"""
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)#to append in begiining
print(d)
d.pop()#right most element removed
print(d)
d.popleft()
print(d)
d.clear()
d.extend([6,7,8])
print(d)
d.extendleft([16,17,18])#this will be added as 8,17,16 IMPORTANT
print(d)
d.rotate(2)#to move 2 places
print(d)
d.rotate(-1)#to move one element to left
print(d)








