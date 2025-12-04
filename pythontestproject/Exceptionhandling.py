'''
Created on Oct 24, 2025

@author: rharidas
example type error eg 5+"tests", name error del a rint(a) or a=2 b=c then name error as c is undefined, zero division error, key error,stop iteration error
imprt somemodule: module not found error
file not found
value error
a=[1,2,3]
a.remove(4)
raises value error
a[5] raised index error
a={'name':"dshdgh"}
a['age'] raises key error


'''
#creating our own exception
class ValueTooHighError(Exception):
    pass
class ValueTooLowError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value
def test_value(x):
    if x>100:
        raise ValueTooHighError("value too big")
    if x<5:
        raise ValueTooLowError("value too low",x)#value too low 1
try:
    test_value(1)#ValueTooHighError: value too big or value too low 1
except ValueTooHighError as e:
    print(e) #prints value too big if without try it will raise exception and stops exceution
except ValueTooLowError as e:
    print(e.message,e.value)
    
print("if no exception then go o else and then finally  ")
try:
    print(10/2)
except ZeroDivisionError:
    print("handled zero devision")
else:
    print("inside else")
finally:
    print("inside finnalyy")  
print("if exception then find the right except and go to finally  ")
try:
    print(10/0)
except ZeroDivisionError:
    print("handled zero devision")
else:
    print("inside else")
finally:
    print("inside finnalyy")
"""
or

except Exception as e:
    print(e)#prints division by zero  message by ZeroDivisionError class 


or
a=5/1
b=5+"test"
except ZeroDivisionError as e:
    print(e)
except typeError as e:
    print(e)//this is raised and 5/0 then zero error is raised. The first one is caught and rest are ignored once you fix first then second is caught




if exception then find the right except and go to finally    
if exception then couldnt find right except and go to finally    
if no exception then go o else and then finally  
"""

#to raise an Exception
y=-4
assert (y>0),"y greater than 0"#AssertionErrorAssertionError: y greater than 0
x=-5
if x<0:
    raise Exception("x should be graeter than 0)")#Exception: x should be graeter than 0)




print("if exception then couldnt find right except then it prints error")
try:
    print(10/0)
except ValueError:
    print("ValueError")
else:
    print("inside else")
finally:
    print("inside finnalyy")




#Array index out of bund is similar to index out of range error
    
#As exception obhect
try:
    num=one
except TypeError as e:
    print("type error",e)
    
 
    
    









