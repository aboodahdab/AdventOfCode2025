


PUZZLE_FILENAME = "day3puzzle.txt"

length_of_joltage = 2
result = 0


def organize_content(content):

    global result
    for i in content:
        the_biggest_num = 0
        joltage = ""
        stripped_bank = i.strip()
        print(stripped_bank)
        for j in stripped_bank:
           
            print("joltage 2",joltage)
            # print(j,"j thing",the_biggest_num,int(j)>the_biggest_num)
            if len(str(joltage)) == length_of_joltage:
                result += int(joltage)
                joltage = ""

            if int(j) > the_biggest_num:
                the_biggest_num = int(j)
                print(joltage)
                joltage+=f"{j}"
                
                print("new_joltage")
                print(joltage,"joltage")

    print(result,)


with open(PUZZLE_FILENAME, "r") as f:
    content = f.readlines()

    organize_content(content)
