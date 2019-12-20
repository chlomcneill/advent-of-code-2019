f = open("/Users/mcneillc/Dev/my-stuff/advent-of-code-2019/inputs/day8input.txt", "r")
password_input = f.readlines()
password_input = [int(char) for char in password_input[0]]
f.close()


def decode_pixel(pixel_layers):
    for layer in pixel_layers:
        if layer == 0:
            return 0
        elif layer == 1:
            return 1


def decode_password(password, pixels_wide, pixels_tall):
    layer_size = pixels_wide * pixels_tall
    password = [password[x:x+layer_size] for x in range(0, len(password), layer_size)]
    new_password = []

    for i in range(layer_size):
        pixel_layers = []
        for layer in password:
            pixel_layers.append(layer[i])
        pixel = decode_pixel(pixel_layers)
        new_password.append(pixel)

    pointer = 0
    for i in range(pixels_tall):
        print(new_password[pointer:pointer+pixels_wide])
        pointer += pixels_wide


def main():
    decode_password(password_input, 25, 6)


main()
# Answer: PCULA
