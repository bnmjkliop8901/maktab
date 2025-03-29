#1

#number = int(input("please enter number: "))
#counter = 0
#for i in range(1 , number):
#    if number % i == 0:
#        counter += i
#if counter == number:
#    print("YES")
#else:
#    print("NO")



#2

#number = int(input("please enter number: "))
#
#while number % 2 == 0:
#    number /= 2
#    print(number)
#if number == 1:
#    print("YES")
#else:
#    print("NO")
     


#3

#from datetime import datetime
#n = input("please enter date YYYY/MM/DD: ")
#date = datetime.strptime(n , "%Y/%m/%d")
#print(f"date : {date}")




#4

#i = int(input("please enter a number: "))
#
#z = [1,2,2,3,4,4,5]
#a = [1,2]
#b = [3,4]
#happiness = 0
#
#if i in z and i in a:
#    happiness += 1
#if i in z and i in b:
#    happiness -= 1
#if i in z and i not in a and i not in b:
#    happiness += 0 



#5
#
#number = int(input("please enter number: "))
#
#print(int(((bin(number)[2:])[::-1]) , 2))