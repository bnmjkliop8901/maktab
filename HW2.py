#1

#def basic_calculator(num1 , num2 , operator):
#    try:
#        if operator == "+":
#            print( num1 + num2 )
#        elif operator == "-":
#            print( num1 - num2 )
#        elif operator == "/":
#            print( num1 / num2 )
#        elif operator == "*":
#            print( num1 * num2 )
#    except Exception as e:
#        print(e)
#
#basic_calculator(4,2,"+")



#2

def parse_contacts():
    dict = {}
    with open("data.txt" ,"r") as file:
        for line in file:
            name , email = line.strip().split(",")
            dict[name] = email
    for name , email in dict.items():
        print(f"{name}: {email}")

parse_contacts()