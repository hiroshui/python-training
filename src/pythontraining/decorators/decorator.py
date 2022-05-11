import time
from functools import wraps

def hello_world():
    print("hello world")
    
greeting = hello_world

#greeting()

def my_simple_decorator(func):
    print("Decorating the function")
    func()
    
#my_simple_decorator(hello_world)

def my_decorator(func):
    def wrapper():
        print("before wrapped")
        func()
        print("after wrapped")
    return wrapper

#say_hello = my_decorator(hello_world)

#say_hello()
#
@my_decorator
def test():
    print("tter")
    
test3 = test

#test3()

# Exercise
def timer(func):
    def wrapper():
        now_t = time.perf_counter()
        result = func()
        then_t = time.perf_counter()
        dif_time_t = then_t - now_t
        print(f"Run time was {dif_time_t} seconds.")
        return result
    return wrapper

@timer
def do_something():
    """Toy function to keep Python busy"""
    return "-".join(str(n) for n in range(1_000_000))

#do_timer = timer()
#do_timer()

y = do_something()

def timer_new(func):
    @wraps(func)
    def wrapper():
        now_t = time.perf_counter()
        result = func()
        then_t = time.perf_counter()
        dif_time_t = then_t - now_t
        print(f"Run time was {dif_time_t} seconds.")
        return result
    return wrapper

@timer_new
def do_something_new():
    """Toy function to keep Python busy"""
    return ";".join(str(n) for n in range(1_000_000))

x = do_something_new()

print("hello world")