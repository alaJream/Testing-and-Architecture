# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add_ingredient(mix, ingredient):
    mix.append(ingredient)
    return mix

def make_drink(drink, addons):
    mix = []
    if 'coffee' in drink:
        mix = add_ingredient(mix, 'coffee')
    elif 'strawberry milkshake' in drink:
        mix = add_ingredient(['ice', 'cream'], 'strawberry')
    mix = add_ingredient(mix, addons)
    return mix

final_drink = make_drink('strawberry milkshake', ['milk', 'sugar'])
print(final_drink)
