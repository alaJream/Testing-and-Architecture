# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):  
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max_value(list_of_values):  
    """Get the maximum value from a list of numeric values."""
    max_value = list_of_values[0]
    for value in list_of_values:
        if value > max_value:
            max_value = value
    return max_value


list_of_values = [5, -1, 43, 32, 87, -100]
print(get_max_value(list_of_values))

############################
def extract_words_from_sentence(sentence):  
    """Extract individual words from a sentence."""
    words = sentence.split(' ')
    return words

print(extract_words_from_sentence('If you were a vegetable, you’d be a ‘cute-cumber.')) 
