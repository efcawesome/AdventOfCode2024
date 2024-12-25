with open("day19input.txt") as f:
    towels = [x for x in f.readline().strip().split(", ")]

    towel_dict = {}

    for towel in towels:
        try:
            towel_dict[len(towel)].append(towel)
        except:
            towel_dict[len(towel)] = [towel]

    patterns = [x.strip() for x in f.readlines()[1:]]

pattern_possiblities = {}

def pattern_is_possible(pattern):
    if len(pattern) == 0:
        return True

    try:
        return pattern_possiblities[pattern]
    except:
        is_possible = False
        for length in towel_dict:
            if length <= len(pattern) and pattern[:length] in towel_dict[length] and pattern_is_possible(pattern[length:]):
                is_possible = True

        pattern_possiblities[pattern] = is_possible

        return is_possible
    
pattern_counts = {}

def get_pattern_possibilities(pattern):
    if len(pattern) == 0:
        return 1
    
    try:
        return pattern_counts[pattern]
    except:
        count = 0
        for length in towel_dict:
            if length <= len(pattern) and pattern[:length] in towel_dict[length]:
                count += get_pattern_possibilities(pattern[length:])

        pattern_counts[pattern] = count

        return count

def puzzle1():
    count = 0

    for pattern in patterns:
        count += int(pattern_is_possible(pattern))
        print(pattern)

    return count

def puzzle2():
    possiblity_sum = 0

    for pattern in patterns:
        possiblity_sum += get_pattern_possibilities(pattern)

        print(pattern)

    return possiblity_sum

print(puzzle2())