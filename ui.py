

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
def print_table(table, title_list):

    # your code

    pass


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
