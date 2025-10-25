'''
Created on Oct 24, 2025

@author: rharidas
'''


try:
    print(10/0)
except ZeroDivisionError:
    print("handled zero devision")
else:
    print("inside else")
finally:
    print("inside finnalyy")
"""
if exception then find the right except and go to finally    
if exception then couldnt find right except and go to finally    
if no exception then go o else and then finally  
"""
try:
    print(10/0)
except ValueError:
    print("ValueError")
else:
    print("inside else")
finally:
    print("inside finnalyy")
    
try:
    print(10/2)
except ZeroDivisionError:
    print("handled zero devision")
else:
    print("inside else")
finally:
    print("inside finnalyy")  
    
    
#As exception obhect
try:
    num=one
except TypeError as e:
    print("type error",e)









