import itertools
PUZZLE_FILENAME = "day6puzzle.txt"

with open(PUZZLE_FILENAME) as f:
    lines = f.readlines()

    lines = [line.replace('\n', '') for line in lines]

    max_w = max(len(l) for l in lines)
    number_lines = [l.ljust(max_w) for l in lines]

    all_results = 0

    columns = list(zip(*number_lines))  # Transpose!
    columns.reverse()
    print(columns,
          'columns')
    #  note: this is just for a triggring the if statement last time
    fake_gap = tuple(' ' for _ in range(len(number_lines)))
    columns.append(fake_gap)
    print()
    operators = lines[-1].split()
    array = []

    op = None
    for column in columns:

        if all(character == ' ' for character in column):
            print("hi and hello")
            numbers = [int(i) for i in array]

            result = 0
            if op == '+':
                result = sum(numbers)
                all_results += result

            elif op == "*":
                result = 1
                for i in numbers:
                    result *= i
                all_results += result
            print(f"Column with {op}: {numbers} = {result}", all_results)
            array = []
        arr = []
        digits = column[:-1]

        for number in digits:
            arr.append(number)

        new_arr = list(itertools.zip_longest(*arr, fillvalue=""))
        joined_arr = "".join(new_arr[0]).strip()
        if joined_arr:
            print(joined_arr)
            array.append(joined_arr)

        op = column[-1]
    print(array)

    print(operators)
    for j in array:
        print(j)
print(all_results)
