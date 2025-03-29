#1

#def recursive_func(s , char):
#    print(f"s = {s}")
#    if s == "":
#        return ""
#    if s[0] == char:
#        return recursive_func(s[1:] , char)
#    else:
#        return s[0] + recursive_func(s[1:] , char)
#    
#print(recursive_func("hello" , "l"))



#2

#def nested_sum(list_1):
#    total = 0
#    for i in list_1:
#        if isinstance(i , list):
#            total += nested_sum(i)
#        else:
#            total += i
#    return total
#
#print(nested_sum([1, [2, 3], [4, [5]]]))



#3

#import time
#def my_decorator(func):
#    def wrapper(*args , **kwargs):
#        x =(time.time())
#        print(x)
#        result = func(*args , **kwargs)
#        z = (time.time())
#        print(z)
#        print(z-x)
#        return result
#    return wrapper

#@my_decorator
#def func():
#    time.sleep(2)
#    print("Function finished:")

#func()



#4

#def my_decorator(func):
#    def wrapper(*args , **kwargs):
#        print(f"starting {func.__name__}")
#        result = func(*args , **kwargs)
#        print(f"finished {func.__name__}")
#        return result
#    return wrapper

#@my_decorator
#def process_data():
#    print("processing ")


#process_data()



#4

from datetime import datetime

def restrict_hours(start , end):
    def my_decorator(func):
        def wrapper(*args , **kwargs):
            current_hour = datetime.now().hour
            if start <= current_hour <= end:
                return func(*args , **kwargs)
            else:
                print(f"the function {func.__name__} can be done in this time")
        return wrapper
    return my_decorator

@restrict_hours(start=9 , end=22)
def do_work():
    print("working...") 

do_work()