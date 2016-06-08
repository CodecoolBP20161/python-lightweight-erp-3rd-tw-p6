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
    title = "\n\nSellings"
    list_options = [
        "Show table",
        "Add new record",
        "Remove record",
        "Update a record",
        "Cheapest item",
        "Looking up items sold between given dates"
    ]
    exit_message = "Return to the main menu"
    ui.print_menu(title, list_options, exit_message)

    while True:
        user_input = ui.get_inputs(["Choose a number from the menu: "], "")[0]

        if user_input == '1':
            show_table("selling/sellings.csv")
        elif user_input == '2':
            add("selling/sellings.csv")
        elif user_input == '3':
            id_to_remove = ui.get_inputs(["ID: "], "")
            remove("selling/sellings.csv", id_to_remove)
        elif user_input == '4':
            id_to_update = ui.get_inputs(["ID: "], "")
            update("selling/sellings.csv", id_to_update)
        elif user_input == '5':
            get_lowest_price_item_id("selling/sellings.csv")
        elif user_input == '6':
            title_list1 = ["month_from: ", "day_from: ", "year_from: ", "month_to: ", "day_to: ", "year_to: "]
            title_list = ui.get_inputs(title_list1, "")
            get_items_sold_between("selling/sellings.csv",
                                   title_list[0],
                                   title_list[1], title_list[2], title_list[3], title_list[4], title_list[5])
        elif user_input == '0':
            break
        else:
            ui.print_error_message("{} is not in the menu!".format(user_input))
            continue


# print the default table of records from the file
def show_table(table):
    table = data_manager.get_table_from_file("selling/sellings.csv")
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    new_id = common.generate_random("selling/sellings.csv")
    title = ""
    list_titles = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
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
        idx = common.id_number(existing_id, id_to_remove)
        table.remove(table[idx])
        table = data_manager.write_table_to_file("selling/sellings.csv", table)
    else:
        ui.print_error_message("{} is not an existing ID!".format(id_))
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    table = data_manager.get_table_from_file("selling/sellings.csv")
    existing_id = [i[0] for i in table]
    id_ = "".join(id_)
    if id_ in existing_id:
        idx = common.id_number(existing_id, id_)
        list_titles = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
        updated_record = ui.get_inputs(list_titles, title="")
        table[idx][1] = updated_record[0]
        table[idx][2] = updated_record[1]
        table[idx][3] = updated_record[2]
        table[idx][4] = updated_record[3]
        table[idx][5] = updated_record[4]
        table = data_manager.write_table_to_file("selling/sellings.csv", table)
    else:
        ui.print_error_message("{} is not an existing ID!".format(id_))

    return table


# special functions:
# ------------------
# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    table = data_manager.get_table_from_file("selling/sellings.csv")

    list_of_prices = []
    list_of_ids = []
    for row in table:
        list_of_prices.append(row[2])
    lowest_price = min(list_of_prices)

    for row in table:
        if lowest_price == row[2]:
            list_of_ids.append(row[0])

    desc_ids = ", ".join(common.sorting_method(list_of_ids))
    ui.print_table(desc_ids)

    return desc_ids


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    table = data_manager.get_table_from_file("selling/sellings.csv")
    filtered_items = []
    from_date = int(year_from) * 365 + int(month_from) * 31 + int(day_from)
    to_date = int(year_to) * 365 + int(month_to) * 31 + int(day_to)

    for row in table:
        days = int(row[5]) * 365 + int(row[3]) * 31 + int(row[4])
        if days >= from_date and days <= to_date:
            filtered_items.append([row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])])

    return(filtered_items)
