# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

# def make_alert_sound():
#     print('made alert sound.')
# def make_accept_sound():
#     print('made acceptance sound')

# ingredients = ['sodium benzoate']
# if 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients\
# or 'sodium oxide' in ingredients:
#     print('!!!')
#     print('there is a toxin in the food!')    
#     print('!!!')
#     make_alert_sound()
# else:
#     print('***')
#     print('Toxin Free')
#     print('***')
#     make_accept_sound()
def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

def check_toxins_in_food(ingredients):
    if 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients\
    or 'sodium oxide' in ingredients:
        return True
    return False

def show_toxin_warning():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()

def show_toxin_free():
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()

ingredients = ['sodium benzoate']
if check_toxins_in_food(ingredients):
    show_toxin_warning()
else:
    show_toxin_free()

