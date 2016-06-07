# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start():
    title = "\n\nSellings\nWhat would you like to do"
    list_options = [
        "Show table",
        "Add new record",
        "Remove record",
        "Update a record",
    ]
    exit_message = "Return to the main menu"
    ui.print_menu(title, list_options, exit_message)

    while True:
        user_input = ui.get_inputs(["Press a number between 0 - 4: "], "")[0]

        if user_input == '1':
            show_table("selling/sellings.csv")
        elif user_input == '2':
            add("selling/sellings.csv")
        elif user_input == '3':
            id_to_remove = ui.get_inputs(["id: "], "")
            remove("selling/sellings.csv", id_to_remove)
        elif user_input == '4':
            update("selling/selling/sellings.csv")
        elif user_input == '0':
            break
        else:
            continue


# print the default table of records from the file
def show_table(table):
    table = data_manager.get_table_from_file("selling/sellings.csv")
    title_list = ["id", "title", "price", "month", "day", "year"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table

def add(table):
    new_id = common.generate_random("selling/sellings.csv")
    title = ""
    list_titles = ["title: ", "price: ", "month: ", "day: ", "year: "]
    record = ui.get_inputs(list_titles, title)
    record.insert(0, new_id)
    table = data_manager.get_table_from_file("selling/sellings.csv")
    table = table + [record]
    table = data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table


def remove(table, id_):
    table = data_manager.get_table_from_file("selling/sellings.csv")
    existing_id = [i[0] for i in table]
    id_to_remove = "".join(id_)
    if id_to_remove in existing_id:
        idx = existing_id.index(id_to_remove)
        table.remove(table[idx])
        table = data_manager.write_table_to_file("selling/sellings.csv", table)
    else:
        print_error_message("{} is not an existing ID!".format(id_))
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order


def get_lowest_price_item_id(table):

    # your code

    pass


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass
