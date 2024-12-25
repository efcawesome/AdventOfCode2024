with open("day10input.txt") as f:
    trails = [[int(z) for z in x.strip()] for x in f.readlines()]

def get_trail_count(i, j, found_nines):
    if trails[i][j] == 9 and found_nines.count((i, j)) == 0:
        found_nines.append((i, j))
        return 1
    
    curr = trails[i][j]

    count = 0

    if i > 0 and trails[i - 1][j] - curr == 1:
        count += get_trail_count(i - 1, j, found_nines)
    if i < len(trails) - 1 and trails[i + 1][j] - curr == 1:
        count += get_trail_count(i + 1, j, found_nines)
    if j > 0 and trails[i][j - 1] - curr == 1:
        count += get_trail_count(i, j - 1, found_nines)
    if j < len(trails[i]) - 1 and trails[i][j + 1] - curr == 1:
        count += get_trail_count(i, j + 1, found_nines)

    return count

def get_unique_trail_count(i, j):
    if trails[i][j] == 9:
        return 1
    
    curr = trails[i][j]

    count = 0

    if i > 0 and trails[i - 1][j] - curr == 1:
        count += get_unique_trail_count(i - 1, j)
    if i < len(trails) - 1 and trails[i + 1][j] - curr == 1:
        count += get_unique_trail_count(i + 1, j)
    if j > 0 and trails[i][j - 1] - curr == 1:
        count += get_unique_trail_count(i, j - 1)
    if j < len(trails[i]) - 1 and trails[i][j + 1] - curr == 1:
        count += get_unique_trail_count(i, j + 1)

    return count    

def puzzle1():
    count = 0

    for i, row in enumerate(trails):
        for j, n in enumerate(row):
            if n == 0:
                found_nines = []
                count += get_trail_count(i, j, found_nines)

    return count

def puzzle2():
    count = 0

    for i, row in enumerate(trails):
        for j, n in enumerate(row):
            if n == 0:
                count += get_unique_trail_count(i, j)

    return count



print(puzzle2())