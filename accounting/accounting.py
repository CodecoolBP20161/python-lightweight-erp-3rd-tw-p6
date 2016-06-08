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
                      list_options=['Show table', 'Add new item', 'Remove item', 'Update item',
                                    'Highest profit in year ***', 'Average profit ***'],
                      exit_message="Back to MainMenu")
        user_input = ui.get_inputs(list_titles=["Please, choose a number: "], title="")[0]
        try:
            if user_input == "0":
                break
            elif user_input == "1":
                show_table("accounting/items.csv")
            elif user_input == "2":
                add("accounting/items.csv")
            elif user_input == "3":
                list_titles = ["Id_: "]
                try:
                    record = ui.get_inputs(list_titles, title="")
                    remove("accounting/items.csv", record)
                except:
                    ui.print_error_message("Invalid input!")
            elif user_input == "4":
                list_titles = ["Id_: "]
                try:
                    record = ui.get_inputs(list_titles, title="")
                    update("accounting/items.csv", record)
                except:
                    ui.print_error_message("Invalid input!")
            elif user_input == "5":
                result = which_year_max("accounting/items.csv")
                ui.print_table(str(result) + " has the highest profit so far.")
            elif user_input == "6":
                list_titles = ["Year: "]
                try:
                    record = ''.join(ui.get_inputs(list_titles, title=""))
                    result = avg_amount("accounting/items.csv", record)
                    ui.print_table(str(result))
                except:
                    ui.print_error_message("Invalid input!")
        except ValueError:
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
    id_ = ''.join(id_)
    for i in table:
        if i[0] == id_:
            table.remove(i)
            table = data_manager.write_table_to_file("accounting/items.csv", table)
        else:
            pass
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):
    """ Removes a certain row from the database identified by id_ """
    table = data_manager.get_table_from_file("accounting/items.csv")
    id_ = ''.join(id_)
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
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    """ Year which has the highest profit """
    table = data_manager.get_table_from_file("accounting/items.csv")
    profits_per_year = {}
    for i in table:
        if i[4] == 'in':
            if i[3] not in profits_per_year.keys():
                profits_per_year.update({i[3]: float(i[5])})
            else:
                profits_per_year[i[3]] += float(i[5])
        elif i[4] == 'out':
            if i[3] not in profits_per_year.keys():
                profits_per_year.update({i[3]: (float(i[5]) * -1)})
            else:
                profits_per_year[i[3]] -= float(i[5])
    max_profit = max(profits_per_year.values())
    for key, val in profits_per_year.items():
        if val == max_profit:
            return int(key)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    """ Average profit in a certain year """
    table = data_manager.get_table_from_file("accounting/items.csv")
    year = str(year)
    profit_in_year = {}
    list_of_years = [i[3] for i in table]
    list_of_spec_year = [i[3] for i in table if i[3] == str(year)]
    for i in table:
        if i[3] == year:
            if i[4] == 'in':
                if i[3] not in profit_in_year.keys():
                    profit_in_year.update({i[3]: float(i[5])})
                else:
                    profit_in_year[i[3]] += float(i[5])
            elif i[4] == 'out':
                if i[3] not in profit_in_year.keys():
                    profit_in_year.update({i[3]: (float(i[5]) * -1)})
                else:
                    profit_in_year[i[3]] -= float(i[5])
    average_profit_in_year = profit_in_year[str(year)] / len(list_of_spec_year)
    return average_profit_in_year
