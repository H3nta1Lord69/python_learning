
# Input from User
name = input("Enter your name: ")
print("Hello, " + name + "!")
age = input("Enter your age: ")
print("You are " + age + " years old.")
height = input("Enter your height in cm: ")
print("You are " + height + " cm tall.")
weight = input("Enter your weight in kg: ")
print("You weigh " + weight + " kg.")
bmi = (float(weight) / (float(height) / 100) ** 2)
print("Your BMI is: " + str(round(bmi, 2)))
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
# Calculate BMI
# BMI = weight (kg) / (height (m))^2
# Note: height is converted from cm to m by dividing by 100
# Round BMI to 2 decimal places
# Display BMI
print("Thank you for using the BMI calculator!")

# What is BMI?
# BMI (Body Mass Index) is a measure of body fat based on height and weight.
# It is used to categorize individuals into different weight categories.
# Categories:
# Underweight: BMI < 18.5
# Normal weight: 18.5 <= BMI < 24.9
# Overweight: 25 <= BMI < 29.9
# Obesity: BMI >= 30

# Note: This is a simple BMI calculator and does not account for muscle mass, bone density, etc.