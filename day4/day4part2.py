PUZZLE_FILENAME = "day4puzzle.txt"

directions = [
    (-1, -1), (-1, 0), (-1, +1),
    (0, -1),          (0, +1),
    (1, -1),  (1, 0),  (1, +1)
]


def check_the_neighbors(row_index, col_index, grid):
    at_neighbors = 0
    
    for row_offset, col_offset in directions:
        neighbor_row = row_index + row_offset
        neighbor_col = col_index + col_offset
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
            symbol = grid[neighbor_row][neighbor_col]
            if symbol == "@":
                at_neighbors += 1
    
    return at_neighbors


def organize_content(content):
    grid = [list(line.strip()) for line in content]
    total_removed = 0
    
    while True:
        positions_to_remove = []
        
        # Loop through the GRID (not content!)
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == "@":
                    neighbor_count = check_the_neighbors(row_index, col_index, grid)
                    if neighbor_count < 4:
                        positions_to_remove.append((row_index, col_index))
        
        # If nothing to remove, we're done!
        if len(positions_to_remove) == 0:
            break
        
        # Remove all the positions we found
        for row, col in positions_to_remove:
            grid[row][col] = "."
        
        total_removed += len(positions_to_remove)
        print(f"Removed {len(positions_to_remove)} this round")
    
    print(f"Total removed: {total_removed}")


with open(PUZZLE_FILENAME, "r") as f:
    content = f.readlines()
    organize_content(content)