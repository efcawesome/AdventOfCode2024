from collections import defaultdict

with open("day20input.txt") as f:
    maze = [[z for z in x.strip()] for x in f.readlines()]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_endpoints():
    start = (0, 0)
    end = (0, 0)

    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                end = (i, j)

    return start, end

def make_path(start, end):
    path = [start]
    curr = (start[0], start[1])

    while curr != end:
        for d in directions:
            new_pos = (curr[0] + d[0], curr[1] + d[1])

            if new_pos not in path and maze[new_pos[0]][new_pos[1]] != "#":
                path.append(new_pos)
                curr = new_pos
                break

    return path

def puzzle1():
    start, end = get_endpoints()

    path = make_path(start, end)

    skips = defaultdict(int)

    for i, point in enumerate(path):
        for dx, dy in directions:
            new_point = (point[0] + dx, point[1] + dy)
            try:
                skip_to = (new_point[0] + dx, new_point[1] + dy)

                if path.index(skip_to) > i and maze[new_point[0]][new_point[1]] == "#" and maze[skip_to[0]][skip_to[1]] != "#":
                    skip_amount = path.index(skip_to) - i - 2

                    skips[skip_amount] += 1
            except:
                continue
            
    result = 0

    for k, v in skips.items():
        if k >= 100:
            result += v

    return result

def puzzle2():
    start, end = get_endpoints()

    path = make_path(start, end)

    skips = defaultdict(int)

    for i, point in enumerate(path):
        jumped_points = set()
        for dx in range(-20, 21):
            for dy in range(-20, 21):
                if (abs(dx) > 1 or abs(dy) > 1) and abs(dx) + abs(dy) <= 20:
                    try:
                        skip_to = (point[0] + dx, point[1] + dy)

                        if path.index(skip_to) > i and maze[skip_to[0]][skip_to[1]] != "#":
                            skip_amount = path.index(skip_to) - i - (abs(dx) + abs(dy))
                            if skip_to not in jumped_points:
                                jumped_points.add(skip_to)
                                skips[skip_amount] += 1
                    except:
                        continue

    result = 0

    print({k:v for k,v in skips.items() if k >= 50})

    for k, v in skips.items():
        if k >= 100:
            result += v

    return result

print(puzzle2())