# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def cooking_score(time, temperature, pressure):
    return time * temperature * pressure * COOKED_CONSTANT

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    if desired_state == 'well-done' and cooking_score(time, temperature, pressure) >= WELL_DONE: 
        return True
    if desired_state == 'medium' and cooking_score(time, temperature, pressure) >= MEDIUM:
        return True
    return False

result = is_cookeding_criteria_satisfied(20, 180, 2, 'well-done')
# print(result) # prints True or False depending on the inputs
if result:
    print("Cooking criteria satisfied.")
else:
    print("Cooking criteria not satisfied.")
