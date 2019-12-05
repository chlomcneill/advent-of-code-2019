def check_length(password):
    password = str(password)
    if len(password) == 6:
        return True
    else:
        return False


def check_double_digits(password):
    password = str(password)
    pointer = 0
    while pointer < 5:
        if password[pointer] == password[pointer+1]:
            return True
        pointer += 1
    return False


def check_increasing(password):
    password = str(password)
    pointer = 0
    while pointer < 5:
        if password[pointer] > password[pointer+1]:
            return False
        pointer += 1
    return True


def check_password(password):
    if check_length(password) and check_double_digits(password) and check_increasing(password):
        return True
    else:
        return False


def find_password_options(range_start, range_stop):
    possible_passwords = []
    for i in range(range_start, range_stop+1):
        if check_password(i):
            possible_passwords.append(i)
    return len(possible_passwords)


def main():
    return find_password_options(273025, 767253)


# print(main())
# Answer: 910

