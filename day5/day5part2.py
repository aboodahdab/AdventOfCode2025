PUZZLE_FILENAME = "day5puzzle.txt"


def check_ranges_and_generate_digits(ranges):
    # Step 1: Parse all ranges into a list of (start, end) tuples
    parsed_ranges = []
    for i in ranges:
        splited_i = i.split("-")
        min_range = int(splited_i[0])
        max_range = int(splited_i[1])
        parsed_ranges.append((min_range, max_range))
    
    # Step 2: Sort ranges by their start value
    # This groups overlapping ranges together
    parsed_ranges.sort()
    
    # Step 3: Merge overlapping ranges
    merged = []
    for start, end in parsed_ranges:
        # Check if this range overlaps with the last merged range
        # If merged is empty, or if current start > last end + 1, they don't overlap
        if not merged or start > merged[-1][1] + 1:
            # No overlap - add as a new separate range
            merged.append([start, end])
        else:
            # They overlap - extend the last merged range's end
            # Take the maximum of the two end values
            merged[-1][1] = max(merged[-1][1], end)
    
    # Step 4: Count total numbers across all merged ranges
    total = 0
    for start, end in merged:
        # Formula: numbers from start to end = (end - start + 1)
        total += (end - start + 1)
    
    print(total, "fresh")
    return total


def organize_content(content):
    splited_content = content.strip().split("\n")
    ranges = []
    
    for i in splited_content:
        if "-" in i:
            ranges.append(i)
    
    return check_ranges_and_generate_digits(ranges)


with open(PUZZLE_FILENAME, "r") as file:
    content = file.read()
    print(organize_content(content))