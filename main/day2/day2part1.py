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

def main():
    program[1] = 12
    program[2] = 2
    return run_program(program)[0]

print(main())