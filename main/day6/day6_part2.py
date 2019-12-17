f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day6input.txt", "r")
orbits_input = f.readlines()
orbits_input = [orbit.strip('\n') for orbit in orbits_input]
f.close()


def retrieve_objects(orbit):
    object1, object2 = orbit.split(')')
    return [object1, object2]


def find_inner_orbits(orbits, pointer):
    inner_orbits = []
    orbit = orbits[pointer]
    obj1, obj2 = orbit[0], orbit[1]

    if obj1 == 'COM':
        inner_orbits += [orbit]
    else:
        inner_orbits += [orbit]
        while obj1 != 'COM':
            for orbit in orbits:
                if orbit[1] == obj1:
                    pointer = orbits.index(orbit)
                    orbit = orbits[pointer]
                    obj1, obj2 = orbit[0], orbit[1]
                    inner_orbits += [orbit]

    return inner_orbits


def calculate_minimum_orbital_transfers(orbits):
    orbits = [retrieve_objects(orbit) for orbit in orbits]

    for orbit in orbits:
        if orbit[1] == 'YOU':
            you_pointer = orbits.index(orbit)

    for orbit in orbits:
        if orbit[1] == 'SAN':
            santa_pointer = orbits.index(orbit)

    you_inner_orbits = find_inner_orbits(orbits, you_pointer)
    santa_inner_orbits = find_inner_orbits(orbits, santa_pointer)

    for you_orbit in you_inner_orbits:
        for santa_orbit in santa_inner_orbits:
            if santa_orbit[0] == you_orbit[0]:
                return you_inner_orbits.index(you_orbit) + santa_inner_orbits.index(santa_orbit)


def main():
    print(calculate_minimum_orbital_transfers(orbits_input))


# main()
# Answer: 460



