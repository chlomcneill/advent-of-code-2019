f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day8input.txt", "r")
password_input = f.readlines()
password_input = [int(char) for char in password_input[0]]
f.close()


def decode_layers(password, pixels_wide, pixels_tall):
    layer_size = pixels_wide * pixels_tall
    password = [password[x:x+layer_size] for x in range(0, len(password), layer_size)]
    layer_with_least_zeros = []
    zero_count = layer_size

    for layer in password:
        if layer.count(0) < zero_count:
            zero_count = layer.count(0)
            layer_with_least_zeros = layer

    return layer_with_least_zeros.count(1) * layer_with_least_zeros.count(2)


def main():
    print(decode_layers(password_input, 25, 6))


# main()
# Answer: 1920
