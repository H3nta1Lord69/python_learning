
is_old = True
is_licensed = False
if is_old and is_licensed:
    print("You can drive the car")
else:
    print("You cannot drive the car")
if is_old or is_licensed:
    print("You can drive the car")
else:
    print("You cannot drive the car")
if is_old and not is_licensed:
    print("You can drive the car")
else:
    print("You cannot drive the car")
if is_old or not is_licensed:
    print("You can drive the car")
else:
    print("You cannot drive the car")
    
# If-elif-else statement
temperature = 35
if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
    
# Nested if statement
age = 18
if age >= 18:
    print("You are old enough to vote")
    if age >= 21:
        print("You are also old enough to drink alcohol")
    else:
        print("You are not old enough to drink alcohol")
else:
    print("You are not old enough to vote")
    
# Ternary operator
is_raining = True
print("Take an umbrella") if is_raining else print("No need for an umbrella")

# Check if a number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Check if a year is a leap year
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
# Check if a person is eligible for a senior citizen discount
age = 65
if age >= 65:
    print("You are eligible for a senior citizen discount")
else:
    print("You are not eligible for a senior citizen discount")
    
# Check if a string is a palindrome
text = "racecar"
if text == text[::-1]:
    print(f'"{text}" is a palindrome')
else:
    print(f'"{text}" is not a palindrome')
    
# Check if a number is positive, negative, or zero
num = -10
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print("The number is zero")