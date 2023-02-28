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

def is_toxin_present(ingredients):
    return 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients or 'sodium oxide' in ingredients

def notify_toxin_presence():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()

def notify_toxin_absence():
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()

ingredients = ['sodium benzoate']
if is_toxin_present(ingredients):
    notify_toxin_presence()
else:
    notify_toxin_absence()


