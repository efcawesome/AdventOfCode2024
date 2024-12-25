with open("day8input.txt") as f:
    input = [[z for z in x.strip()] for x in f.readlines()]

def puzzle1():
    antinodes = set()

    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c != ".":
                for i1 in range(i + 1, len(input)):
                    row1 = input[i1]

                    for j1, c1 in enumerate(row1):
                        if c1 == c: # same signal
                            diff = (abs(i - i1), abs(j - j1))

                            if j < j1:
                                if i - diff[0] >= 0 and j - diff[1] >= 0:
                                    antinodes.add((i - diff[0], j - diff[1]))
                                if i1 + diff[0] < len(input) and j1 + diff[1] < len(input[0]):
                                    antinodes.add((i1 + diff[0], j1 + diff[1]))
                            else:
                                if i - diff[0] >= 0 and j + diff[1] < len(input):
                                    antinodes.add((i - diff[0], j + diff[1]))
                                if i1 + diff[0] < len(input) and j1 - diff[1] >= 0:
                                    antinodes.add((i1 + diff[0], j1 - diff[1]))

    print(antinodes)
    return len(antinodes)

def puzzle2():
    antinodes = set()

    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c != ".":
                for i1 in range(i + 1, len(input)):
                    row1 = input[i1]

                    for j1, c1 in enumerate(row1):
                        if c1 == c: # same signal
                            diff = (abs(i - i1), abs(j - j1))

                            if j < j1:
                                curr_i = i
                                curr_j = j

                                while curr_i >= 0 and curr_j >= 0:
                                    antinodes.add((curr_i, curr_j))
                                    curr_i -= diff[0]
                                    curr_j -= diff[1]

                                curr_i = i1
                                curr_j = j1

                                while curr_i < len(input) and curr_j < len(input[0]):
                                    antinodes.add((curr_i, curr_j))
                                    curr_i += diff[0]
                                    curr_j += diff[1]
                            else:
                                curr_i = i
                                curr_j = j

                                while curr_i >= 0 and curr_j < len(input):
                                    antinodes.add((curr_i, curr_j))
                                    curr_i -= diff[0]
                                    curr_j += diff[1]

                                curr_i = i1
                                curr_j = j1

                                while curr_i < len(input) and curr_j >= 0:
                                    antinodes.add((curr_i, curr_j))
                                    curr_i += diff[0]
                                    curr_j -= diff[1]

    return len(antinodes)

print(puzzle2())