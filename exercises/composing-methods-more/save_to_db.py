# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into database")

username = input('Please enter your username: ')
save_into_db(username)

birth_year_input = int(input('Please enter your birth year: '))
current_year = 2023
age = current_year - birth_year_input
print("You are", age, "years old.")

