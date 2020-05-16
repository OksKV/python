# Task 1
variable1 = 10
variable2 = 4.5
print("This is an example of integer number: " + str(variable1) + "\nAnd this is an example of float number: " + str(
    variable2))

name = input("What is your name?")
age = input("How old are you?")
print(f"Hey, {name}! You don\'t look like you\'re {age} years old!")

# Task 2 - Time converter
time = int(input("How many seconds did you spend to do this homework?"))
hours = time // 3600
min = (time // 60) % 60
sec = time % 60
print(f"You\'ve spent {hours}:{min}:{sec} for your homework??? Wow!")

# Task 3 Sum of numbers
num = int(input("Give me some integer number."))
total_sum = num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num))
print(f"The sum of {num}, {num}{num} and {num}{num}{num} will be: {total_sum}")

# Task 4 The biggest element
num = int(input("Give me some big random number."))
num_max = 0
for i in str(num):
    if num_max < int(i):
        num_max = int(i)
    else:
        continue
print(f"Methode 1. \nThe biggest element in this number is: {num_max}")

# Or with While loop
while num > 0:
    num = num // 10
    a = num % 10
    if a > num_max:
        num_max = a
    else:
        continue
print(f"Methode 2. \nThe biggest element in this number is: {num_max}")

# Task 5 Income calculation
revenue = int(input("Please insert your Company's revenue"))
costs = int(input("Please insert your Company's costs"))
if revenue <= costs:
    print("Sorry, your company is operating at a loss")
else:
    income = revenue - costs
    profitability = int(income / revenue * 100)
    print(f"Congratulations, you have a profit! \nYour profitability index is {profitability}%")
    workers = int(input("How many workers are in your Company?"))
    income_per_person = int(income / workers)
    print(f"The company's income per person is {income_per_person}$")

# Task 6 Sportsman
start_distance = int(input("How many kilometers a sportsman did on first day?"))
required_distance = int(input("What is a required distance for him?"))
day_num = 0
while int(start_distance) != required_distance:
    day_num += 1
    start_distance += start_distance * 0.1
print(f"The sportsman will do {required_distance} kilometers on the day {day_num}")