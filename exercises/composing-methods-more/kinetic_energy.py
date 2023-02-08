# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def convert_distance_to_km(distance):
    if distance.unit != 'km':
        if distance.unit == "ly":
            in_km = distance.value * 9.461e12
            return Distance(in_km, "km")
        else:
            print("unit is Unknown")
            return distance
    return distance

def convert_mass_to_kg(mass):
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            value = mass.value * 1.98892e30
            return Mass(value, 'kg')
        else:
            print("unit is Unknown")
            return mass
    return mass

def calculate_kinetic_energy(mass, distance, time):
    distance = convert_distance_to_km(distance)
    mass = convert_mass_to_kg(mass)

    if distance is None or mass is None:
        return None

    speed = distance.value/time # [km per sec]
    kinetic_energy = 0.5 * mass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))


