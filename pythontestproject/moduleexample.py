'''
Created on Oct 23, 2025

@author: rharidas

'''
import sys,os
from functionsexample import *
from pip._internal.utils.filesystem import directory_size
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
#dir(os) gives name of different fucntions part of os module
"""
os.getcwd()
os.listdir()to get files in particular directory
dir(modulename) gives all build in methods or mafic methods+custom functions inside the module
module are searched in cwd,path in windows and anything specified in python when installed
import sys
sys.path gives the moddules in the path which python searches
"""
print(sys.path)
