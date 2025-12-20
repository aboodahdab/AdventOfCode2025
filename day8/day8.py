from collections import Counter
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

    # Process the first 1000 pairs
    print(len(circuits))
    for idx in range(min(1000, len(circuits)//2)):
        distance, box_i, box_j = pairs[idx]

        circuit_of_i = circuits[box_i]
        circuit_of_j = circuits[box_j]

        if circuit_of_i == circuit_of_j:
            continue

        for k in range(len(circuits)):
            if circuits[k] == circuit_of_j:
                circuits[k] = circuit_of_i

    sizes = sorted(Counter(circuits).values(), reverse=True)
    print(f"Circuits: {len(sizes)}, Top 3: {sizes[:3]}")
    print(f"Answer: {sizes[0] * sizes[1] * sizes[2]}")


# Read input
with open(PUZZLE_FILENAME, "r") as file:
    boxes = []
    for line in file:
        coords = line.strip().split(",")
        boxes.append(tuple(coords))

    solve(boxes)
