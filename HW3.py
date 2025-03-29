#1

#from functools import reduce
#people = [
#    {"name":"Ali" , "age" : 16},
#    {"name":"Reza" , "age" : 20},
#    {"name":"Shima" , "age" : 25},
#    {"name":"Sara" , "age" : 15}
#]
#z = (list(filter(lambda x:x["age"] > 18 , people )))
#print(z)
#v = list(map(lambda x: f"{x["name"]}({x["age"]})" , z))
#print(v)
#print(reduce(lambda x , _ : x + 1 , v, 0))



#2

#students = [
#    {"name":"Ali" , "grade" : 18},
#    {"name":"Reza" , "grade" : 25},
#    {"name":"Shima" , "grade" : 19},
#    {"name":"Sara" , "grade" : 14}
#]

#z = list(filter(lambda x:x["grade"] > 18 , students))
#print(z)
#y = list(map(lambda x: f"{x["name"]}" , z))
#print(y)



#3

products = [
    {"name":"Laptop" , "price":150000 , "stock":0},
    {"name":"Mouse" , "price":30000 , "stock":50},
    {"name":"Keyboard" , "price":40000 , "stock":20},
    {"name":"Monitor" , "price":200000 , "stock":10},
]

print(list(filter(lambda x:x["price"] < 50000 and x["stock"] > 0 , products)))