f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day5input.txt", "r")
program = f.readlines()[0].split(',')
program = [int(val) for val in program]
f.close()


def decipher_first_value(value):
    value = f'{value:05}'
    opcode = value[3:]
    parameter_mode_1 = value[2]
    parameter_mode_2 = value[1]
    parameter_mode_3 = value[0]

    return opcode, parameter_mode_1, parameter_mode_2, parameter_mode_3


def process_program(input_val, program):
    pointer = 0
    first_value = program[pointer]
    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

    while opcode in ['01', '02', '03', '04', '05', '06', '07', '08']:

        if opcode == '01':
            if param_mode_1 == '0' and param_mode_2 == '0':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) + int(program[program[pointer + 2]])
            elif param_mode_1 == '1' and param_mode_2 == '0':
                program[program[pointer + 3]] = int(program[pointer + 1]) + int(program[program[pointer + 2]])
            elif param_mode_1 == '0' and param_mode_2 == '1':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) + int(program[pointer + 2])
            elif param_mode_1 == '1' and param_mode_2 == '1':
                program[program[pointer + 3]] = int(program[pointer + 1]) + int(program[pointer + 2])
            pointer += 4
            first_value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

        elif opcode == '02':
            if param_mode_1 == '0' and param_mode_2 == '0':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) * int(program[program[pointer + 2]])
            elif param_mode_1 == '1' and param_mode_2 == '0':
                program[program[pointer + 3]] = int(program[pointer + 1]) * int(program[program[pointer + 2]])
            elif param_mode_1 == '0' and param_mode_2 == '1':
                program[program[pointer + 3]] = int(program[program[pointer + 1]]) * int(program[pointer + 2])
            elif param_mode_1 == '1' and param_mode_2 == '1':
                program[program[pointer + 3]] = int(program[pointer + 1]) * int(program[pointer + 2])
            pointer += 4
            first_value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

        elif opcode == '03':
            program[program[pointer + 1]] = input_val
            pointer += 2
            first_value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

        elif opcode == '04':
            if param_mode_1 == '0':
                print(program[program[pointer + 1]])
            elif param_mode_1 == '1':
                print(program[pointer + 1])
            pointer += 2
            first_value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

        elif opcode == '05':
            if param_mode_1 == '0' and param_mode_2 == '0':
                if program[program[pointer+1]] != 0:
                    pointer = program[program[pointer+2]]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
            elif param_mode_1 == '1' and param_mode_2 == '0':
                if program[pointer+1] != 0:
                    pointer = program[program[pointer+2]]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
            elif param_mode_1 == '0' and param_mode_2 == '1':
                if program[program[pointer+1]] != 0:
                    pointer = program[pointer+2]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
            elif param_mode_1 == '1' and param_mode_2 == '1':
                if program[pointer+1] != 0:
                    pointer = program[pointer+2]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

        elif opcode == '06':
            if param_mode_1 == '0' and param_mode_2 == '0':
                if program[program[pointer+1]] == 0:
                    pointer = program[program[pointer+2]]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
            elif param_mode_1 == '1' and param_mode_2 == '0':
                if program[pointer+1] == 0:
                    pointer = program[program[pointer+2]]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
            elif param_mode_1 == '0' and param_mode_2 == '1':
                if program[program[pointer+1]] == 0:
                    pointer = program[pointer+2]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
            elif param_mode_1 == '1' and param_mode_2 == '1':
                if program[pointer+1] == 0:
                    pointer = program[pointer+2]
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)
                else:
                    pointer += 3
                    first_value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

        elif opcode == '07':
            if param_mode_1 == '0' and param_mode_2 == '0':
                if program[program[pointer+1]] < program[program[pointer+2]]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            elif param_mode_1 == '1' and param_mode_2 == '0':
                if program[pointer+1] < program[program[pointer+2]]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            elif param_mode_1 == '0' and param_mode_2 == '1':
                if program[program[pointer+1]] < program[pointer+2]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            elif param_mode_1 == '1' and param_mode_2 == '1':
                if program[pointer+1] < program[pointer+2]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            pointer += 4
            first_value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)

        elif opcode == '08':
            if param_mode_1 == '0' and param_mode_2 == '0':
                if program[program[pointer+1]] == program[program[pointer+2]]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            elif param_mode_1 == '1' and param_mode_2 == '0':
                if program[pointer+1] == program[program[pointer+2]]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            elif param_mode_1 == '0' and param_mode_2 == '1':
                if program[program[pointer+1]] == program[pointer+2]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            elif param_mode_1 == '1' and param_mode_2 == '1':
                if program[pointer+1] == program[pointer+2]:
                    program[program[pointer+3]] = 1
                else:
                    program[program[pointer+3]] = 0
            pointer += 4
            first_value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_first_value(first_value)


def main():
    input_value = input("Please enter an input value: ")
    process_program(input_value, program)


# main()
# Answer: 9168267





