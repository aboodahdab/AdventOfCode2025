PUZZLE_FILENAME = "day5puzzle.txt"


def check_ranges_and_digits(ranges, digits):
    digit_set = set(int(d) for d in digits)
    fresh_count = 0

    # Check each digit once - is it in ANY range?
    for num in digit_set:
        for i in ranges:
            min_range, max_range = map(int, i.split("-"))
            if min_range <= num <= max_range:  # inclusive on both ends
                fresh_count += 1
                break  # Stop checking ranges once we find it's fresh

    print("Final Result I Think:", fresh_count)
    return fresh_count


def organize_content(content):
    splited_content = content.strip().split("\n")
    ranges = []
    digits = []
    for i in splited_content:
        if i.isdigit():
            digits.append(i)
        elif "-" in i:
            ranges.append(i)

    return check_ranges_and_digits(ranges, digits)


with open(PUZZLE_FILENAME, "r") as file:
    content = file.read()
    print(organize_content(content))

    PUZZLE_FILENAME = "day5puzzle.txt"
fresh_count = 0
