
invalid_ids = 0
PUZZLE_FILENAME = "day2puzzle.txt"


def check_if_invalid(string_number,):
    global invalid_ids
    for length in range(1, len(string_number)):
        if len(string_number) % length == 0:           # substring must divide full length
            part = string_number[:length]              # takes the substring
            if part * (len(string_number)//length) == string_number:
                print("invalid:", part)
                invalid_ids += int(string_number)
                break



def split_content(string):


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
