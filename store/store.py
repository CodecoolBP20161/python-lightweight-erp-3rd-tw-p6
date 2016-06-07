# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common manager module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()

table = data_manager.get_table_from_file("store/games.csv")


# start this manager by a menu
def start():
    list_options = ["Show table",
                    "Add",
                    "Remove",
                    "Update",
                    "Get count by manufacturers",
                    "Get average by manufacturer"]
    ui.print_menu("Store menu", list_options, "Exit menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == '1':
        show_table(table)
    elif option == '2':
        add(table)
    elif option == '3':
        title = "Remove a record from the table by ID."
        list_titles = ["Enter ID: "]
        id_ = ui.get_inputs(list_titles, title)
        remove(table, id_)
    elif option == '4':
        title = "Update data in record by ID"
        list_titles = ["Enter ID: "]
        id_ = ui.get_inputs(list_titles, title)
        update(table, id_)
    elif option == '5':
        get_counts_by_manufacturers(table)
    elif option == '6':
        title = "Get average by a given manufacturer"
        list_titles = ["Enter manufacturer name: "]
        manufacturer = ui.get_inputs(list_titles, title)
        get_average_by_manufacturer(table, manufacturer)
    elif option == '0':
        quit()
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
def show_table(table):

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    title = "Adding a new record to the table."
    list_titles = ["Enter a title: ",
                   "Enter the name of the manufacturer: ",
                   "Price(dollar): ",
                   "In stock: "]
    added_input = ui.get_inputs(list_titles, title)
    randomgen = common.generate_random(table)
    record = [randomgen, added_input[0], added_input[1], added_input[2], added_input[3]]
    table.append(record)
    data_manager.write_table_to_file("store/games.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    for element in table:
        if element[0] == id_[0]:
            table.remove(element)
    data_manager.write_table_to_file("store/games.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    for element in table:
        if element[0] == id_[0]:
            selected_element = element
    list_options = ["Game name",
                    "manufacturer name",
                    "Price",
                    "Stock"]
    ui.print_menu("Please choose an option", list_options, "Back to store menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == '1':
        list_titles = ["Enter a new name: "]
        name_input = ui.get_inputs(list_titles, "")
        selected_element[1] = name_input[0]
    elif option == '2':
        list_titles = ["Enter a new manufacturer name: "]
        man_input = ui.get_inputs(list_titles, "")
        selected_element[2] = man_input[0]
    elif option == '3':
        list_titles = ["Enter a new price: "]
        price_input = ui.get_inputs(list_titles, "")
        selected_element[3] = man_input[0]
    elif option == '4':
        list_titles = ["Enter a new stock quantity: "]
        q_input = ui.get_inputs(list_titles, "")
        selected_element[4] = q_input[0]
    elif option == '0':
        start()
    else:
        raise KeyError("There is no such option.")
    for element in table:
        if element[0] == added_input[0]:
            element = selected_element
    data_manager.write_table_to_file("store/games.csv", table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturer_count = {}
    for element in table:
        manufacturer_count[element[2]] = 0
    for i in table:
        for j in manufacturer_count.keys():
            if i[2] == j:
                manufacturer_count[j] += 1
    return manufacturer_count


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    manufacturer_all_games_list = []
    for i in table:
        if i[2] == manufacturer[0]:
                manufacturer_all_games_list.append(int(i[4]))
    manufacturer_avg_num = sum(manufacturer_all_games_list) / len(manufacturer_all_games_list)
    return manufacturer_avg_num
