with open("day14input.txt") as f:
    robots = [[[int(x.split(",")[0].split("=")[1]), int(x.split(",")[1].split(" ")[0])], [int(x.split(",")[1].split("=")[1]), int(x.split(",")[2])]] for x in f.readlines()]

def move_robots(x_max, y_max):
    for pos, vel in robots:
        pos[0] += vel[0]
        pos[1] += vel[1]

        if pos[0] >= x_max:
            pos[0] -= x_max
        elif pos[0] < 0:
            pos[0] += x_max
        if pos[1] >= y_max:
            pos[1] -= y_max
        elif pos[1] < 0:
            pos[1] += y_max

def get_safety_factor(x_max, y_max):
    quadrants = [0] * 4

    for pos, vel in robots:
        x = pos[0]
        y = pos[1]
        mid_x = int(x_max / 2)
        mid_y = int(y_max / 2)

        if x < mid_x:
            if y < mid_y:
                quadrants[0] += 1
            elif y > mid_y:
                quadrants[1] += 1
        elif x > mid_x:
            if y < mid_y:
                quadrants[2] += 1
            elif y > mid_y:
                quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

def print_robots(x_max, y_max, seconds):
    positions = [["." for j in range(x_max)] for i in range(y_max)]

    for pos, vel in robots:
        positions[pos[1]][pos[0]] = "O"

    has_long_row = False
    for row in positions:
        count = 0

        for i in range(1, len(row)):
            if row[i] == "O":
                if row[i - 1] == "O":
                    count += 1
                else:
                    count = 1
                
                if count >= 10:
                    has_long_row = True
            

    if has_long_row:
        with open("day14output.txt", "a") as f:
            f.write(str(seconds) + "\n")

            for r in positions:
                newline = ""
                for c in r:
                    newline += c

                newline += "\n"

                f.write(newline)

            f.write("\n")

def puzzle1():
    x_max = 101
    y_max = 103

    for i in range(10000):
        move_robots(x_max, y_max)

        print_robots(x_max, y_max, i + 1)

    return get_safety_factor(x_max, y_max)

print(puzzle1())

    