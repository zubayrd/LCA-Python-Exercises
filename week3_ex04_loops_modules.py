# Question 1

# Create a list of fruits

fruits = ["apple", "banana", "mango", "watermelon"]

# Use a for loop to print each fruit in the list

for fruit in fruits:
    print(fruit)

# Question 2

# Use a while loop to create the countdown

count = 5
while count >= 1:
    print(count)
    count -= 1

# Question 3

# Use for loop in range

for i in range(1, 11):
    print(i ** 2)

# Question 4

import random

# Create a list of colours

colours = ["blue", "green", "yellow", "red", "pink", "purple", "black"]

# Use for loop to print 3 random colours

for _ in range(3):
    print(random.choice(colours))
