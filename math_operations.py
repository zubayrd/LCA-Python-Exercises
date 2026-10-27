# Question 5

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
# Import custom module

import math_operations

# Use while loop to create a simple calculator

while True:
    print("\n---Simple Calculator---")
    print("1. Add")
    print("2. Subract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "5":
        print("Goodbye.")
        break
    
    elif choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if choice == "1":
            result = math_operations.add(num1, num2)
        elif choice == "2":
            result = math_operations.subtract(num1, num2)
        elif choice == "3":
            result = math_operations.multiply(num1, num2)
        elif choice == "4":
            result = math_operations.divide(num1, num2)

        print(f"Result: {result}")

    else:
        print("Invalid choice, please try again")
