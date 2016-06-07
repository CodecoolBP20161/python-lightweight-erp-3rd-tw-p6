# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
ui = SourceFileLoader("module.name", current_file_path + "/../ui.py").load_module()
data_manager = SourceFileLoader("module.name", current_file_path + "/../data_manager.py").load_module()


def start_module():
    table = data_manager.get_table_from_file("hr/persons.csv")
    title = "HR Abteilung"
    list_options = ["Show table", "Add", "Remove", "Update", "Get oldest person", "Get people closest to average age"]
    ui.print_menu(title, list_options, "Exit")
    while True:
        user_input = input("\n Please specify a command. \n")

        if user_input == "1":
            show_table(table)

        elif user_input == "2":
            table = add(table)

        elif user_input == "3":
            removeable_id = input("Id of the person to be removed:")
            table = remove(table, removeable_id)

        elif user_input == "4":
            updateable_id = input("Id of the person to be updated:")
            table = update(table, updateable_id)

        elif user_input == "5":
            print(get_oldest_person(table))

        elif user_input == "6":
            print(get_persons_closest_to_average(table))

        elif user_input == "0":
            return

        else:
            print("You did not enter a valid command. Try again.")


def show_table(table):
    """ Prints the default table of records from the file. """
    print(table)
    for row in table:
        printable = "{0} {1} {2}".format(row[0], row[1], row[2])
        print(printable)


def add(table):
    """ Adds a new record to the table based on user input. """
    table.append([])
    table[-1].append("random_generated_id_from_balazs")
    user_input = input("Give in the name: ")
    table[-1].append(user_input)
    user_input = input("Give in the year: ")
    table[-1].append(user_input)
    return table


def remove(table, id_):
    """ Removes a record from the table specified by the user. """
    id_counter = 0
    found = 0
    for row in table:
        if row[0] == id_:
            del table[id_counter]
            print("Id {0} deleted from the table (name: {1} , year: {2})".format(row[0], row[1], row[2]))
            found = 1
        id_counter += 1
    if found == 0:
        print("The ID {0} does not exist.".format(id_))
    return table


def update(table, id_):
    """ Updates a table record based on user input. """
    id_counter = 0
    for row in table:
        if row[0] == id_:
            name = input("Give in the updated name:")
            year = input("Give in the updated year:")
            table[id_counter][1] = name
            table[id_counter][2] = year
            print("Id {0} updated (name: {1} , year: {2})".format(row[0], row[1], row[2]))
        id_counter += 1

    return table


def get_oldest_person(table):
    """ Returns the oldest person from the table. """
    minimum = 9999
    name = []
    for row in table:
        if int(row[2]) < int(minimum):
            name = []
            minimum = row[2]
            name.append(row[1])
        elif int(row[2]) == int(minimum):
            name.append(row[1])

    return name


def get_persons_closest_to_average(table):
    """ Returns person from the table closest to the average age. """
    year_sum = 0.0
    counter = 0
    years = []
    names = []
    for row in table:
        year_sum += float(row[2])
        years.append(float(row[2]))
        counter += 1
    average_year = year_sum / counter

    year = min(years, key=lambda x: abs(x-average_year))

    for row in table:
        if int(row[2]) == int(year):
            names.append(row[1])
    return names
