# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

    while True:

        user = input("Please choose a number:\nshow-table - 1\nadd - 2\nremove - 3\nupdate - 4\nquit - 0\n")
        if user == "0":
            break
        elif user == "1":
            show_table("tools_test.csv")
        elif user == "2":
            add("tools_test.csv")
        elif user == "3":
            update(table, id_)
        elif user == "4":
            get_available_tools(table)


# print the default table of records from the file
def show_table(table):
    table = data_manager.get_table_from_file("tools_test.csv")
    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    table = data_manager.get_table_from_file("tools_test.csv")


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
def get_average_durability_by_manufacturers(table):

    # your code

    pass
