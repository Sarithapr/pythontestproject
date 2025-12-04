'''
Created on Oct 21, 2025

@author: rharidas
'''
p,q=100,200#global variable
class MyClass:
    __a,b=1,2
    def myfunc(self):#self is a keyword that tells this method belongs to the class and this is instance method
        pass
    def display(self,name):#self is a keyword that tells this method belongs to the class
        print(name)
    """@staticmethod
    def staticmethod():#self is a keyword that tells this method belongs to the class
        print("static")"""
    @staticmethod
    def staticmethod1(self):#when we put self its taken as postional argument
        print("staticmethod1")
    def add(self):
        i,j=20,30#self is a keyword that tells this method belongs to the class and this is instance methis
        print(i+j)
        print(self.__a+self.b)
        print(p+q)
        

obj=MyClass()
obj.display("sarit")
obj.myfunc()
#MyClass.staticmethod1() For this to work you have to remove the self argument of the static method 
MyClass.staticmethod1(10)
obj.add()
"""
For nonam methods self is referred to saying it belongs to the class
for static method, when we put self its taken as postional argument
"""
class objectidclass:
    def myfunc(self):
        pass
    
    
newobj = objectidclass()
print(id(newobj))
newobj1 = objectidclass()
print(id(newobj1))
newobj2=newobj1
print(id(newobj2))
print(newobj is newobj1)
print(newobj is not newobj1)
print(newobj2 is newobj1)
print(newobj2 is not newobj1)
#All variables have same name
p,q=100,200#global variable
class MyClass1:
    p,q=1,2#class varible
    def add(self):
        p,q=20,30#self is a keyword that tells this method belongs to the class and this is instance methis method variable
        print(p+q)
        print(self.p+self.q)
        print(globals()['p']+globals()['q'])
        #creating mutiple object for a class. Obje is physical so stored in memeory wehere class is blueprint and not saved
print("obj2")
obj2=MyClass1();#named object
obj2.add()
print("obj3 ")
obj3=MyClass1();
obj3.add()
#unnamed object and this concept is there in java also
MyClass1.add();#for this to work you need to make it static
        





