import os
class Test:
    def __init__(self , name):
        self.name = name
        with open(self.name , "w") as file:
            file.write("hello im soheil")
    
    @property
    def read_file(self):
        with open(self.name ,"r") as file:
            print(file.read())

    @read_file.setter
    def read_file(self , x):
        with open(self.name , "a") as file:
            print(file.write(x))

    @read_file.deleter
    def read_file(self):
        os.remove(self.name)
        print("file_removed")

t1 =Test("soheil.txt")
t1.read_file
t1.read_file = "goodbye"
t1.read_file
del t1.read_file