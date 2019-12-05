f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day5input.txt", "r")
program = f.readlines()[0].split(',')
program = [int(val) for val in program]
f.close()


def decipher_first_value(value):
    value = f'{value:05}'
    opcode = value[3:]
    mode_parameter_1 = value[2]
    mode_parameter_2 = value[1]

    return opcode, mode_parameter_1, mode_parameter_2


def process_program(input_val, program):
    pointer = 0
    first_value = program[pointer]
    opcode, mode_param_1, mode_param_2 = decipher_first_value(first_value)

    while opcode in ['01', '02', '03', '04']:

        if opcode == '01':
            if mode_param_1 == '0' and mode_param_2 == '0':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) + int(program[program[pointer + 2]])
            elif mode_param_1 == '1' and mode_param_2 == '0':
                program[program[pointer + 3]] = int(program[pointer + 1]) + int(program[program[pointer + 2]])
            elif mode_param_1 == '0' and mode_param_2 == '1':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) + int(program[pointer + 2])
            elif mode_param_1 == '1' and mode_param_2 == '1':
                program[program[pointer + 3]] = int(program[pointer + 1]) + int(program[pointer + 2])
            pointer += 4
            first_value = program[pointer]
            opcode, mode_param_1, mode_param_2 = decipher_first_value(first_value)

        elif opcode == '02':
            if mode_param_1 == '0' and mode_param_2 == '0':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) * int(program[program[pointer + 2]])
            elif mode_param_1 == '1' and mode_param_2 == '0':
                program[program[pointer + 3]] = int(program[pointer + 1]) * int(program[program[pointer + 2]])
            elif mode_param_1 == '0' and mode_param_2 == '1':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) * int(program[pointer + 2])
            elif mode_param_1 == '1' and mode_param_2 == '1':
                program[program[pointer + 3]] = int(program[pointer + 1]) * int(program[pointer + 2])
            pointer += 4
            first_value = program[pointer]
            opcode, mode_param_1, mode_param_2 = decipher_first_value(first_value)

        elif opcode == '03':
            program[program[pointer + 1]] = input_val
            pointer += 2
            first_value = program[pointer]
            opcode, mode_param_1, mode_param_2 = decipher_first_value(first_value)

        elif opcode == '04':
            if mode_param_1 == '0':
                print(program[program[pointer + 1]])
            elif mode_param_1 == '1':
                print(program[pointer + 1])
            pointer += 2
            first_value = program[pointer]
            opcode, mode_param_1, mode_param_2 = decipher_first_value(first_value)

        elif opcode == '99':
            return


def main():
    input_value = input("Please enter an input value: ")
    process_program(input_value, program)


main()
# Answer: 6745903



