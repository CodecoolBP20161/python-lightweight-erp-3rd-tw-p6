from copy import deepcopy

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/


def print_table(table, title_list):
    """ Pretty prints a table. """
    table = deepcopy(table)
    table.insert(0, title_list)

    # s = [[str("| " + e) for e in row] for row in table]
    s = [[(e) for e in row] for row in table]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:<{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]

    length = sum(lens)
    for i in range(len(table)):
        table.insert(2*i + 1, "-"*(length + 8*(len(title_list)-1)))
    table.insert(0, "-"*(length + 8*(len(title_list)-1)))

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
