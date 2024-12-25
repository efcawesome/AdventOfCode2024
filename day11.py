import threading
import time


with open("day11input.txt") as f:
    stones = [int(x) for x in f.readline().strip().split(" ")]

def has_even_digit_count(num):
    return len(str(num)) % 2 == 0

def split_digits(num):
    num_str = str(num)
    length = int(len(num_str) / 2)
    num1 = int(num_str[:length])
    num2 = int(num_str[length:])

    return num1, num2

solutions = {}

def blink_store_solutions(stone, num_blinks):
    if num_blinks == 0:
        return 1

    count = 0

    if num_blinks > 0:
        try:
            for s in solutions[stone]:
                count += blink_store_solutions(s, num_blinks - 1)
        except:
            if stone == 0:
                solutions[0] = [1]
                count += blink_store_solutions(1, num_blinks - 1)
            elif has_even_digit_count(stone):
                new_stones = split_digits(stone)
                solutions[stone] = [new_stones[0], new_stones[1]]

                count += blink_store_solutions(new_stones[0], num_blinks - 1)
                count += blink_store_solutions(new_stones[1], num_blinks - 1)
            else:
                solutions[stone] = [stone * 2024]
                count += blink_store_solutions(stone * 2024, num_blinks - 1)

    return count



def get_next_stone(stone):
    if stone == 0:
        return [1]
    elif has_even_digit_count(stone):
        return split_digits(stone)
    else:
        return [stone * 2024]

def puzzle2():
    stone_counts = {}

    start_time = time.time()

    total = 0

    #for stone in stones:
    #    print(stone)
    #    count += blink_store_solutions(stone, 75)
    for s in stones:
        stone_counts[s] = 1

    for c in range(1000):
        new_stone_counts = {}

        for stone, count in stone_counts.items():
            new_stone = get_next_stone(stone)

            for s in new_stone:
                try:
                    new_stone_counts[s] += count
                except:
                    new_stone_counts[s] = count

        stone_counts = new_stone_counts

    for n in stone_counts.values():
        total += n

    end_time = time.time()
    print(end_time - start_time)

    return total

def puzzle1():
    for count in range(25):
        i = 0

        while i < len(stones):
            curr = stones[i]

            if curr == 0:
                stones[i] = 1
            elif has_even_digit_count(curr):
                new_stones = split_digits(curr)
                stones[i] = new_stones[1]
                stones.insert(i, new_stones[0])
                i += 1
            else:
                stones[i] *= 2024

            i += 1

    return len(stones)
            
print(puzzle2())