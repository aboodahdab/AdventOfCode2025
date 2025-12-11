def solve_machine_brute(target, buttons):

    n_buttons = len(buttons)
    n_lights = len(target)
    min_presses = float('inf')

    # Try all combinations (2^n_buttons)
    for mask in range(1 << n_buttons):
        lights = [0] * n_lights  # Start with all lights off
        presses = 0

        # Check each button
        for i in range(n_buttons):
            if mask & (1 << i):  # Should we press button i?
                presses += 1
                # Toggle the lights this button affects
                for light in buttons[i]:
                    lights[light] ^= 1

        # Check if we matched the target
        if lights == target:
            min_presses = min(min_presses, presses)

    return min_presses


# Example usage:
def parse_line(line):
    """
    Parse a line like: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    """
    # Extract the target pattern between [ ]
    target_start = line.index('[') + 1
    target_end = line.index(']')
    target_str = line[target_start:target_end]
    target = [1 if char == '#' else 0 for char in target_str]

    # Extract buttons between ( )
    buttons = []
    import re
    button_matches = re.findall(r'\(([0-9,]+)\)', line)
    for match in button_matches:
        button = tuple(int(x) for x in match.split(','))
        buttons.append(button)

    return target, buttons


# Solve all machines
def solve_all_machines(input_text):
    total_presses = 0

    for line in input_text.strip().split('\n'):
        target, buttons = parse_line(line)
        min_presses = solve_machine_brute(target, buttons)
        total_presses += min_presses
        print(f"Machine: {min_presses} presses")

    return total_presses


# Example input
with open("day10.txt", "r") as file:
    result = solve_all_machines(file.read())
    print(result)
