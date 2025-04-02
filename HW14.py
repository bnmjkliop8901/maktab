from datetime import datetime

class Customer:
    """Represents a customer with name, phone, haircut preferences, and appointments."""
    def __init__(self, name, phone, haircut_preferences):
        self.name = name
        self.phone = phone
        self.haircut_preferences = haircut_preferences
        self.appointments = []

    def book_appointment(self, appointment):
        """Adds appointment to customer's list."""
        self.appointments.append(appointment)

    def cancel_appointment(self, time):
        """Cancels appointment based on time."""
        appointment_to_cancel = next((appt for appt in self.appointments if appt.time == time), None)

        if appointment_to_cancel:
            self.appointments.remove(appointment_to_cancel)
            appointment_to_cancel.barber.gg.remove(appointment_to_cancel)
            return f"Appointment for {self.name} at {time} has been cancelled."
        else:
            return f"No appointment found for {self.name} at {time}."

    def __repr__(self):
        return f"Customer({self.name}, {self.phone}, {self.haircut_preferences})"


class Barber:
    """Represents a barber with name, hourly rate, commission, and appointments."""
    def __init__(self, name, phone, per_hour, commission_rate):
        self.name = name
        self.phone = phone
        self.per_hour = per_hour
        self.commission_rate = commission_rate
        self.hours_worked = 0
        self.total_earnings = 0
        self.gg = []  # Barber's appointments list

    def is_available(self, time):
        """Check if barber is free at the given time."""
        return all(appointment.time != time for appointment in self.gg)

    def book_appointment(self, appointment):
        """Book an appointment if available."""
        if self.is_available(appointment.time):
            self.gg.append(appointment)
            appointment.customer.book_appointment(appointment)
            return f"Appointment booked for {appointment.customer.name} at {appointment.time}."
        else:
            return f"Error: Barber {self.name} is already booked at {appointment.time}."

    def log_hours(self, hours):
        """Log hours worked and update earnings."""
        self.hours_worked += hours
        self.total_earnings += hours * self.per_hour

    def add_commission(self, commission):
        """Add commission earnings."""
        self.total_earnings += commission

    def __repr__(self):
        return f"Barber({self.name}, {self.phone}, {self.per_hour}/hr)"


class Appointment:
    """Represents an appointment between a customer and a barber."""
    def __init__(self, customer, barber, time, service, price):
        self.customer = customer
        self.barber = barber
        self.time = time
        self.service = service
        self.price = price

    def __repr__(self):
        return f"Appointment(Customer: {self.customer.name}, Barber: {self.barber.name}, Time: {self.time}, Service: {self.service}, Price: {self.price})"


class Financials:
    """Handles financial records including revenue and expenses."""
    def __init__(self):
        self.daily_revenue = 0
        self.expenses = 0

    def add_income(self, amount):
        """Records income from services."""
        self.daily_revenue += amount

    def add_expense(self, amount):
        """Records expenses."""
        self.expenses += amount

    def calculate_profit(self):
        """Calculates net profit."""
        return self.daily_revenue - self.expenses


# Example Usage:

# Creating customers and a barber
c1 = Customer("Soheil", 9919892093, "Buzz Cut")
c2 = Customer("Mmd", 9214910215, "Kachal")
b1 = Barber("Ali", 9214910214, 20000, 0.1)

# Logging work and commission
b1.log_hours(10)
b1.add_commission(10000)
print(b1.hours_worked)  # ✅ Hours worked
print(b1.total_earnings)  # ✅ Total earnings

# Booking appointments
appointment1 = Appointment(c1, b1, "April 1, 2:00 PM", "Fade Cut", 200000)
appointment2 = Appointment(c1, b1, "April 1, 2:00 PM", "Fade Cut", 200000)  # Duplicate booking attempt

print(b1.book_appointment(appointment1))  # ✅ Successfully booked
print(c1.cancel_appointment("April 1, 2:00 PM"))
print(b1.book_appointment(appointment2))  # ❌ Should prevent double booking

# Cancel appointment


# Financial tracking
financials = Financials()
financials.add_income(50000)
financials.add_expense(10000)

print(f"Profit: ${financials.calculate_profit()}")  # ✅ Net profit calculation
