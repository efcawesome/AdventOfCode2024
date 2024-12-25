with open("day7input.txt") as f:
    input = [[int(z.strip(":")) for z in x.split(" ")] for x in f.readlines()]

def concatenate(n, n1):
    return int(str(n) + str(n1))

def has_solution_1(n, nums, soFar, i):
    if i == len(nums) - 1:
        return soFar + nums[i] == n or soFar * nums[i] == n

    return has_solution_1(n, nums, soFar + nums[i], i + 1) or has_solution_1(n, nums, soFar * nums[i], i + 1)

def has_solution_2(n, nums, soFar, i):
    if i == len(nums) - 1:
        return soFar + nums[i] == n or soFar * nums[i] == n or concatenate(soFar, nums[i]) == n

    return has_solution_2(n, nums, soFar + nums[i], i + 1) or has_solution_2(n, nums, soFar * nums[i], i + 1) or has_solution_2(n, nums, concatenate(soFar, nums[i]), i + 1)

def puzzle1():
    count = 0
    for line in input:
        if has_solution_1(line[0], line[2:], line[1], 0):
            count += line[0]

    return count

def puzzle2():
    count = 0
    for line in input:
        if has_solution_2(line[0], line[2:], line[1], 0):
            count += line[0]

    return count

print(puzzle2())