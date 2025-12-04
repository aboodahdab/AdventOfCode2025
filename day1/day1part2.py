DIAL_VALUE = 50

def count_zeros_crossed(start, distance, direction):
    """Count how many times we pass through 0 during a rotation"""
    count = 0
    
    if direction == 'r':
        # Going right
        for step in range(1, distance + 1):
            if (start + step) % 100 == 0:
                count += 1
    else:  # direction == 'l'
        # Going left
        for step in range(1, distance + 1):
            if (start - step) % 100 == 0:
                count += 1
    
    return count


def ToLeftOrRight(string, dial_value):
    string_splited = string.split("\n")
    zero_times = 0
    
    for i in string_splited:
        if not i.strip():
            continue
            
        print(i)
        i_letter = i[0].lower()
        i_number = int(i[1:])
        
        # Count how many times we pass through 0 during this rotation
        zeros_in_rotation = count_zeros_crossed(dial_value, i_number, i_letter)
        zero_times += zeros_in_rotation
        
        # Update position
        if i_letter == "r":
            dial_value = (dial_value + i_number) % 100
        else:
            dial_value = (dial_value - i_number) % 100
            
        print(f"new position: {dial_value}, zeros crossed: {zeros_in_rotation}, total: {zero_times}")
    
    print("Final answer:", zero_times)


with open("day1puzzle.txt", "r") as file:
    content = file.read()
    ToLeftOrRight(content, DIAL_VALUE)