# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into database")

def get_username_from_user():
    return input('Please enter your username: ')

def get_birth_year_from_user():
    return int(input('Please enter your birth year: '))

username = get_username_from_user()
save_into_db(username)
birth_year = get_birth_year_from_user()
age = 2020 - birth_year
print("You are", age, "years old.")

