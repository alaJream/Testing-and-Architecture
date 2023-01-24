# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class pizza:
    def __init__ (self, my_bread_type, cheese_type, meat_type, pizza_toppings, size):
        self.bread_type= my_bread_type
        self.cheese_type = cheese_type
        self.meat_type= meat_type
        self.toppings = pizza_toppings
        self.size = size        
    @classmethod
    def createChicagoPizza (class_type, size):
        bread_type = 'deep-dish bread'
        cheese_type = 'mozzarella cheese'
        meat_type = 'italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return class_type (bread_type, cheese_type, meat_type, toppings, size)    
    @classmethod
    def createCaliforniaPizza(class_type, meat_type, size):
        bread_type = 'thin crust'
        cheese_type = 'feta cheese'
        toppings =['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        return class_type(bread_type, cheese_type, meat_type, toppings, size) 
    def printInfo(obj):
        print('Bread type is: ', obj.bread_type)
        print('Cheese type is: ', obj.cheese_type)
        print('Meat type is: ', obj.meat_type)
        print('Toppings are: ', end='')
        print(', '.join(map(str, obj.toppings)))

    
myPizza = pizza.createCaliforniaPizza('chicken', 'large')
myPizza.printInfo()