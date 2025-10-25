'''
Created on Oct 23, 2025

@author: rharidas
'''
#Method Overiding
from pkg_resources._vendor.jaraco.context import null
class NameMethodOverriding:
    __a=10
    def greeting(self):
       return self.__a
class C(NameMethodOverriding):
    __a=20
    def greeting(self):
       return self.__a
        
obj1 = C()
print(obj1.__a)
print(obj1.greeting())

#Its is not possible to overload like in java but we can do as elow
class NameMethodLoading:
    def greeting(self,name=None):
       if name is None:
           print("hello")
       else:
           print("hello",name)
        
obj1 = NameMethodLoading()
obj1.greeting()
obj1.greeting("saritha")