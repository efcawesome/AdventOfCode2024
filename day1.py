import time

with open("day1Input.txt") as f:
    l_list = []
    r_list = []

    for line in f.readlines():
        l_list.append(int(line.split("   ")[0]))
        r_list.append(int(line.split("   ")[1].strip()))

def puzzle_1():
    dist_sum = 0

    while len(l_list) > 0:
        min_l = min(l_list)
        min_r = min(r_list)

        dist_sum += abs(min_l - min_r)

        l_list.pop(l_list.index(min_l))
        r_list.pop(r_list.index(min_r))

    return dist_sum

def puzzle_2():
    sim_score = 0

    for n in l_list:
        sim_score += r_list.count(n) * n
    
    return sim_score

def fast_puzzle_2(): # added later
    r_list_counts = {}

    for n in r_list:
        try:
            r_list_counts[n] += 1
        except:
            r_list_counts[n] = 1

    total = 0
    for n in l_list:
        try:
            total += r_list_counts[n] * n
        except:
            continue

    return total

def time_func():
    s = time.time()

    print(fast_puzzle_2())

    print(time.time() - s)


time_func()