with open("day18input.txt") as f:
    bytes = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in f.readlines()]

BYTE_COUNT = 1024
MAZE_SIZE = 71

def dijkstras(graph):
    dist = {}
    sptSet = set()

    for v in graph:
        dist[v] = 100000
        sptSet.add(v)

    dist[(0, 0)] = 0

    while len(sptSet) > 0:
        u = min(sptSet, key=dist.get)
        sptSet.remove(u)

        for v in graph[u]:
            new_dist = dist[u] + 1
            if new_dist < dist[v]:
                dist[v] = new_dist

    return dist[(MAZE_SIZE - 1, MAZE_SIZE - 1)]

def puzzle1():
    graph = {}

    for x in range(MAZE_SIZE):
        for y in range(MAZE_SIZE):
            if bytes.count((x, y)) == 0:
                graph[(x, y)] = []
                
                if x > 0 and bytes.count((x - 1, y)) == 0:
                    graph[(x, y)].append((x - 1, y))
                if x < MAZE_SIZE - 1 and bytes.count((x + 1, y)) == 0:
                    graph[(x, y)].append((x + 1, y))
                if y > 0 and bytes.count((x, y - 1)) == 0:
                    graph[(x, y)].append((x, y - 1))
                if y < MAZE_SIZE - 1 and bytes.count((x, y + 1)) == 0:
                    graph[(x, y)].append((x, y + 1))

    [print(f"{x}: {val}") for x, val in graph.items()]

    return dijkstras(graph)

def puzzle2():
    curr_ind = BYTE_COUNT

    curr_bytes = bytes[:curr_ind]
    graph = {}

    for x in range(MAZE_SIZE):
        for y in range(MAZE_SIZE):
            if curr_bytes.count((x, y)) == 0:
                graph[(x, y)] = []
                
                if x > 0 and curr_bytes.count((x - 1, y)) == 0:
                    graph[(x, y)].append((x - 1, y))
                if x < MAZE_SIZE - 1 and curr_bytes.count((x + 1, y)) == 0:
                    graph[(x, y)].append((x + 1, y))
                if y > 0 and curr_bytes.count((x, y - 1)) == 0:
                    graph[(x, y)].append((x, y - 1))
                if y < MAZE_SIZE - 1 and curr_bytes.count((x, y + 1)) == 0:
                    graph[(x, y)].append((x, y + 1))
    
    while dijkstras(graph) < 100000:
        new_byte = bytes[curr_ind]

        graph.pop(new_byte)

        for v in graph.values():
            if v.count(new_byte) != 0:
                v.remove(new_byte)

        curr_ind += 1


    return bytes[curr_ind - 1]

print(puzzle2())