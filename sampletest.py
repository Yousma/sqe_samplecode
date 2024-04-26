//codesmell issue
def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

//bug issue
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)

//vulnerability issue
import os

def delete_file(filename):
    os.remove(filename)
    print(f"{filename} deleted successfully!")

//security hotspot issue
import subprocess

def run_command(command):
    subprocess.run(command, shell=True)

//covergae issue
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

//duplications issue
def calculate_area_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def calculate_area_sphere(radius):
    pi = 3.14
    area = 4 * pi * radius * radius
    return area

//code complexity issue
def calculate_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

//maintainability issue
def process_data(data):
    # Complex data processing logic here
    result = ...
    return result

//reliability issue
def process_data(data):
    # Complex data processing logic here
    result = ...
    return result

