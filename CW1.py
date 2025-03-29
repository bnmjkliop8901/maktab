#1

#def reverse_func(input_1):
#    return input_1[::-1]
#
#print((reverse_func("hello")))



#2

#def sum_func(list_1):
#    return sum(list_1)
#
#print(sum_func([1,2,3,4]))



#4

#def max_func(list_1):
#    return max(list_1)
#
#print(max_func([1,2,5,3,1]))




#5

#def func(number):
#    for i in range(number+1):
#        if i % 3 == 0 and i % 5 == 0:
#            print("FizzBuzz")
#        elif i % 5 == 0:
#            print("Buzz")
#        elif i % 3 == 0:
#            print("Fizz")
#        else:
#            print(i)
#
#func(15)



#6 

#def func(list_1 , target):
#    for i in range(len(list_1)):
#        for j in range(i+1 , len(list_1)):
#            if list_1[i] + list_1[j] == target:
#                print([i,j])
#
#func([2,7,11,15] , 9)



#7

#def func(s , t):
#    return sorted(s) == sorted(t)
#
#print(func("listen" , "silent"))



#8

#def func(list_1):
#    x = set(list_1)
#    return [i for i in x]
#
#print(func([1,2,2,3,4,4,5]))



#9

#def func(str_1):
#    counter = 0
#    for i in str_1:
#        if i == "a":
#            counter += 1
#        if i == "e":
#            counter += 1
#        if i == "i":
#            counter += 1 
#        if i == "o":
#            counter += 1
#        if i == "u":
#            counter += 1
#    return counter
#
#print(func("hello world"))



#10

#def func(list_1 , list_2):
#    x = list_1 + list_2
#    return sorted(x)
#
#print(func([1,3,5] , [2,6,4]))



#11

#def func(str_1):
#    result = []
#    for i in str_1:
#        result.append(i)
#        if result.count(i) > 1:
#            result.pop()
#            break
#    return(len(result))
#
#print(func("abcabcbb"))



#12

def func(list_1):
    result = []
    for i in list_1:
        if list_1.count(i) > 1 and i not in result:
            result.append(i)
    return result

print(func([3,2,3]))