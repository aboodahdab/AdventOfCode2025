
invalid_ids = 0
PUZZLE_FILENAME = "day2puzzle.txt"


def check_if_invalid(string_number,):

    if len(string_number) % 2 != 0:
        return False
    length = len(string_number)
    string_number_first_part = string_number[:length//2]
    string_number_second_part = string_number[length//2:]
    if string_number_first_part == string_number_second_part:
        print("what is that bro", string_number)
        global invalid_ids
        invalid_ids += int(string_number)
        print(invalid_ids, "that is invalid")
    return invalid_ids
# need to check for repeated integers like 1010


def split_content(string):

    #  just a func to split the string bro
    splited_string_by_comma = string.split(",")
    for str_range in splited_string_by_comma:
        str_range = str_range.strip()
        str_ranges = str_range.split("-")
        first_number = int(str_ranges[0])
        last_number = int(str_ranges[1])
        print(first_number, last_number)
        for j in range(first_number, last_number+1):
            j_str = str(j)
            check_if_invalid(j_str)
    print(invalid_ids, "these are invalid ids")


with open(PUZZLE_FILENAME, "r") as file:
    content = file.read()
    split_content(content)
