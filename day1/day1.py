DIAL_VALUE = 50
zero_times = 0


def ToLeftOrRight(string, dial_value,zero_times):

    string_splited = string.split("\n")
    new_position = None
    for i in string_splited:
        print(i)
        i_letter = i[0]
        i_number = int(i[1:])
        if i_letter.lower() == "r":
            new_position = (dial_value + i_number) % 100
            dial_value = new_position
            print(new_position, "new_position")
            if new_position == 0:
                zero_times += 1
        if i_letter.lower() == "l":
            new_position = (dial_value - i_number) % 100
            dial_value = new_position
            print(new_position, "new_position")
            if new_position == 0:
                zero_times += 1

        print("zero_times m3lmi",zero_times)


with open("day1puzzle.txt", "r") as file:
    content = file.read()
    print(ToLeftOrRight(content, DIAL_VALUE, zero_times))
