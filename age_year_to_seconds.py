__author__ = "Rejoan"

# get age in years
def get_age():
    """Take input users age and return the age.
        Raises an ValueError when inputted age isn't
        integer.
    """
    msg = f"What is your age (in years): "
    
    try:
        age = int(input(msg))
    except ValueError:
        print(f"Inputted year is not valid.")

    return age

# calculate in seconds
def age_in_seconds(user_age):
    """Calculates user age in seconds."""
    age = user_age * 365 * 24 * 60 * 60
    return age


#driver
user_age = get_age() #gets user's age

#check is input is negative or not
if user_age < 0:
    print(f"Invalid Input! You enterd {user_age} as age.")
else:
    user_age_in_seconds = age_in_seconds(user_age)
    print(f"You are {user_age} years old.\nYour age in seconds: {user_age_in_seconds} seconds.")

print("...Program finished...")