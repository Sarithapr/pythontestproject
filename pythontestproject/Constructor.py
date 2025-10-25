'''
Created on Oct 22, 2025

@author: rharidas
'''
class ConstructorEg:
    def m1(self):
        print("hello")
    #construcor starts with __init and init is a keyword
    def __init__(self):
        print("inside constructor")
obj1=ConstructorEg();#prints "inside constructor
obj1.m1()    

#converting local variables to class variables
class ConstructorEg1:
    #doing the same below with constructor
    def __init__(self,v1,v2):
        
    #def values(self,v1,v2):#here v1 and v2 are local variables
       # print(v1)
       # print(v2)
        self.v1=v1
        self.v2=v2
    #construcor starts with __init and init is a keyword
    def add(self):
        #print(v1+v2)#here v1 and v2 are not availale as theyare normal variables so we need to convert to class variables using self.v1 and self.v2
        print(self.v1+self.v2)
obj1=ConstructorEg1(1,2);#prints "inside constructor
#obj1.values(1, 2) 
obj1.add()

#calling one method inside another
class ConstructorEg2:
    def m1(self):
        print("hello")
        self.m2(4000)
    
    def m2(self,a):
        print("inside constructor",a)
obj3=ConstructorEg2();#prints "inside constructor
obj3.m1()

#initilaizing a constructor
class ConstructorEg4:
    name="new test"
    def __init__(self,name):
        print(name)#local variable
        print(self.name)#class variable
obj4=ConstructorEg4("test")


#Example
class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid,end="")
        print(self.ename,end="")
        print(self.sal,end="")
        print("eid:{} ename:{} sal:{}".format(self.eid,self.ename,self.sal))
        print("eid:%d ename:%s sal:%g" %(self.eid,self.ename,self.sal))
        
objemp=Emp(1,"test",35000)
objemp.display()
#predefined fucntions
#__str__ and __delete__
#str is automatically invoked when refernce variable is printed
#del is invoked when objct is destroyed
class strclass:
    pass
    
objstr=strclass()#objstr is refernce variable
print(objstr)#<__main__.strclass object at 0x7602eeacb8c0> . This is internally printed by __str calss and return string. It prints the address of object


class strclass1:
    def __str__(self):#overiding __str__
        return "test"
    
objstr1=strclass1()#objstr is refernce variable
print(objstr1)

class Emp1:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):#here it should return as a string and no print statement allowerd
        return("eid:{} ename:{} sal:{}".format(self.eid,self.ename,self.sal))
        return("eid:%d ename:%s sal:%g" %(self.eid,self.ename,self.sal))
        
objemp=Emp1(1,"test",35000)
print(objemp)

class test:
    def __del__(self):
        print("destroyed")
        
test1=test()
test2=test()
del test1
del test2










  