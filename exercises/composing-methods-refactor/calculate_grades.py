# Make code more modular
# divide up the functions to do one thing

import math

# calculate mean
# pass grades as parameter 
def calc_mean(grades): 
    total = sum(grades)
    mean = total / len(grades)
    return mean

# calculate standard deviation
def calc_sd(grades, mean):
    sum_of_sqrs = 0
    for grade in grades:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grades))
    return sd

# print
def print_stat(grades):
    mean = calc_mean(grades)
    sd = calc_sd(grades, mean)
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

grades = []
# numer of inputs
n_student = 5
for _ in range(n_student):
    grades.append(int(input('Enter a number: ')))

print_stat(grades)