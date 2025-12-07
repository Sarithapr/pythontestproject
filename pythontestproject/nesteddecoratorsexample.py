def logginex(basefn):
    def enhancedfn(*args,**kwargs):
        print(f"Logging {basefn.__name__}")
        result=basefn(*args,**kwargs)
        print(f"End Logging {basefn.__name__}")
        return result
    return enhancedfn




@logginex
def loggingexample(order_id):
    print("starting")
    print(f"Processing order #{order_id}")
    print("ending")

loggingexample(100)


import random
import time

def retry(times):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times+1):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    time.sleep(1)
            print("All retry attempts failed.")
        print(wrapper)
        return wrapper
    print(decorator)
    return decorator

@retry(times=3)
def flaky_operation():
    if random.random() < 0.7:
        raise ValueError("Network issue")
    return "Success"

print(flaky_operation())
