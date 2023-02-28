# by Kami Bigdely
# Remove control flag

def find_food(food, fridge):
    for item in fridge:
        if food in item:
            return item
    return None

if __name__ == "__main__":
    food = 'wesabi'
    food_list = ['onion', 'cucumber','Guacamole', 'kabob barg', 'wesabi']
    found_item = find_food(food, food_list)
    if found_item is not None:
        print(food, "Found: " + found_item)
    else:
        print(food, "not found")
