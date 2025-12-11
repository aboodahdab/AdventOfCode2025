
PUZZLE_FILENAME = "day8puzzle.txt"
STOP_AFTER_CONNECTIONS_NUMBER = 1000


def calculate_distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return (int(x2) - int(x1))**2 + (int(y2) - int(y1))**2 + (int(z2) - int(z1))**2


def solve(boxes):
    pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distance = calculate_distance(boxes[i], boxes[j])
            pairs.append((distance, i, j))

    pairs.sort()
    circuits = list(range(len(boxes)))
    last_variable = ""
    # Process the first 1000 pairs
    for idx, (distance, box_i, box_j) in enumerate(pairs):

        circuit_of_i = circuits[box_i]
        circuit_of_j = circuits[box_j]

        if circuit_of_i == circuit_of_j:
            continue

        for k in range(len(circuits)):
            if circuits[k] == circuit_of_j:
                circuits[k] = circuit_of_i
                last_variable = (box_i, box_j)
    if len(set(circuits)) == 1:
            box_i_index = last_variable[0]
            box_j_index = last_variable[1]

            x_of_box_i = int(boxes[box_i_index][0])  # Get X coordinate of first box
            x_of_box_j = int(boxes[box_j_index][0])  # Get X coordinate of second box

            answer = x_of_box_i * x_of_box_j
            print(answer)


# Read input
with open(PUZZLE_FILENAME, "r") as file:
    boxes = []
    for line in file:
        coords = line.strip().split(",")
        boxes.append(tuple(coords))

    solve(boxes)
