'''
Created on Oct 23, 2025

@author: rharidas
'''
from functionsexample import *
sum(2, 4)
"""
If functionsexample andfunctionsexample1 module has same fucnion sum then write as below so that conflict is reolved
from functionsexample import *
sum(2, 4)
from functionsexample1 import *
sum(2, 4)
If its same method within 2 class in 2 modules then access with objects like below:
from a(module) import Animal (is class name)
from b(module) import Bird (is class name)
obj1=Animal()
obj1.display()
obj2=Bird()
obj2.display()
"""
#from Classesandobjects import *
import InheritanceExample
print (dir(InheritanceExample))#no of classes inside InheritanceExample
"""
If I create just ficntions without self keyword and outisde the class or without the class and with just these fucntions in the module then dir shows tat well
def add()):
if its methods with self inside class like below then its not shown.
class a:
def add()self):
"""
