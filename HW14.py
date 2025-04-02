class Customer:
    def __init__(self, name, phone, haircut_preferences):
        self.name = name
        self.phone = phone
        self.haircut_preferences = haircut_preferences
        self.appointments = []

    def book_appointment(self, appointment):
        self.appointments.append(appointment)

class Barber(Customer):
    def __init__(self, name, per_hour, commission_rate):
        self.name = name
        self.per_hour = per_hour
        self.commission_rate = commission_rate
        self.hours_worked = 0
        self.total_earnings = 0

    def log_hours(self, hours):
        self.hours_worked += hours
        self.total_earnings += hours * self.per_hour

    def add_commission(self, commission):
        self.total_earnings += commission

class Appointment:
    def __init__(self, customer, barber, time, service, price):
        self.customer = customer
        self.barber = barber
        self.time = time
        self.service = service
        self.price = price

class Financials:
    def __init__(self):
        self.daily_income = 0
        self.expenses = 0

    def add_income(self, amount):
        self.daily_income += amount

    def add_expense(self, amount):
        self.expenses += amount

    def calculate_profit(self):
        return self.daily_revenue - self.expenses

customer1 = Customer("John Doe", "123456789", "Fade Cut")
barber1 = Barber("Mike", "987654321", 20, 0.1)

appointment1 = Appointment(customer1, barber1, "April 1, 2:00 PM", "Fade Cut", 50)
appointment2 = Appointment(customer1, barber1, "April 1, 2:00 PM", "Buzz Cut", 40)  # Attempting a double booking

print(barber1.book_appointment(appointment1))  # ✅ Successfully booked
print(barber1.book_appointment(appointment2))  # ❌ Error: Barber is already booked

