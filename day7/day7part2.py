PUZZLE_FILENAME = "day7puzzle.txt"
cache = {}


def check_for_splitters_and_hande_them(row_index, rows, col_index):
    if row_index < 0 or row_index >= len(rows) or col_index < 0 or col_index > len(rows[0]):
        return 1

    # safe to access
    val = rows[row_index][col_index]
    print(val)
    key = (row_index, col_index)
    if key in cache:
        return cache[key]  # Return the cached number of paths

    if val.lower() == "s":
        return check_for_splitters_and_hande_them(row_index+1, rows, col_index)
    if val.lower() == ".":
        return check_for_splitters_and_hande_them(row_index+1, rows, col_index)

    if val.lower() == "^":
        left = check_for_splitters_and_hande_them(
            row_index+1, rows, col_index-1)
        right = check_for_splitters_and_hande_them(
            row_index+1, rows, col_index+1)
        result=right+left
        cache[key]=result
        print(result)
        return result


with open(PUZZLE_FILENAME, "r") as file:
    content = [i.strip() for i in file.readlines()]
    s_index = None

    for row_index, i in enumerate(content):
        for col_index, j in enumerate(i):
            if j.lower() == "s":
                s_index = (row_index, col_index)
                print("s index", s_index)
                print(check_for_splitters_and_hande_them(
                    row_index, content, col_index))
