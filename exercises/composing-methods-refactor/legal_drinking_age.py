# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 21


class Person:
    def __init__(self, my_age):
        self.age = my_age


def enter_night_club(individual):
    print("Allowed to enter.") if individual.age > LEGAL_DRINKING_AGE else print(
        "Enterance of minors is denited.")


# function not needed
# def older_than_18_year_old(age):
#     if age > LEGAL_DRINKING_AGE:
#         return True
#     else:
#         return False


person = Person(20.9)
enter_night_club(person)
