class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.circle_radius = diameter / 2

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.circle_radius

    def calculate_area(self):
        return self.__pi * (self.circle_radius * self.circle_radius)

    def calculate_area_of_sector(self, angul):
        return (angul / 360) * self.__pi * self.circle_radius * self.circle_radius


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
