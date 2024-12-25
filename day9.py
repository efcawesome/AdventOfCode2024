with open("day9input.txt") as f:
    input = [int(x) for x in f.readline().strip()]

def get_disk():
    curr_id = 0
    disk = []

    is_files = True

    for n in input:
        if is_files:
            [disk.append(curr_id) for i in range(n)]
            curr_id += 1
        else:
            [disk.append(-1) for i in range(n)]
        
        is_files = not is_files

    return disk

def get_checksum(disk):
    checksum = 0
    for i, num in enumerate(disk):
        if num == -1:
            continue
        
        checksum += i * num

    return checksum


def puzzle1():
    disk = get_disk()

    beginning = 0
    end = len(disk) - 1

    while end > beginning:
        if disk[beginning] == -1:
            while disk[end] == -1:
                end -= 1
            if end <= beginning:
                break
            disk[beginning] = disk[end]
            disk[end] = -1
            end -= 1
        
        beginning += 1

    return get_checksum(disk)

def get_len_empty_space(start, disk):
    count = 0

    for i in range(start, len(disk)):
        if disk[i] == -1:
            count += 1
        else:
            return count

    return count

def get_len_curr_id(end, curr_id, disk):
    count = 0

    for i in range(end, 0, -1):
        if disk[i] == curr_id:
            count += 1
        else:
            return count, i + 1
        
    return count, -1



def puzzle2():
    disk = get_disk()

    beginning = 0
    end = len(disk) - 1
    curr_id = disk[end]

    while curr_id >= 0:
        if disk[beginning] == -1:
            empty_len = get_len_empty_space(beginning, disk)

            while disk[end] != curr_id:
                end -= 1

            if end > beginning:
                end_len, pos = get_len_curr_id(end, curr_id, disk)
                    
                if end_len <= empty_len:
                    for i in range(0, end_len):
                        disk[beginning + i] = disk[pos + i]
                        disk[pos + i] = -1
            else:
                end = len(disk) - 1
                curr_id -= 1
                beginning = -1
    
        beginning += 1
        
    print(disk)
    return get_checksum(disk)

print(puzzle2())