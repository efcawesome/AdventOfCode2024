with open("day5input.txt") as f:
    rules = []
    ind = 0
    input = [x.strip() for x in f.readlines()]
    
    while input[ind] != "":
        rule = input[ind].split("|")
        rules.append((int(rule[0]), int(rule[1])))
        ind += 1

    updates = [[int(z) for z in x.split(",")] for x in input[ind + 1:]]

print(rules)
print(updates)

def get_mid(row):
    return row[int(len(row) / 2)]

def is_legal(update):
    for rule in rules:
        if update.count(rule[0]) > 0:
            if update.count(rule[1]) > 0 and update.index(rule[0]) > update.index(rule[1]):
                return False
            
    return True

def puzzle1():
    count = 0

    for update in updates:
        if is_legal(update):
            count += get_mid(update)

    return count

def puzzle2():
    count = 0

    for update in updates:
        if not is_legal(update):
            while not is_legal(update):
                for rule in rules:
                    if update.count(rule[0]) > 0:
                        if update.count(rule[1]) > 0 and update.index(rule[0]) > update.index(rule[1]): 
                            # swap them
                            temp = update.index(rule[1])
                            update[update.index(rule[0])] = rule[1]
                            update[temp] = rule[0]
                            break

            count += get_mid(update)

    return count



print(puzzle2())