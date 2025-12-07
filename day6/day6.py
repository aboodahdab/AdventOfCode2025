PUZZLE_FILENAME = "day6puzzle.txt"
with open(PUZZLE_FILENAME) as f:
    lines = f.read().strip().split('\n')

    number_lines = [line.split() for line in lines[:-1]]
    all_results = 0
    columns = list(zip(*number_lines))  # Transpose!
    print(columns)
    operators = lines[-1].split()
    print(operators)
    for col, op in zip(columns, operators):
        print(col, op)
        numbers = [int(x) for x in col]
        if op == '+':
            result = sum(numbers)
            all_results+=result

        elif op == "*":
            result = 1
            for i in numbers:
                result *= i
            all_results+=result
        print(f"Column with {op}: {numbers} = {result}", all_results)
