
PUZZLE_FILENAME = "day4puzzle.txt"
accessible_at_count = 0
directions = [
    (-1, -1), (-1, 0), (-1, +1),
    (0, -1),          (0, +1),
    (1, -1),  (1, 0),  (1, +1)
]


def check_the_neighbors(row_index, col_index, grid):
    neighbors = 0
    at_neighbors = 0
    global accessible_at_count
    for row_offset, col_offset in directions:
        # print(row_offset, row_index, col_offset, col_index)
        neighbor_row = row_index + row_offset
        neighbor_col = col_index + col_offset
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
            # safe to access grid[neighbor_row][neighbor_col]
            symbol = grid[neighbor_row][neighbor_col]
            # print(symbol)
            neighbors += 1
            if symbol == "@":
                at_neighbors += 1

    if at_neighbors < 4:
        accessible_at_count += 1
    # print(accessible_at_count)


def organize_content(content):
    grid = [list(line.strip()) for line in content]
    print(grid)
    for row_index, row in enumerate(content):
        stripped_row = row.strip()
        for column_index, symbol in enumerate(stripped_row):
            if symbol == "@":

                check_the_neighbors(row_index, column_index, grid)
                # print(symbol, stripped_row[row_index])


with open(PUZZLE_FILENAME, "r") as f:
    content = f.readlines()
    organize_content(content)
