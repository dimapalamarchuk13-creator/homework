from enum import Enum


"""Enum type: planet type — terrestrial or jovian"""
class PlanetType(Enum):
    TERRESTRIAL = 1
    JOVIAN = 2


"""Planet class with all necessary fields"""
class Planet:
    """Represents a planet with orbital and physical characteristics."""

    def __init__(self, name, mass_kg, orbital_velocity, mean_temperature,
                 length_of_day, distance_from_sun, planet_type: PlanetType):
        """Constructor"""
        self.name = name
        self.mass_kg = mass_kg
        self.orbital_velocity = orbital_velocity
        self.mean_temperature = mean_temperature
        self.length_of_day = length_of_day
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def __del__(self):
        """Destructor (demonstration only)"""
        pass

    def get_info(self):
        """Returns full information about the planet."""
        return (f"Name: {self.name}, Mass: {self.mass_kg} kg, "
                f"Orbital velocity: {self.orbital_velocity} km/s, "
                f"Temperature: {self.mean_temperature} °C, "
                f"Day length: {self.length_of_day} h, "
                f"Distance from Sun: {self.distance_from_sun} mln km, "
                f"Type: {self.planet_type.name}")


"""PlanetSystem class — collection of planets"""
class PlanetSystem:
    """A collection (system) of planets."""

    def __init__(self):
        """Constructor"""
        self.planets = []

    def add_planet(self, planet: Planet):
        """Adds a planet to the system."""
        self.planets.append(planet)

    def show_all(self):
        """Prints all planets in the system."""
        for p in self.planets:
            print(p.get_info())

    def sort_by_day_length(self):
        """Sorts planets by their day length."""
        self.planets.sort(key=lambda p: p.length_of_day)


def findDistanceBetween(planetA: Planet, planetB: Planet):
    """Returns the absolute distance between two planets based on their distance from the Sun."""
    return abs(planetA.distance_from_sun - planetB.distance_from_sun)


def findAverageMass(planets_list):
    """Returns the average mass of a list of planets."""
    return sum(p.mass_kg for p in planets_list) / len(planets_list) if planets_list else 0


def main():
    """Demonstrates the functionality of the Planet and PlanetSystem classes."""

    """Creating planets"""
    earth = Planet("Earth", 5.97e24, 29.8, 15, 24, 150, PlanetType.TERRESTRIAL)
    mars = Planet("Mars", 6.39e23, 24.1, -60, 24.6, 228, PlanetType.TERRESTRIAL)
    jupiter = Planet("Jupiter", 1.90e27, 13.1, -145, 9.9, 779, PlanetType.JOVIAN)

    """Creating system and adding planets"""
    system = PlanetSystem()
    system.add_planet(earth)
    system.add_planet(mars)
    system.add_planet(jupiter)

    print("=== All planets ===")
    system.show_all()

    print("\n=== After sorting by day length ===")
    system.sort_by_day_length()
    system.show_all()

    print("\nDistance between Earth and Mars:",
          findDistanceBetween(earth, mars), "mln km")

    avg_mass = findAverageMass(system.planets)
    print("\nAverage mass of planets in the system:", avg_mass, "kg")


if __name__ == "__main__":
    main()
