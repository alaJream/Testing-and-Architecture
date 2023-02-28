class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def convert_distance_to_km(distance):
    if distance.unit == 'km':
        return distance.value
    elif distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
        # convert from light-year to km unit
        in_km = distance.value * 9.461e12
        return in_km
    else:
        print("distance unit is unknown")
        return None

def convert_mass_to_kg(mass):
    if mass.unit == 'kg':
        return mass.value
    elif mass.unit == "solar-mass":
        # convert from solar mass to kg
        value = mass.value * 1.98892e30 # [kg]
        return value
    else:
        print("mass unit is unknown")
        return None

def calculate_kinetic_energy(mass, distance, time):
    distance_in_km = convert_distance_to_km(distance)
    if distance_in_km is None:
        return None

    mass_in_kg = convert_mass_to_kg(mass)
    if mass_in_kg is None:
        return None

    speed = distance_in_km / time # [km per sec]
    kinetic_energy = 0.5 * mass_in_kg * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))