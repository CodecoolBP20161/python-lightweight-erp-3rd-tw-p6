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
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start():
    """ Creates a submenu for accounting.py """
    while True:
        ui.print_menu(title='Accounting manager',
                      list_options=['Show table', 'Add new item', 'Remove item',
                                    'Update item', 'Highest profit (2015/16) ***', 'Average profit per year ***'],
                      exit_message="Back to MainMenu")
        user_input = ui.get_inputs(list_titles=["Please, choose a number: "], title="")[0]
        if user_input == "0":
            break
        elif user_input == "1":
            show_table("accounting/items.csv")
        elif user_input == "2":
            add("accounting/items.csv")
        elif user_input == "3":
            list_titles = ["Id_: "]
            record = ui.get_inputs(list_titles, title="")
            remove("accounting/items.csv", record)
        elif user_input == "4":
            list_titles = ["Id_: "]
            record = ui.get_inputs(list_titles, title="")
            update("accounting/items.csv", record)
        elif user_input == "5":
            which_year_max("accounting/items.csv")
        elif user_input == "6":
            list_titles = ["Year: "]
            record = ui.get_inputs(list_titles, title="")
            avg_amount("accounting/items.csv", year)
        else:
            ui.print_error_message("Invalid input!")


# print the default table of records from the file
def show_table(table):
    """ Shows the accounting/items.csv database """
    table = data_manager.get_table_from_file("accounting/items.csv")
    title_list = ["id", "month", "day", "year", "type", "amount"]
    return ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    """ Adds a new row to the database """
    id_input = common.generate_random("accounting/items.csv")
    list_titles = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
    record = ui.get_inputs(list_titles, title="")
    record.insert(0, id_input)
    table = data_manager.get_table_from_file("accounting/items.csv")
    table = table + [record]
    table = data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    """ Removes a certain row from the database identified by id_ """
    table = data_manager.get_table_from_file("accounting/items.csv")
    existing_id = [i[0] for i in table]
    id_ = ''.join(id_)
    if id_ in existing_id:
        for i in table:
            if i[0] == id_:
                table.remove(i)
                table = data_manager.write_table_to_file("accounting/items.csv", table)
        else:
            pass
    else:
        ui.print_error_message("Invalid input!")
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):
    """ Removes a certain row from the database identified by id_ """
    table = data_manager.get_table_from_file("accounting/items.csv")
    existing_id = [i[0] for i in table]
    id_ = ''.join(id_)
    if id_ in existing_id:
        for i in table:
            if i[0] == id_:
                list_titles = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
                updated_inputs = ui.get_inputs(list_titles, title="")
                i[1] = updated_inputs[0]
                i[2] = updated_inputs[1]
                i[3] = updated_inputs[2]
                i[4] = updated_inputs[3]
                i[5] = updated_inputs[4]
                table = data_manager.write_table_to_file("accounting/items.csv", table)
    else:
        ui.print_error_message("Invalid input!")
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):
    """ Highest profit of 2 years: 2015 or 2016 """
    in_2016 = []
    out_2016 = []
    in_2015 = []
    out_2015 = []
    table = data_manager.get_table_from_file("accounting/items.csv")
    for i in table:
        if i[3] == '2016' and i[4] == "in":
            in_2016.append(float(i[5]))
        elif i[3] == '2016' and i[4] == "out":
            out_2016.append(float(i[5]))
        elif i[3] == '2015' and i[4] == "in":
            in_2015.append(float(i[5]))
        elif i[3] == '2015' and i[4] == "out":
            out_2015.append(float(i[5]))
    profit_2016 = common.summary(in_2016) - common.summary(out_2016)
    profit_2015 = common.summary(in_2015) - common.summary(out_2015)
    if profit_2015 > profit_2016:
        print("The highest profit was reached in 2015.")
        return 2015
    else:
        print("The highest profit was reached in 2016.")
        return 2016


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
