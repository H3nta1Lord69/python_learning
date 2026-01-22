
# Candidate evaluation Program
# Get name, age, experience, and skills from the user

# Validate if has +3 years of experience and knows Python or JavaScript: Excellent
# If has +1 year of experience and knows Django or React: Good
# If has less than 1 year of experience and knows HTML/CSS: Beginner
# Otherwise: Not qualified

name = input("Enter your name: ")
age = int(input("Enter your age: "))
experience = float(input("Enter your years of experience: "))
skills = input("Enter your skills (comma separated): ").lower().split(',')
skills = [skill.strip() for skill in skills]
qualified = False
if experience >= 3 and ('python' in skills or 'javascript' in skills):
    qualified = True
elif experience >= 1 and ('django' in skills or 'react' in skills):
    qualified = True
elif experience < 1 and ('html' in skills or 'css' in skills):
    qualified = True
if qualified:
    print(f"Congratulations {name}, you are qualified for the position!")
else:
    print(f"Sorry {name}, you do not meet the qualifications for the position; but we will keep your resume on file.")