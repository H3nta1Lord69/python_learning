
# Kinda register
# Get user input and print a summary
# Name, birthdate, email, phone number, password
def get_user_info():
    print("Welcome to the Kinda Register!")
    
    name = input("Please enter your full name: ")
    birthdate = input("Please enter your birthdate (YYYY-MM-DD): ")
    email = input("Please enter your email address: ")
    phone_number = input("Please enter your phone number: ")
    password = input("Please create a password: ")
    
    print("\nThank you for registering! Here is the information you provided:")
    card = f"""
    Name: {name}
    Birthdate: {birthdate}
    Email: {email}
    Phone Number: {phone_number}
    Password: {'*' * len(password)}"""  # Masking the password for security
    print(card)
    
get_user_info()