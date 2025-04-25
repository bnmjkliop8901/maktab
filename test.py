class Car():
    def __init__(self , color , vin):
        self.color = color
        self._is_on = False
        self.__vin = vin
    def getter(self):
        return self._is_on
    def setter (self , is_on):
        self._is_on = is_on
    def get(self):
        return self.__vin
    def set(self , vin):
        self.__vin = vin

    @property
    def is_on(self):
        return self._is_on
    @is_on.setter
    def is_on(self , value):
        self._is_on = value



c1 = Car("red" , 12)
print(c1.color)
print(c1.getter())
c1.setter(True)
print(c1.getter())
print(c1.get())
c1.set(13)
print(c1.get())
print(c1.is_on)
c1.is_on = False
print(c1.is_on)


