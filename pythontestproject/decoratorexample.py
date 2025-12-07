import functools

def decorator1(fn):
    @functools.wraps(fn)
    def wrapper1(*args, **kwargs):
        print(fn.__name__)
        print("Decorator 1: before")
        result = fn(*args, **kwargs)
        print("Decorator 1: after")
        return result
    return wrapper1


def decorator2(fn):
    @functools.wraps(fn)
    def wrapper2(*args, **kwargs):
        print(fn.__name__)
        print("Decorator 2: before")
        result = fn(*args, **kwargs)
        print("Decorator 2: after")
        return result
    return wrapper2


@decorator1
@decorator2
def greet(name):
    print(f"Hello, {name}!")


greet("Sara")