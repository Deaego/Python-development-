class Road:

    def __init__(self, width, length):
        self.weight = width
        self.length = length

    def calculation(self, thickness=5, mass_of_asphalt_on_1m=25):
        total_mass = (self.weight * self.length * mass_of_asphalt_on_1m * thickness)
        return print(total_mass)


mass = Road(120, 100, )
mass.calculation()
