# Question 1

# Define function

def greet():
    print("Hello World!")

# Call the function

greet()

# Question 2

# Store name in variable

name = input("Enter your name: ")

# Create greeting function

def personalized_greeting(name):
    print(f"Hello, {name}")

# Call greeting function

personalized_greeting(name)

# Question 3

# Store number in a variable

num1 = int(input("Enter a number: "))

# Create a square function
 
def square(num1):
    return num1 ** 2

# Call square function

square(num1)

# Question 4

# Store length and width in variables

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Create a function for the area of the rectangle

def rectangle_area(length, width):
    return length * width

# Call and print area

area = rectangle_area(length, width)
print(area)

# Question 5

# Store number in variable

num2 = int(input("Enter a number: "))

# Create functions

def apply_opertaion(function, num2):
    return function(num2)

def double(num2):
    return num2 * 2

# Print results

result1 = apply_opertaion(double, 7)
print(result1)

result2 = apply_opertaion(square,3)
print(result2)
