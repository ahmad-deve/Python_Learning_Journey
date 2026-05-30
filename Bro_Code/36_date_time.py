import datetime

def get_the_age(birth_year):
    # Get the current date
    today = datetime.date.today()
    age = today.year - int(birth_year)
    
    return f"You are {age} years old."

# Get user input once
user_input = input("Enter your birth year (e.g., 1995): ")

# Call the function and print the result
print(get_the_age(user_input))