# You are implementing the computation & storage component of a spreadsheet
# (think Excel or Google Sheets). You have a UI developer who will be
# responsible for, well, User Interaction (rendering, handling user input,
# etc).

# We will be providing the UI developer two functions:

# 1. set_cell - to be used like `set_cell("C1", "45")` 
#             or, for formulas, `set_cell("C1", "=A1+B1")`
# 2. get_value - ie, `get_value("C1")`, and return an integer value.
 
# We will not be implementing all of a spreadsheet's features, but we need the
# ability for a cell to refer to other cells in formulas, and to sum values
# from other cells. 

# When in doubt, bias towards simplicity.

# ===================
# Sample spreadsheet:
# ===================
#     A   B   C
# 1   3   5
# 2           =A1+B1
# ===================

import pandas as pd
data = {}

formula = {}

def get_sum(value):
    values = value.split("+")
    if len(values):
        values[0] = values[0].split("=")[1]
    sum = 0
    for v in values:
        sum += get_value(v)
    return sum

def update_cells(column_data):
    for k,v in formula.items():
        if column_data in v:
            data[k] = get_sum(v)
            update_cells(k)

def resolve(column_data, value):
    if "int" in str(type(value)):
        data[column_data] = value
    else:
        formula[column_data] = value
        data[column_data] = get_sum(value)

def set_cell(column_data, value):
    resolve(column_data, value)
    update_cells(column_data)

def get_value(column):
    try:
        return data[column]
    except KeyError:
        print("Key Value not found")
        return 0

#postive
set_cell("B1", 45)
set_cell("B2", 46)
set_cell("B4", 46)
set_cell("C1", "=B1+B4")

#negative handling KeyError
set_cell("C1", "=B1+B3")
get_value("A1")

set_cell("C3", "=C1+B1")
print(data)
#updation
set_cell("B1", 50)

#multiple values
set_cell("C2", "=B1+B4+B2")

set_cell("B3", 10)
print(data)
print(formula)

#handling symbols other than +
