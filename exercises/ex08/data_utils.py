"""Dictionary related utility functions."""
__author__ = "730573354"
from csv import DictReader


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a "table"."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    # read each row of CSV line by line
    for row in csv_reader:
        result.append(row)
    file_handle.close()  # close file when done to free its resources
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all the values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Takes a table and returns the first n # of rows as a new table."""
    result: dict[str, list[str]] = {}
    for key in table:
        counter: int = 0
        str_list: list[str] = []
        while counter < n:
            str_list.append(table[key][counter])
            counter += 1
        result[key] = str_list
    return result


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Selects a specifc column and returns all the values from the table with that key."""
    result: dict[str, list[str]] = {}
    for val in col_names:
        result[val] = table[val]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column based tables into a single column based table."""
    result: dict[str, list[str]] = {}
    for col in table_1:
        for val in table_1[col]:
            result[col] = table_1[col]
    
    for col in table_2:
        for val in table_2[col]:
            if col in result:  # If value already exists in result it adds the value to the current value
                result[col] += table_2[col]
            else:  # new values are added seperately 
                result[col] = table_2[col]
    return result

    