#1






#2

def func(start , stop):
    lst = []
    while start < stop:
        lst.append(start)
        start += 1
    return lst

print(func(2,11))