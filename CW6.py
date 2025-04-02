class Car:
    def __init__(self , color , vin):
        self.color = color
        self._is_on = False
        self.__vin = vin
    
    @property
    def is_on(self):
        print(self._is_on)

    @is_on.setter
    def is_on(self , l):
        self._is_on = l

    def set_vin(self , x):
        self.__vin = x
    def get_vin(self):
        print(self.__vin)
    def set_is_on(self , z):
        self._si_on = z
    def get_is_on(self):
        print(self._is_on)

    def start(self):
        self._is_on = True

class Suv(Car):
    def start(self):
        print("loud noise")
        self._is_on = True

c1 = Car("red" , 1010)
c1.is_on = True
c1.is_on
