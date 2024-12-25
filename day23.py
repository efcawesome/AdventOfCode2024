from collections import defaultdict

with open("day23input.txt") as f:
    connections = defaultdict(set)

    for line in f.readlines():
        split_line = line.strip().split("-")
    
        connections[split_line[0]].add(split_line[1])
        connections[split_line[1]].add(split_line[0])

def get_mutual_connections(computer, so_far):
    for other in connections[computer]:
        if other not in so_far:
            other_connections = connections[other]

            has_all_connections = True

            for c in so_far:
                if c not in other_connections:
                    has_all_connections = False
                    break

            if has_all_connections:
                so_far.add(other)

                for new_c in other_connections:
                    if new_c not in so_far:
                        get_mutual_connections(new_c, so_far)

    return so_far

def puzzle1():
    tri_set = set()

    for computer, others in connections.items():
        for other_comp in others:
            for final_comp in connections[other_comp]:
                if final_comp in others:
                    tri_set.add(tuple(sorted((computer, other_comp, final_comp))))

    t_count = 0

    for ts in tri_set:
        for c in ts:
            if c[0] == "t":
                t_count += 1
                break

    return t_count

def puzzle2():
    parties = set()

    for computer in connections:
        party = get_mutual_connections(computer, set())

        parties.add(tuple(sorted(party)))

    max_party = max(parties, key=len)

    result = ""

    for c in max_party:
        result += c + ","

    result = result[:-1]

    return result


print(puzzle2())