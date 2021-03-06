import random
# implement commonly used functions here


def summary(my_list):
    solution = 0
    for i in my_list:
        solution += int(i)
    return solution


def id_number(my_list, item):
    index = -1
    for i in my_list:
        index += 1
        if i == item:
            return index


# generate and return a unique and random
# (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter) string
# it must be unique in the list
def generate_random(table):
    lower = "abcdefghijklmnopqrstuvwxyz"
    chars = "[!@#$%^&*()?]"
    existing_id = [i[0] for i in table]
    num = [random.randint(0, 9) for i in range(2)]
    letter = [lower[random.randint(0, len(lower) - 1)] for i in range(2)]
    letter_upper = [lower[random.randint(
        0, len(lower) - 1)].upper() for i in range(2)]
    special = [chars[random.randint(0, len(chars) - 1)] for i in range(2)]
    a = num + letter + letter_upper + special
    password = "".join(str(i) for i in a)
    if password not in existing_id:
        return password
    else:
        return generate_random(table)



def sorting_method(list1):
    """ Sorts list1 """
    new_list1 = []

    for i in range(len(list1)):
        order = id_number(list1, max(list1))
        new_list1.append(list1[order])
        list1.remove(list1[order])

    return new_list1
