PUZZLE_FILENAME = "day3puzzle.txt"

length_of_joltage = 2
result = 0


def organize_content(content):

    global result
    for i in content:

        stripped_bank = i.strip()
        print(stripped_bank)
        biggest_num = 0
        for index, num in enumerate(stripped_bank):
            for h in range(index+1, len(stripped_bank)):
                other_num = stripped_bank[h]
                calc_joltage = 10 * int(num)+int(other_num)
                if calc_joltage > biggest_num:
                    biggest_num = calc_joltage
            result += biggest_num

    print(result)


with open(PUZZLE_FILENAME, "r") as f:
    content = f.readlines()

    organize_content(content)
