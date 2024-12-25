from collections import defaultdict

with open("day21input.txt") as f:
    keys = [x.strip() for x in f]

numpad = {'7':(0, 0), '8':(0, 1), '9':(0, 2),
          '4':(1, 0), '5':(1, 1), '6':(1, 2),
          '1':(2, 0), '2':(2, 1), '3':(2, 2),
                      '0':(3, 1), 'A':(3, 2)}

dirpad = {            "^":(0, 1), 'A':(0, 2),
          "<":(1, 0), "v":(1, 1), ">":(1, 2)}

def get_min_string(s1, s2):
    if s1 != "":
        if s2 != "":
            return min(s1, s2, key=len)
        else:
            return s1
    else:
        return s2

# PART 1
def get_intermediate_sequences(sequence, repeats):
    if repeats == 0:
        return sequence

    key_rob_pos = (0, 2)
    new_sequence = ""

    for c in sequence:
        pos_y, pos_x = dirpad[c]

        dy = pos_y - key_rob_pos[0]
        dx = pos_x - key_rob_pos[1]

        y_char = "^" if dy < 0 else "v"
        x_char = "<" if dx < 0 else ">"

        x_count = x_char * abs(dx)
        y_count = y_char * abs(dy)

        s1 = ""
        s2 = ""

        if key_rob_pos[1] != 0 or key_rob_pos[0] + dy != 0:
            s1 = get_intermediate_sequences(y_count + x_count + "A", repeats - 1)
        if key_rob_pos[0] != 0 or key_rob_pos[1] + dx != 0:
            s2 = get_intermediate_sequences(x_count + y_count + "A", repeats - 1)

        new_sequence += get_min_string(s1, s2)
        key_rob_pos = (pos_y, pos_x)

    return new_sequence

def get_sequences(key, repeats):
    num_rob_pos = (3, 2)
    sequence = ""

    for c in key:
        pos_y, pos_x = numpad[c]

        dy = pos_y - num_rob_pos[0]
        dx = pos_x - num_rob_pos[1]

        y_char = "^" if dy < 0 else "v"
        x_char = "<" if dx < 0 else ">"

        x_count = x_char * abs(dx)
        y_count = y_char * abs(dy)

        s1 = ""
        s2 = ""

        if num_rob_pos[1] != 0 or num_rob_pos[0] + dy != 3: # check for going over illegal space
            s1 = get_intermediate_sequences(y_count + x_count + "A", repeats)
        if num_rob_pos[0] != 3 or num_rob_pos[1] + dx != 0: # same as above
            s2 = get_intermediate_sequences(x_count + y_count + "A", repeats)

        sequence += get_min_string(s1, s2)

        num_rob_pos = (pos_y, pos_x)

    return sequence

results = {}

# PART 2
def get_intermediate_sequences_len(sequence, repeats):
    if repeats == 0:
        return len(sequence)
    
    if (sequence, repeats) in results:
        return results[(sequence, repeats)]

    key_rob_pos = (0, 2)
    length = 0

    for c in sequence:
        pos_y, pos_x = dirpad[c]

        dy = pos_y - key_rob_pos[0]
        dx = pos_x - key_rob_pos[1]

        y_char = "^" if dy < 0 else "v"
        x_char = "<" if dx < 0 else ">"

        x_count = x_char * abs(dx)
        y_count = y_char * abs(dy)

        l1 = 1000000000000000000
        l2 = 1000000000000000000

        if key_rob_pos[1] != 0 or key_rob_pos[0] + dy != 0:
            l1 = get_intermediate_sequences_len(y_count + x_count + "A", repeats - 1)
        if key_rob_pos[0] != 0 or key_rob_pos[1] + dx != 0:
            l2 = get_intermediate_sequences_len(x_count + y_count + "A", repeats - 1)

        length += min(l1, l2)
        key_rob_pos = (pos_y, pos_x)

    results[(sequence, repeats)] = length

    return length

def get_sequences_len(key, repeats):
    num_rob_pos = (3, 2)
    length = 0

    for c in key:
        pos_y, pos_x = numpad[c]

        dy = pos_y - num_rob_pos[0]
        dx = pos_x - num_rob_pos[1]

        y_char = "^" if dy < 0 else "v"
        x_char = "<" if dx < 0 else ">"

        x_count = x_char * abs(dx)
        y_count = y_char * abs(dy)

        l1 = 1000000000000000000000
        l2 = 1000000000000000000000

        if num_rob_pos[1] != 0 or num_rob_pos[0] + dy != 3: # check for going over illegal space
            l1 = get_intermediate_sequences_len(y_count + x_count + "A", repeats)
        if num_rob_pos[0] != 3 or num_rob_pos[1] + dx != 0: # same as above
            l2 = get_intermediate_sequences_len(x_count + y_count + "A", repeats)

        length += min(l1, l2)

        num_rob_pos = (pos_y, pos_x)

    return length

def get_complexity_sum(sequences):
    complexity_sum = 0

    for key, sequence in sequences.items():
        print(f"{key}: {sequence}")
        print(f"{len(sequence)} * {int(key[:-1])}")
        complexity_sum += len(sequence) * int(key[:-1])
    
    return complexity_sum

def puzzle1():
    sequences = {}

    for key in keys:
        sequences[key] = get_sequences(key, 2)

    return get_complexity_sum(sequences)

def puzzle2():
    sequences = {}

    complexity_sum = 0

    for key in keys:
        sequences[key] = get_sequences_len(key, 25)

    for k, v in sequences.items():
        print(f"{k}: {v}")

        complexity_sum += int(k[:-1]) * v

    return complexity_sum

print(puzzle2())