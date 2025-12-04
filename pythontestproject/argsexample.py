"""
args is just a name and can be anything. we can pass any number of arguments and that function will add and work accordinglt
we can pass as function arguments
or we can passs fro where the function is called
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
    s=0
    for j in args:
     s=s+j
    print(s)
args = [1,3]
add1(*args)#number of araeters passed shoudl be equal to number of parameters received

"""if you wanr to pass as key argument then use **kwargs funcname(name='time,team='scholl')
"""
def testfunc1(**kargs):#should be same as key
    for i,j in kargs.items():
        print(i,j)
testfunc1(name='tom',job='qa')

def testfunc(name,job):#should be same as key
    print(name,job)
dictionarytest={"name":"hsdgh","job":"dev"}
testfunc(**dictionarytest)
    
     