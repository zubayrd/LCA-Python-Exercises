# Question 1:

# Store x an y values

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

# Equations

x += 3
y *= 2
result = x / y

# Print result

print(result)

# Question 2

# Store a, b, and c values

a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

# Conditions

con1 = a > b
con2 = b % 2 == 0
con3 = c <= a

# Check if final condition is True

final_condition = (con1) or (con2 and con3)
print(final_condition)

# Question 3

# Store value 0-100

score = int(input("Enter a value from 0-100: "))

# Create grading system using if-else statements
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Question 4

# Store two numbers and an operation into variables 

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Create a formula using the variables and if-else statements

if operation == "+":
    solution = num1 + num2
    print(solution)
elif operation == "-":
    solution = num1 - num2
    print(solution)
elif operation == "*":
    solution = num1 * num2
    print(solution)
elif operation == "/":
    if num2 == 0:
        print("Division by zero is not allowed")
    else:
        solution = num1 / num2
        print(solution)
