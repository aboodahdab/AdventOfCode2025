# DIAL_VALUE = 50
# zero_times = 0


# def ToLeftOrRight(string, dial_value, zero_times):

#     string_splited = string.split("\n")
#     new_position = None
#     for i in string_splited:
#         print(i)
#         i_letter = i[0]
#         i_number = int(i[1:])
#         if i_letter.lower() == "r":
#             new_position = (dial_value + i_number) % 100
#             dial_value = new_position
#             print(new_position, "new_position", "R")
#             if new_position == 0:
#                 zero_times += 1
#         if i_letter.lower() == "l":
#             new_position = (dial_value - i_number) % 100
#             dial_value = new_position
#             print(new_position, "new_position", "L")
#             if new_position == 0:
#                 zero_times += 1

#         print("zero_times m3lmi", zero_times)


# with open("day1puzzle.txt", "r") as file:
#     content = file.read()
#     print(ToLeftOrRight(content, DIAL_VALUE, zero_times))

# part 2
DIAL_VALUE = 50
zero_times = 0


def ToLeftOrRight(string, dial_value, zero_times):

    string_splited = string.split("\n")
    new_position = None
    for i in string_splited:
        i_letter = i[0]
        i_number = int(i[1:])

        if i_letter.lower() == "r":
            new_position = (dial_value + i_number) % 100
            i_letter_2 = i_number//100

            for j in range(1, int(i_letter_2)):
                h = (dial_value + i_number) % 100
                if h == 0:
                    zero_times += 1
                print(h, zero_times, "h_and_zero_teims")
            # print(new_position, "new pos")
            dial_value = new_position
            # print(new_position, "new_position", "R")
            # if new_position == 0:
            #     zero_times += 1
        if i_letter.lower() == "l":
            new_position = (dial_value - i_number) % 100
            i_letter_2 = i_number/100
            print(i_letter_2)
            for j in range(1, int(i_letter_2)):
                print(j)
                h = (dial_value - i_number) % 100
                if h == 0:
                    zero_times += 1
                print(h, zero_times, "h_and_zero_teims")
            # print(new_position, "new_position", "L")
            # if new_position == 0:
            #     zero_times += 1


with open("day1puzzle.txt", "r") as file:
    content = file.read()
    print(ToLeftOrRight(content, DIAL_VALUE, zero_times))
# i_letter_2=i_letter/50 important very important
