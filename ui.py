import copy


# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/


def print_table(table, title_list=""):
    """ Pretty prints a table or prints a simple string. """
    if isinstance(table, str):
        print(table)
        return

    table = copy.deepcopy(table)
    table.insert(0, title_list)

    table = [[str("| " + cell) for cell in row] for row in table]
    lenghts = [max(map(len, col)) for col in zip(*table)]
    width_format = ''.join('{{:<{}}}'.format(x) for x in lenghts)
    table = [width_format.format(*row) for row in table]

    table[:] = [x for i in table for x in [i + ' |', '-'*(2+len(table[0]))]]
    table.insert(0, "-"*(len(table[0])))

    corner = list(table[0])
    (corner[0], corner[-1]) = "/", "\\"
    table[0] = "".join(corner)

    corner = list(table[-1])
    (corner[0], corner[-1]) = "\\", "/"
    table[-1] = "".join(corner)

    row_list = list(table[1])
    for i in range(len(table[1])):
        if row_list[i] == "|":
            for k in range(1, len(table)-1):
                row_list2 = list(table[k])
                row_list2[i] = "|"
                table[k] = "".join(row_list2)

    print('\n'.join(table))

# An example output:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# see the function call in main.py


def print_menu(title='Title', list_options=['a', 'b', 'c'], exit_message="Back"):
    print("%s:" % (title))
    line = 1
    for i in list_options:
        print("(%s) %s" % (line, i))
        line += 1
    print("(%s) %s" % (0, exit_message))


# see the function call in main.py


def get_inputs(list_titles, title):
    print(title)
    record = [input(i) for i in list_titles]
    # your code
    return record


# see the function call in main.py
def print_error_message(message):
    print(message)
