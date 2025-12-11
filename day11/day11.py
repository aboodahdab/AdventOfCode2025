PUZZLE_FILENAME = "day11puzzle.txt"


def organize_content(content):
    splited_content = content.split("\n")
    complete_paths = 0
    data_dic = {}

    for i in splited_content:
        splited_i = i.split(":")
        key = splited_i[0]
        value = splited_i[1].strip().split(" ")
        data_dic[f"{key}"] = value

    def recursive_func(device_name):
        if device_name == "out":
            return 1
        choices = data_dic[device_name]
        total = 0
        for choice in choices:
            total += recursive_func(choice)
            print(choice)
        return total
    result = recursive_func("you")
    print(result)


with open(PUZZLE_FILENAME, "r") as file:
    content = file.read()
    organize_content(content)
