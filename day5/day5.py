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


# def check_ranges_and_digits(ranges, digits):
#     global fresh_count
#     for i in ranges:
#         splited_i = i.split("-")
#         min_range = int(splited_i[0])
#         max_range = int(splited_i[1])
#         numbers_inside_range = []
#         for j in range(min_range, max_range):
#             numbers_inside_range.append(j)
#         for h in digits:
#              if int(h) in numbers_inside_range:
#                 fresh_count += 1
#     print("final result i think:".title(),fresh_count)


# def organize_content(content):
#     splited_content = content.strip().split("\n")
#     ranges = []
#     digits = []
#     for i in splited_content:
#         if i.isdigit():
#             digits.append(i)

#         elif "-" in i:
#             ranges.append(i)
#     check_ranges_and_digits(ranges, digits)
#     print("splited one", splited_content)


# with open(PUZZLE_FILENAME, "r") as file:
#     content = file.read()
#     print(organize_content(content))
# shout out to me i did not google a thing in this puzzle but i will cut this because it performance draining so much
