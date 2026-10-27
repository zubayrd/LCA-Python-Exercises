# Question 1

# Create a list of fruits

fruits = ["apple", "banana", "pear", "watermelon"]

# Add orange to the end of the list

fruits.append("orange")

# Add mango to the beginning of the list

fruits.insert(0, "mango")

# Remove banana from the list

fruits.remove("banana")

# Print the outcome

print(fruits)

# Question 2

# Create list of numbers (1-5)

numbers = [1, 2, 3, 4, 5]

# Create a list for squared numbers in previous list

squared_numbers = [x ** 2 for x in numbers]

# Find average

total_sum = sum(numbers)
average = total_sum / len(numbers)

# Print results

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Total sum:", total_sum)
print("Average:", average)

# Question 3

# Create a dictionary of countries and their capitals

capitals = {
    "South Africa": "Cape Town",
    "France":"Paris",
    "Japan":"Tokyo",
    "Germany":"Berlin"
}

# Add a new country-capital pair

capitals["Egypt"] = "Cairo"

# Update the capital of an existing country

capitals["South Africa"] = "Pretoria"

# Remove a country-caoital pair

del capitals["Germany"]

# Print dictionary

print(capitals)

# Question 4

# Create a dictionary of fruit colours

fruit_colours = {
    "apple":"red",
    "banana":"yellow",
    "orange":"orange",
    "grape":"purple"
    }

# Print all the fruits

print("Fruits:",fruit_colours.keys())

# Print all the colours

print("Colours:",fruit_colours.values())

# Print each fruit and its colour

for fruit, colour in fruit_colours.items():
    print(f"{fruit}: {colour}")

# Check if fruit is in dictionary and print its colour

fruit_check = input("Enter a fruit: ")

if fruit_check in fruit_colours:
    print(f"The colour of {fruit_check} is {fruit_colours[fruit_check]}.")
else:
    print(f"{fruit_check} is not in the dictionary")
