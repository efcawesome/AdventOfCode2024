with open("day4input.txt") as f:
    input = [[z for z in x.strip()] for x in f.readlines()]

def check_xmas(i, j, di, dj):
    pass    

def puzzle1():
    count = 0

    # atrocious code
    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c == "X":
                possibilities = []
                if j >= 3: # backwards
                    possibilities.append(row[j] + row[j - 1] + row[j - 2] + row[j - 3])
                if j <= len(row) - 4: # forwards
                    possibilities.append(row[j] + row[j + 1] + row[j + 2] + row[j + 3])
                if i >=  3: # up
                    possibilities.append(input[i][j] + input[i - 1][j] + input[i - 2][j] + input[i - 3][j])

                    if j >= 3: # up left
                        possibilities.append(input[i][j] + input[i - 1][j - 1] + input[i - 2][j - 2] + input[i - 3][j - 3])
                    if j <= len(row) - 4:
                        possibilities.append(input[i][j] + input[i - 1][j + 1] + input[i - 2][j + 2] + input[i - 3][j + 3])

                if i <= len(input) - 4: # down
                    possibilities.append(input[i][j] + input[i + 1][j] + input[i + 2][j] + input[i + 3][j])

                    if j >= 3: # down left
                        possibilities.append(input[i][j] + input[i + 1][j - 1] + input[i + 2][j - 2] + input[i + 3][j - 3])
                    if j <= len(row) - 4: # down right
                        possibilities.append(input[i][j] + input[i + 1][j + 1] + input[i + 2][j + 2] + input[i + 3][j + 3])

                for s in possibilities:
                    if s == "XMAS":
                        count += 1

    return count

def puzzle2():
    count = 0

    for i in range(1, len(input) - 1):
        for j in range(1, len(input[i]) - 1):
            if input[i][j] == "A":
                if input[i - 1][j - 1] != input[i + 1][j + 1]:
                    cross_words = [input[i - 1][j - 1], input[i - 1][j + 1], input[i + 1][j - 1], input[i + 1][j + 1]]

                    if cross_words.count("M") == cross_words.count("S") == 2    :
                        count += 1

    return count

print(puzzle2())