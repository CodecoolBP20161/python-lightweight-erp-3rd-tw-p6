# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()


# start this manager by a menu
def start():
    """ Creates a submenu for accounting.py """
    ui.print_menu(title='Accounting manager', list_options=['Show table', 'Add new item', 'Remove item', 'Update item'],
                  exit_message="Back to MainMenu")
    while True:
        user_input = input()
        if user_input == "0":
            break
        elif user_input == "1":
            show_table("items.csv")
        elif user_input == "2":
            add("items.csv")
        elif user_input == "3":
            remove("items.csv", id_)
        elif user_input == "4":
            update("items.csv", id_)
        else:
            ui.print_error_message("Not an option!")


# print the default table of records from the file
def show_table(table):
    """ Shows the items.csv database """
    table = data_manager.get_table_from_file("items.csv")
    title_list = ["id", "month", "day", "year", "type", "amount"]
    for rows in table:
        print(rows)
    # ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
