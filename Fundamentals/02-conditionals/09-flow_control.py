
# flow control with if, elif, and else statements
def categorize_number(num):
    if num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    else:
        return "Positive"
# Testing the function
print(categorize_number(-5))  # Negative
print(categorize_number(0))   # Zero
print(categorize_number(7))   # Positive