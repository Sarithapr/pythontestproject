"""
args is just a name and can be anything. we can pass any number of arguments and that function will add and work accordinglt
we can pass as function arguments
or we can passs fro where the function si called
"""
from certifi.__main__ import args


def add(*args):
    s=0
    for i in args:
     s=s+i
    print(s)
add(1,2,3,4,5)
add(1,2,3)
add(1,2)    


def add1(a,b):
    print(a,b)
args = [1,3]
add1(*args)
     