from collections import defaultdict

with open("day22input.txt") as f:
    secret_nums = [int(x.strip()) for x in f.readlines()]

PRUNE_NUM = 2 ** 24

def get_next_secret_num(num):
    num = ((num << 6) ^ num) % PRUNE_NUM # step 1
    num = ((num >> 5) ^ num) % PRUNE_NUM # step 2
    num = ((num << 11) ^ num) % PRUNE_NUM # step 3

    return num

def puzzle1():
    total = 0

    for num in secret_nums:
        for i in range(2000):
            num = get_next_secret_num(num)

        total += num

    return total

def puzzle2():
    sequences = defaultdict(int)

    for num in secret_nums:
        seen_sequences = set()
        prev_nums = [(num % 10, 0)]

        for i in range(2000):
            num = get_next_secret_num(num)
            cost = num % 10
            prev_nums.append((cost, cost - prev_nums[-1][0]))

            if len(prev_nums) > 4:
                prev_nums.pop(0)

            if i >= 3:
                sequence = (prev_nums[0][1], prev_nums[1][1], prev_nums[2][1], prev_nums[3][1])
                
                if sequence not in seen_sequences:
                    sequences[sequence] += prev_nums[3][0]
                    seen_sequences.add(sequence)

    print(max(sequences, key=sequences.get))
    return max(sequences.values())

print(puzzle2())