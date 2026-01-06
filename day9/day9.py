PUZZLE_FILENAME = "day9puzzle.txt"


def organize_content(content):
    max_area = 0
    for index, i in enumerate(content):
        splitted_i = i.split(",")
        col = int(splitted_i[0])

        row = int(splitted_i[1])

        for j in content[index + 1:]:
            splitted_j = j.split(",")
            j_col = int(splitted_j[0])
            j_row = int(splitted_j[1])

            width = max(j_col, col)-min(j_col, col)+1
            height = max(j_row, row)-min(j_row, row)+1

            area = width*height
            if area > max_area:
                max_area = area
    return max_area


with open(PUZZLE_FILENAME, "r") as file:
    content = [i.strip() for i in file.readlines()]
    print(organize_content(content), "maximum area")
