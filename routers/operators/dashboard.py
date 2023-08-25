




def remove_date_columns(columns: list) -> list:
    remove_strings = ["Date", "Year", "Month", "Day"]
    return list(filter(lambda s: s not in remove_strings, columns))

