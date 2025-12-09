from enum import Enum
import math

'Enum type: тип планети — земна або газова'
class PlanetType(Enum):
    TERRESTRIAL = 1
    JOVIAN = 2


'Клас Planet з усіма потрібними полями'
class Planet:
    'Конструктор'
    def __init__(self, name, mass_kg, orbital_velocity, mean_temperature,
                 length_of_day, distance_from_sun, planet_type: PlanetType):
        self.name = name
        self.mass_kg = mass_kg
        self.orbital_velocity = orbital_velocity
        self.mean_temperature = mean_temperature
        self.length_of_day = length_of_day
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    'Деструктор (для демонстрації)'
    def __del__(self):
        pass

    'Функція доступу – повна інформація про планету'
    def get_info(self):
        return (f"Назва: {self.name}, Маса: {self.mass_kg} кг, "
                f"Швидкість орбіти: {self.orbital_velocity} км/с, "
                f"Температура: {self.mean_temperature} °C, "
                f"Довжина дня: {self.length_of_day} год, "
                f"Відстань від Сонця: {self.distance_from_sun} млн км, "
                f"Тип: {self.planet_type.name}")


'Клас Planetary — колекція планет'
class Planetary:
    'Конструктор'
    def __init__(self):
        self.planets = []

    'Додати планету'
    def add_planet(self, planet: Planet):
        self.planets.append(planet)

    'Вивести всі планети'
    def show_all(self):
        for p in self.planets:
            print(p.get_info())

    'Сортування за довжиною дня'
    def sort_by_day_length(self):
        self.planets.sort(key=lambda p: p.length_of_day)


'Відстань між двома планетами (за їх відстанями від Сонця)'
def findDistanceBetween(planetA: Planet, planetB: Planet):
    return abs(planetA.distance_from_sun - planetB.distance_from_sun)


'Середня маса серед масиву планет'
def findAverageMass(planets_list):
    return sum(p.mass_kg for p in planets_list) / len(planets_list) if planets_list else 0


'MAIN — демонстрація роботи'
def main():
    'Створення планет'
    earth = Planet("Earth", 5.97e24, 29.8, 15, 24, 150, PlanetType.TERRESTRIAL)
    mars = Planet("Mars", 6.39e23, 24.1, -60, 24.6, 228, PlanetType.TERRESTRIAL)
    jupiter = Planet("Jupiter", 1.90e27, 13.1, -145, 9.9, 779, PlanetType.JOVIAN)

    'Створення системи та додавання планет'
    system = Planetary()
    system.add_planet(earth)
    system.add_planet(mars)
    system.add_planet(jupiter)

    print("=== Усі планети ===")
    system.show_all()

    print("\n=== Після сортування за довжиною дня ===")
    system.sort_by_day_length()
    system.show_all()

    print("\nВідстань між Earth та Mars:",
          findDistanceBetween(earth, mars), "млн км")

    avg_mass = findAverageMass(system.planets)
    print("\nСередня маса планет у системі:", avg_mass, "кг")


if __name__ == "__main__":
    main()
