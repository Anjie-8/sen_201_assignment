#  A Simple Calculator Application

def  calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"

# Main program
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = calculate(first_number, second_number, op)
print("Result:", result)

