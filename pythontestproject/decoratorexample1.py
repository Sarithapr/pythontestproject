import time
from datetime import datetime,timedelta
def mytimer(base_fn):
    def enhancedfn(*args,**kwargs):# colects positional arguments into args tuple args=("green,1") Packs postionalargs into a tuple
        #collects all keyword argumets into kwargs dictionary kwargs={type="green",steeptime=1}
            print("starting")
            start=time.time()
            result=base_fn(*args,**kwargs)# if we pass as base_fn(args) then it will take as single arguments (green,1) as type and steep time foes missing so we need to split into green and 1
            #as multiple arguments ie unpacjs to separate individual positionalargumenst ie base_fn("green",1)
            #unpacks dictionary into separate keyword arguments ie base_fn(type="green",steeptime=1)
            print("result",result)
            end=time.time()
            print(f"func name is {base_fn.__name__}")
            print(f"exec time is {end-start} ")
            print("ending")
            return result
            print("enhancedfn",enhancedfn)
    print("enhancedfn",enhancedfn)
    return enhancedfn     #this is returned as partof decorator return the functios ypeError: 'NoneType' object is not callable so changed from enhancedfn() to enhancedfn
#doesnt handle return values



@mytimer
def brew(type,steeptime):
    print(f"brew tea {type}")   
    time.sleep(steeptime)
    print("end brew tea")
    
@mytimer
def matcha():
    #breakpoint() #here in header call its args=0 and basefn()
    print("matcha tea")
    time.sleep(1)
    print("end matcha tea")
    #breakpoint()
    #to calculate and return 30 min drinking window
    return  f"drink matcha by {datetime.now() + timedelta(minutes=30)}"

brew("green",1)#TypeError: mytimer.<locals>.enhancedfn() takes 0 positional arguments but 2 were given so put *agrds and *kwargs so add *args ad *kwargs in
#enhancedfn as it is called when the decorator mytimer is called

brew(type="green",steeptime=1)#this also works due to **kwargs def brew(type="green",steeptime=1): These are paasd toenhand=ced function
#breakpoint()
print(matcha())
#his prints none as retunr value is not captured. To fix this we need to capture the retunred result from base function to a variable result and rettuns that variable at the ened of the enhanced function
#this works when the brew function doesnt reurn anything 