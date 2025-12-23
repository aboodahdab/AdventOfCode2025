PUZZLE_FILENAME = "day7puzzle.txt"


def check_for_splitters_and_hande_them(s_index, grid):
    split_hit_count = 0

    spliters_index_set = {s_index}

    for row_index in range(1, len(grid)):
        new_splits_index_set = set()
        for s_row_index, s_col_index in spliters_index_set:
            if grid[row_index][s_col_index] == ".":
                new_splits_index_set.add((row_index, s_col_index))
            elif grid[row_index][s_col_index] == "^":
                new_splits_index_set.add(
                    (row_index, s_col_index - 1))
                new_splits_index_set.add((row_index, s_col_index + 1))
                print("ahh a stupid splitter ", row_index, col_index,)
                split_hit_count += 1
        spliters_index_set = new_splits_index_set


    return split_hit_count


with open(PUZZLE_FILENAME, "r") as file:
    content = [i.strip() for i in file.readlines()]
    s_index = None

    for row_index, i in enumerate(content):
        for col_index, j in enumerate(i):
            if j.lower() == "s":
                s_index = (row_index, col_index)
                print("s index", s_index)
                print(check_for_splitters_and_hande_them(s_index, content))
