from itertools import permutations

f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day7input.txt", "r")
program_input = f.readlines()[0].split(',')
program_input = [int(val) for val in program_input]
f.close()


def decipher_value(value):
    value = f'{value:05}'
    opcode = value[3:]
    parameter_mode_1 = value[2]
    parameter_mode_2 = value[1]
    parameter_mode_3 = value[0]

    return opcode, parameter_mode_1, parameter_mode_2, parameter_mode_3


def process_program(input1, input2, program):
    output = 0
    pointer = 0
    input_selector = 1
    value = program[pointer]
    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

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
            value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

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
            value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

        elif opcode == '03':
            if input_selector == 1:
                program[program[pointer + 1]] = input1
                pointer += 2
                value = program[pointer]
                opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                input_selector = 2
            elif input_selector == 2:
                program[program[pointer + 1]] = input2
                pointer += 2
                value = program[pointer]
                opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                input_selector = 3

        elif opcode == '04':
            if param_mode_1 == '0':
                output = program[program[pointer + 1]]
            elif param_mode_1 == '1':
                output = program[pointer + 1]
            pointer += 2
            value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

        elif opcode == '05':
            if param_mode_1 == '0' and param_mode_2 == '0':
                if program[program[pointer+1]] != 0:
                    pointer = program[program[pointer+2]]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
            elif param_mode_1 == '1' and param_mode_2 == '0':
                if program[pointer+1] != 0:
                    pointer = program[program[pointer+2]]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
            elif param_mode_1 == '0' and param_mode_2 == '1':
                if program[program[pointer+1]] != 0:
                    pointer = program[pointer+2]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
            elif param_mode_1 == '1' and param_mode_2 == '1':
                if program[pointer+1] != 0:
                    pointer = program[pointer+2]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

        elif opcode == '06':
            if param_mode_1 == '0' and param_mode_2 == '0':
                if program[program[pointer+1]] == 0:
                    pointer = program[program[pointer+2]]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
            elif param_mode_1 == '1' and param_mode_2 == '0':
                if program[pointer+1] == 0:
                    pointer = program[program[pointer+2]]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
            elif param_mode_1 == '0' and param_mode_2 == '1':
                if program[program[pointer+1]] == 0:
                    pointer = program[pointer+2]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
            elif param_mode_1 == '1' and param_mode_2 == '1':
                if program[pointer+1] == 0:
                    pointer = program[pointer+2]
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)
                else:
                    pointer += 3
                    value = program[pointer]
                    opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

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
            value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

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
            value = program[pointer]
            opcode, param_mode_1, param_mode_2, param_mode_3 = decipher_value(value)

    return program, output


def apply_phase_setting(input, program, combination):
    # Combination format = [n,n,n,n,n]
    phase_setting_1, phase_setting_2, phase_setting_3, phase_setting_4, phase_setting_5 = combination
    program_A, output_A = process_program(phase_setting_1, input, program)
    program_B, output_B = process_program(phase_setting_2, output_A, program_A)
    program_C, output_C = process_program(phase_setting_3, output_B, program_B)
    program_D, output_D = process_program(phase_setting_4, output_C, program_C)
    program_E, output_E = process_program(phase_setting_5, output_D, program_D)
    return output_E


def find_best_amplifier_combination(input, program):
    highest_output = 0
    possible_phase_settings = list(permutations([0, 1, 2, 3, 4], 5))
    for phase_setting in possible_phase_settings:
        output = apply_phase_setting(input, program, phase_setting)
        if output > highest_output:
            highest_output = output
    return highest_output


def main():
    input_value = input("Please enter an input value: ")
    print(find_best_amplifier_combination(input_value, program_input))


# main()
# Answer: 338603





