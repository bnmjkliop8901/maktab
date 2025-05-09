class Customer:

    def __init__(self, name, phone, haircut_preferences):
        self.name = name
        self.phone = phone
        self.haircut_preferences = haircut_preferences
        self.appointments = []

    def book_appointment(self, appointment):

        self.appointments.append(appointment)

    def cancel_appointment(self, time):

        appointment_to_cancel = next((appt for appt in self.appointments if appt.time == time), None)

        if appointment_to_cancel:

            appointment_to_cancel.barber.gg.remove(appointment_to_cancel)
            return f"Appointment for {self.name} at {time} has been cancelled."
        else:
            return f"No appointment found for {self.name} at {time}."

    def __repr__(self):
        return f"Customer({self.name}, {self.phone}, {self.haircut_preferences})"


class Barber:

    def __init__(self, name, phone, per_hour, commission_rate):
        self.name = name
        self.phone = phone
        self.per_hour = per_hour
        self.commission_rate = commission_rate
        self.hours_worked = 0
        self.total_earnings = 0
        self.gg = []  

    def is_available(self, time):

        return all(appointment.time != time for appointment in self.gg)

    def book_appointment(self, appointment):

        if self.is_available(appointment.time):
            self.gg.append(appointment)
            appointment.customer.book_appointment(appointment)
            return f"Appointment booked for {appointment.customer.name} at {appointment.time}."
        else:
            return f"Error: Barber {self.name} is already booked at {appointment.time}."

    def log_hours(self, hours):

        self.hours_worked += hours
        self.total_earnings += hours * self.per_hour

    def add_commission(self, commission):

        self.total_earnings += commission

    def __repr__(self):
        return f"Barber({self.name}, {self.phone}, {self.per_hour}/hr)"


class Appointment:

    def __init__(self, customer, barber, time, service, price):
        self.customer = customer
        self.barber = barber
        self.time = time
        self.service = service
        self.price = price

    def __repr__(self):
        return f"Appointment(Customer: {self.customer.name}, Barber: {self.barber.name}, Time: {self.time}, Service: {self.service}, Price: {self.price})"


class Financials:

    def __init__(self):
        self.daily_revenue = 0
        self.expenses = 0
        self.barber_earnings = {} 
        self.service_popularity = {}

    def add_income(self, barber, service, amount):
        
        self.daily_revenue += amount
        
        if barber.name in self.barber_earnings:
            self.barber_earnings[barber.name] += amount
        else:
            self.barber_earnings[barber.name] = amount
        
        if service in self.service_popularity:
            self.service_popularity[service] += 1
        else:
            self.service_popularity[service] = 1
        
    def add_expense(self, amount):
        self.expenses += amount

    def calculate_profit(self):
        return self.daily_revenue - self.expenses
    
    def top_barber(self):
        return max(self.barber_earnings, key=self.barber_earnings.get)

    def most_popular_service(self):
        return max(self.service_popularity, key=self.service_popularity.get)






c1 = Customer("Soheil", 9919892093, "Cut")
c2 = Customer("Mmd", 9214910215, "Kachal")
b1 = Barber("Ali", 9214910214, 20000, 0.1)
b2 = Barber("Dog" , 921 , 20000 , 0.2)

b1.log_hours(10)
b1.add_commission(10000)
print(b1.hours_worked)  
print(b1.total_earnings)  


appointment1 = Appointment(c1, b1, "April 1, 2:00 PM", "Cut", 200000)
appointment2 = Appointment(c1, b1, "April 1, 2:00 PM", "Cut", 200000)  

print(b1.book_appointment(appointment1))  
print(c1.cancel_appointment("April 1, 2:00 PM"))
print(b1.book_appointment(appointment2))  





financials = Financials()
financials.add_income(b1 , "Cut" ,1)
financials.add_expense(10000)

 

print(f"Top Barber: {financials.top_barber()}")
print(f"Most Popular Service: {financials.most_popular_service()}")


print(financials.service_popularity)