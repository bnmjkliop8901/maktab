from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def mohit(self):
        pass

class Moraba(Shape):
    def mohit(self , x , y):
        print(f"mohit = {2*(x+y)}")

class Circle(Shape):
    def mohit(self , x):
        print(f"mohit = {3.14 * 2 * x}")

m1 = Moraba()
m1.mohit(2,3)

c1 = Circle()
c1.mohit(2)
    