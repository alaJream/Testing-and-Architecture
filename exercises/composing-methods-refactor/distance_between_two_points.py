# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math
# ~~~~~~ Second block ~~~~~~
# extract distance 
def distance(xc1, yc1, xc2, yc2):
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

distance = distance(4, 4.25, 53, -5.35)
print('distance', distance)
# ~~~~~~ Second block ~~~~~~
# extract length
def length(xa, ya, xb, yb):
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

length = length(-36, 97, .34, .91)
print('length', length)