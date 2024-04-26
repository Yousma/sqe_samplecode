# Python code with various issues for SonarCloud analysis

# Code Smells
def calculate_area(radius):
    # Magic number without explanation
    area = 3.14 * radius * radius

    # Unused variable
    unused_variable = "This variable is not used anywhere"

    return area


# Security Hotspots
def insecure_function(command):
    import os
    os.system(command)  # Command injection vulnerability

    # Hardcoded credentials (for demonstration purposes only)
    username = "admin"
    password = "password123"  # Hardcoded credentials issue


# Duplications
def calculate_circumference(radius):
    pi = 3.14
    circumference = 2 * pi * radius
    return circumference

def calculate_circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


# Consistency Issues
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")


class Truck:  # Inconsistency in naming (Car vs. Truck)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Truck: {self.year} {self.make} {self.model}")


# Adaptability Issues
def process_data(data):
    # Inflexible processing logic
    result = data * 2
    return result


# Technical Debt
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    radius = 5
    area = calculate_area(radius)
    print("Area:", area)

    command = "echo 'Hello, World!'"
    insecure_function(command)

    car1 = Car("Toyota", "Camry", 2020)
    car1.display_info()

    truck1 = Truck("Ford", "F-150", 2022)
    truck1.display_info()

    data = 10
    processed_data = process_data(data)
    print("Processed Data:", processed_data)

    interest = calculate_interest(1000, 5, 2)
    print("Interest:", interest)
