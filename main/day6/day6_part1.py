f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day6input.txt", "r")
orbits_input = f.readlines()
orbits_input = [orbit.strip('\n') for orbit in orbits_input]
f.close()


def retrieve_objects(orbit):
    object1, object2 = orbit.split(')')
    return object1, object2


def find_inner_orbits(orbits, pointer):
    orbits = [retrieve_objects(orbit) for orbit in orbits]
    inner_orbits = 0
    orbit = orbits[pointer]
    obj1, obj2 = orbit[0], orbit[1]

    if obj1 == 'COM':
        inner_orbits += 1
    else:
        inner_orbits += 1
        while obj1 != 'COM':
            for orbit in orbits:
                if orbit[1] == obj1:
                    pointer = orbits.index(orbit)
                    orbit = orbits[pointer]
                    obj1, obj2 = orbit[0], orbit[1]
                    inner_orbits += 1

    return inner_orbits


def calculate_orbits(orbits):
    total_orbits = 0
    pointer = 0

    while pointer < len(orbits):
        total_orbits += find_inner_orbits(orbits, pointer)
        # print(total_orbits)
        pointer += 1

    return total_orbits


def main():
    print(calculate_orbits(orbits_input))


# main()
# Answer: 273985



