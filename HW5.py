class Employee:
    def __init__(self , name , employee_id , salary):
        self._name = name
        self._employee_id = employee_id
        self.__salary = salary

    @property
    def get_salary(self):
        print(self.__salary)
    
    @get_salary.setter
    def get_salary(self , value):
        if value > 0:
            self.__salary = value
        else:
            print("insufficient")
    def get_details(self):
        print(self._name ,self._employee_id , self.get_salary)

class Manager(Employee):
    def __init__(self , name ,employee_id , salary , department):
        super().__init__(name , employee_id , salary)
        self._department = department



    def get_department(self):
        print(self._department)
    def set_department(self , x):
        self._department = x
