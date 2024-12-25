from copy import deepcopy

with open("day6input.txt") as f:
    input = [[z for z in x.strip()] for x in f.readlines()]

def puzzle1():
    guard_pos = [0, 0]

    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == "^":
                guard_pos = [i, j]
    
    while guard_pos[0] >= 1 and guard_pos[0] < len(input) - 1 and guard_pos[1] >= 1 and guard_pos[1] < len(input[0]) - 1:
        match input[guard_pos[0]][guard_pos[1]]:
            case "^":
                if input[guard_pos[0] - 1][guard_pos[1]] == "#":
                    input[guard_pos[0]][guard_pos[1]] = ">"
                else:
                    input[guard_pos[0] - 1][guard_pos[1]] = "^"
                    input[guard_pos[0]][guard_pos[1]] = "X"

                    guard_pos[0] -= 1
            case ">":
                if input[guard_pos[0]][guard_pos[1] + 1] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "v"
                else:
                    input[guard_pos[0]][guard_pos[1] + 1] = ">"
                    input[guard_pos[0]][guard_pos[1]] = "X"

                    guard_pos[1] += 1
            case "v":
                if input[guard_pos[0] + 1][guard_pos[1]] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "<"
                else:
                    input[guard_pos[0] + 1][guard_pos[1]] = "v"
                    input[guard_pos[0]][guard_pos[1]] = "X"

                    guard_pos[0] += 1
            case "<":
                if input[guard_pos[0]][guard_pos[1] - 1] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "^"
                else:
                    input[guard_pos[0]][guard_pos[1] - 1] = "<"
                    input[guard_pos[0]][guard_pos[1]] = "X"

                    guard_pos[1] -= 1

    input[guard_pos[0]][guard_pos[1]] = "X"

    x_count = 0
    for row in input:
        for col in row:
            if col == "X":
                x_count += 1

    return x_count

def run_sim(base_input, init_guard_pos, modification):
    if init_guard_pos == modification:
        return False

    input = deepcopy(base_input)
    input[modification[0]][modification[1]] = "#"
    positions = {"^":[deepcopy(init_guard_pos)],">":[],"<":[],"v":[]}
    guard_pos = deepcopy(init_guard_pos)

    while guard_pos[0] >= 1 and guard_pos[0] < len(input) - 1 and guard_pos[1] >= 1 and guard_pos[1] < len(input[0]) - 1:
        match input[guard_pos[0]][guard_pos[1]]:
            case "^":
                if input[guard_pos[0] - 1][guard_pos[1]] == "#":
                    input[guard_pos[0]][guard_pos[1]] = ">"
                else:
                    input[guard_pos[0] - 1][guard_pos[1]] = "^"
                    guard_pos[0] -= 1
            case ">":
                if input[guard_pos[0]][guard_pos[1] + 1] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "v"
                else:
                    input[guard_pos[0]][guard_pos[1] + 1] = ">"
                    guard_pos[1] += 1
            case "v":
                if input[guard_pos[0] + 1][guard_pos[1]] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "<"
                else:
                    input[guard_pos[0] + 1][guard_pos[1]] = "v"
                    guard_pos[0] += 1
            case "<":
                if input[guard_pos[0]][guard_pos[1] - 1] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "^"
                else:
                    input[guard_pos[0]][guard_pos[1] - 1] = "<"
                    guard_pos[1] -= 1

        if positions[input[guard_pos[0]][guard_pos[1]]].count(guard_pos) > 0:
            return True
        
        positions[input[guard_pos[0]][guard_pos[1]]].append(deepcopy(guard_pos))
        
    return False

def puzzle2():
    init_guard_pos = [0, 0]
    base_input = deepcopy(input)

    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == "^":
                init_guard_pos = [i, j]

    guard_pos = deepcopy(init_guard_pos)

    count = 0
    tests = 0

    tested_spots = []

    while guard_pos[0] >= 1 and guard_pos[0] < len(input) - 1 and guard_pos[1] >= 1 and guard_pos[1] < len(input[0]) - 1:
        match input[guard_pos[0]][guard_pos[1]]:
            case "^":
                if input[guard_pos[0] - 1][guard_pos[1]] == "#":
                    input[guard_pos[0]][guard_pos[1]] = ">"
                else:
                    if tested_spots.count([guard_pos[0] - 1, guard_pos[1]]) == 0 and run_sim(base_input, init_guard_pos, [guard_pos[0] - 1, guard_pos[1]]):
                        count += 1

                    tests += 1
                    tested_spots.append([guard_pos[0] - 1, guard_pos[1]])
                        
                    input[guard_pos[0] - 1][guard_pos[1]] = "^"
                    guard_pos[0] -= 1
            case ">":
                if input[guard_pos[0]][guard_pos[1] + 1] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "v"
                else:
                    if tested_spots.count([guard_pos[0], guard_pos[1] + 1]) == 0 and run_sim(base_input, init_guard_pos, [guard_pos[0], guard_pos[1] + 1]):
                        count += 1

                    tests += 1
                    tested_spots.append([guard_pos[0], guard_pos[1] + 1])

                    input[guard_pos[0]][guard_pos[1] + 1] = ">"
                    guard_pos[1] += 1
            case "v":
                if input[guard_pos[0] + 1][guard_pos[1]] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "<"
                else:
                    if tested_spots.count([guard_pos[0] + 1, guard_pos[1]]) == 0 and run_sim(base_input, init_guard_pos, [guard_pos[0] + 1, guard_pos[1]]):
                        count += 1

                    tests += 1
                    tested_spots.append([guard_pos[0] + 1, guard_pos[1]])                        
                    input[guard_pos[0] + 1][guard_pos[1]] = "v"
                    guard_pos[0] += 1
            case "<":
                if input[guard_pos[0]][guard_pos[1] - 1] == "#":
                    input[guard_pos[0]][guard_pos[1]] = "^"
                else:
                    if tested_spots.count([guard_pos[0], guard_pos[1] - 1]) == 0 and run_sim(base_input, init_guard_pos, [guard_pos[0], guard_pos[1] - 1]):
                        count += 1

                    tests += 1
                    tested_spots.append([guard_pos[0], guard_pos[1] - 1])
                    input[guard_pos[0]][guard_pos[1] - 1] = "<"
                    guard_pos[1] -= 1

    print(tests)

    return count

print(puzzle2())