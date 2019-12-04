f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day3input.txt", "r")
wires = f.readlines()
# print(wires)
wires = [wire.rstrip('\n').split(',') for wire in wires]
# print(wires)
f.close()


def get_coords_list(wire):
    coords_list = []
    current_y = 0
    current_x = 0
    for direction in wire:
        if direction[0] == 'U':
            for i in range(int(direction[1:])):
                current_y += 1
                coords_list.append([current_x, current_y])
        elif direction[0] == 'R':
            for i in range(int(direction[1:])):
                current_x += 1
                coords_list.append([current_x, current_y])
        elif direction[0] == 'D':
            for i in range(int(direction[1:])):
                current_y -= 1
                coords_list.append([current_x, current_y])
        elif direction[0] == 'L':
            for i in range(int(direction[1:])):
                current_x -= 1
                coords_list.append([current_x, current_y])
    return coords_list


def find_closest_intersection(wires):
    wire1 = wires[0]
    wire2 = wires[1]
    wire1_coords_list = get_coords_list(wire1)
    wire2_coords_list = get_coords_list(wire2)

    intersections = []
    for coord in wire1_coords_list:
        if coord in wire2_coords_list:
            intersections.append(coord)

    intersections = [abs(coord[0])+abs(coord[1]) for coord in intersections]
    intersections.sort()

    return intersections[0]


def main():
    return find_closest_intersection(wires)


print(main())







