'''
Created on Oct 22, 2025

@author: rharidas
'''
class parent1:
    p,q=6,2#class varible
    def __init__(self):
        print("inside parent constructor")
        
    def m1(self):
        print("inside m1")
    def m2(self):
        print("inside m2")
    def m3(self):
        print("inside m3")

p,q=100,200#global variable
class child1(parent1):
    p,q=1,2#class varible
    def m4(self):
        print("inside m4")
        super().m1()
    def __init__(self):
        print("inside child constructor")#if there is no child constructor then parent constructor is invoked by deafult
        super().__init__()
        #parent1.__init__() Either super or parent class name
    def add(self):
        p,q=20,30#self is a keyword that tells this method belongs to the class and this is instance methis method variable
        print(p+q)
        print(super().p+super().q)
        print(self.p+self.q)
        print(globals()['p']+globals()['q'])
        
childobj=child1()
childobj.m4()
childobj.add()