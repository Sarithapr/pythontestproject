'''
Created on Oct 23, 2025

@author: rharidas
'''
#we can accress privste variables outside of the class indirectly using methods
class MyClass1:
    __empid=100#can be assessed onl within the class and not outside the class.same for methods
    def setempid(self,eid):
        self.__empid=eid
    def getEmpId(self):
        print(self.__empid)
obj2=MyClass1()
obj2.getEmpId()
obj2.setempid(123)
obj2.getEmpId()
class MyClass:
    __a=10#can be assessed onl within the class and not outside the class.same for methods
    def __disp(self):
        print("hello")
    def disp1(self):
        print(self.__a)
        self.__disp()
        
obj1=MyClass()
obj1.disp1()
#obj1.__disp()
#print(obj1.__a)
#print(MyClass.__a)
"""
to access a private variable call self.__a within a public method
to ccess a private method, create another pblic method and call this private method inside the public method"""
