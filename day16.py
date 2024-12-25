
from copy import deepcopy

with open("day16input.txt") as f:
    maze = [[c for c in x.strip()] for x in f.readlines()]

def get_start():
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == "S":
                return (i, j)
            
def print_maze(pos, dir):
    for i, row in enumerate(maze):
        result = ""
        for j, c in enumerate(row):
            if i == pos[0] and j == pos[1]:
                match dir:
                    case (-1, 0):
                        result += "^"
                    case (1, 0):
                        result += "v"
                    case (0, -1):
                        result += "<"
                    case (0, 1):
                        result += ">"
            else:
                result += c

        print(result)
    
    print()

def get_endpoints():
    start = (0, 0)
    end = (0, 0)
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == "S":
                start = (i, j)
            elif c == "E":
                end = (i, j)
            
    return start, end

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def create_graph():
    graph = {}

    for d in directions:
        for i, row in enumerate(maze):
            for j, c in enumerate(row):
                if c != "#":
                    graph[(i, j, d)] = []

                    if maze[i + d[0]][j + d[1]] != "#":
                        graph[(i, j, d)].append((i + d[0], j + d[1], d))
                    if maze[i - d[1]][j - d[0]] != "#":
                        graph[(i, j, d)].append((i - d[1], j - d[0], (-d[1], -d[0])))
                    if maze[i + d[1]][j + d[0]] != "#":
                        graph[(i, j, d)].append((i + d[1], j + d[0], (d[1], d[0])))

    return graph

def dijkstras(start, fin, graph):
    dist = {}
    p_set = set()

    for v in graph:
        dist[v] = 10000000000
        p_set.add(v)

    dist[start] = 0

    while len(p_set) > 0:
        u = min(p_set, key=dist.get)
        p_set.remove(u)

        for v in graph[u]:
            new_dist = dist[u] + 1
            if v[2] != u[2]:
                new_dist += 1000

            if new_dist < dist[v]:
                dist[v] = new_dist

    results = []

    for d in directions:
        try:
            results.append(dist[(fin[0], fin[1], d)])
        except:
            continue

    return min(results)

def puzzle1():
    start, fin = get_endpoints()
    
    return dijkstras((start[0], start[1], (0, 1)), fin, create_graph())

path_points = set()

def get_paths(start, end, prev):
    path_points.add((end[0], end[1]))
    
    if (end[0], end[1]) != (start[0], start[1]):
        for v in prev[end]:
            get_paths(start, v, prev)

def dijkstras_p2(start, fin, graph):
    dist = {}
    prev = {}

    p_set = set()

    for v in graph:
        dist[v] = 10000000000
        prev[v] = []
        p_set.add(v)

    dist[start] = 0

    while len(p_set) > 0:
        u = min(p_set, key=dist.get)
        p_set.remove(u)

        for v in graph[u]:
            new_dist = dist[u] + 1
            if v[2] != u[2]:
                new_dist += 1000

            if new_dist == dist[v]:
                prev[v].append(u)
            elif new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = [u]

    for d in directions:
        if dist[(fin[0], fin[1], d)] == 66404:
            get_paths(start, (fin[0], fin[1], d), prev)

    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if (i, j) in path_points:
                print("O", end="")
            else:
                print(c, end="")

        print()
    

    return len(path_points)

def puzzle2():
    start, fin = get_endpoints()
    
    return dijkstras_p2((start[0], start[1], (0, 1)), fin, create_graph())

print(puzzle2())