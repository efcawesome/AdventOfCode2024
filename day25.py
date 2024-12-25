with open("day25input.txt") as f:
    input = [x.strip() for x in f.readlines()]

    locks = []
    keys = []

    for i in range(0, len(input), 8):
        is_lock = input[i] == "#####"
        curr = [-1, -1, -1, -1, -1]

        for j in range(i, i + 7):
            for k, c in enumerate(input[j]):
                if c == "#":
                    curr[k] += 1
    
        if is_lock:
            locks.append(curr)
        else:
            keys.append(curr)

def lock_key_fits(lock, key):
    for h1, h2 in zip(lock, key):
        if h1 + h2 > 5:
            return False
        
    return True

def puzzle1():
    fit_count = 0

    for lock in locks:
        for key in keys:
            fit_count += int(lock_key_fits(lock, key))

    return fit_count

print(puzzle1())
