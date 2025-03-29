#1

#import base64
#def func(str_1):
#    byte = str_1.encode("utf_8")
#    base_64 = base64.b64encode(byte)
#    return base_64
#
#print(func("hello"))



#2

#import base64
#def func(encode):
#    byte = base64.b64decode(encode)
#    str = byte.decode("utf_8")
#    return str
#
#print(func("aGVsbG8="))



#3

#def func(file_1):
#    with open (file_1 , "r") as file_1:
#        return len(file_1.readlines())
#
#print(func("ggg.txt"))



#4

#def func(num1 , num2):
#    try:
#        print("enter")
#        print(num1/num2)
#        print("exit")
#    except Exception as e:
#        print(e)
#        
#
#(func(4,0))



#5

#x = input("please enter something: ")
#with open ("output.txt" , "w") as file:
#    file.write(x)
#with open ("output.txt" , "r") as file:
#    print(file.read())



#6

#import json
#def func(dict_1):
#    encode = json.dumps(dict_1)
#    print(encode)
#    decode = json.loads(encode)
#    print(decode)
#
#func({"name": "Alice", "age": 25, "city": "Wonderland"})



#7

#def func():
#    try:
#        with open("data.txt" , "r") as file:
#            print(file.read())
#    except Exception as e:
#        print(e)
#
#func()



#8

#def func():
#    with open ("data.txt" , "r") as file:
#        x = file.read()
#    new = x.replace("Python" , "Java")
#    with open ("data.txt" , "w") as file:
#        file.write(new)
#
#print(func())



#9
#import os
#def func():
#    if os.path.exists("data.txt"):
#        with open("data.txt" , "a") as file:
#            print(file.write("hello"))
#    else:
#        with open("data.txt" , "w") as file:
#            print(file.write("kkkk"))
#
#func()



#10

#import base64
#def func(str_1):
#    byte = str_1.encode("utf_8")
#    base_64 = base64.b64encode(byte)
#    with open("encrypted.txt" , "wb") as file:
#        file.write(base_64)
#    with open("encrypted.txt" , "rb") as file:
#        x = file.read()
#    byte = base64.b64decode(x)
#    str_2 = byte.decode("utf_8")
#    print(str_2)
#
#func("Secure Data")



#11

#12

from collections import Counter 
def func():
    with open("data.txt" , "r") as file:
        x = file.read()
    words = x.split()
    print(words)
    word_count = Counter(words)
    print(word_count)
    for word , count in word_count.items():
        print(f"{word}: {count}")

func()