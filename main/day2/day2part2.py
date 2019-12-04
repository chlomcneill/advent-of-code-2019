from itertools import product

f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day2input.txt", "r")
program = f.readlines()[0].split(',')
program = [int(val) for val in program]
f.close()


def run_program(input):
    pointer = 0
    while input[pointer] != 99:
        if input[pointer] == 1:
            input[input[pointer+3]] = input[input[pointer+1]] + input[input[pointer+2]]
            pointer += 4
        elif input[pointer] == 2:
            input[input[pointer+3]] = input[input[pointer+1]] * input[input[pointer+2]]
            pointer += 4
    return input


def find_inputs():
    combos = list(product(list(range(100)), repeat=2))
    for combo in combos:
        attempt = program.copy()
        attempt[1] = combo[0]
        attempt[2] = combo[1]
        run = run_program(attempt)
        if run[0] == 19690720:
            return combo


def main():
    (noun, verb) = find_inputs()
    return (100 * noun) + verb


print(main())