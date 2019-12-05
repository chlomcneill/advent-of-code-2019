f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day1input.txt", "r")
masses = f.readlines()
masses = [int(mass[:-1]) for mass in masses]
f.close()


def calculate_fuel(mass):
    return int(mass / 3) - 2


def main():
    total_fuel = 0
    for mass in masses:
        total_fuel += calculate_fuel(mass)
    return total_fuel


# print(main())



