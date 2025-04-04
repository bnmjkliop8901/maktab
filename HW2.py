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

#def parse_contacts():
#    dict = {}
#    with open("data.txt" ,"r") as file:
#        for line in file:
#            name , email = line.strip().split(",")
#            dict[name] = email
#    for name , email in dict.items():
#        print(f"{name}: {email}")
#
#parse_contacts()



#3

#def replace_content(pattern_string , replacement_string , file_input , file_output):
#    try:
#        with open (file_input , "r") as file:
#            x = file.read()
#            x.replace(pattern_string , replacement_string)
#        with open (file_output) as file:
#            file.write(x)
#    except Exception as e:
#        print(e)



#4



    
    
