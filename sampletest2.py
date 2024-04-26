# Code with multiple issues for SonarCloud analysis

def calculate_area(radius):
    # Magic number without explanation
    area = 3.14 * radius * radius  # Magic number issue

    # Unreachable code
    if False:
        print("This line is unreachable")

    # Unused variable
    unused_variable = "This variable is not used anywhere"

    # Concatenation instead of formatted string
    message = "The area of the circle with radius " + str(radius) + " is " + str(area)  # Concatenation issue

    return area  # Unused variable issue


def divide(a, b):
    # Division by zero
    result = a / b  # Division by zero issue
    return result


def insecure_function(command):
    # Security vulnerability: Command injection risk
    import os
    os.system(command)  # Command injection vulnerability

    # Hardcoded credentials (for demonstration purposes only, not a real credential)
    username = "admin"
    password = "password123"  # Hardcoded credentials issue


def main():
    radius = 5
    area = calculate_area(radius)
    print("Area:", area)

    result = divide(10, 0)
    print("Result:", result)

    command = "echo 'Hello, World!'"
    insecure_function(command)


if __name__ == "__main__":
    main()
