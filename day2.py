with open("day2input.txt") as f:
    reports = [[int(z) for z in x.strip().split(" ")] for x in f.readlines()]

print(reports)

def is_safe(report):
    safe = True
    increasing = report[1] - report[0] > 0
    for i in range(1, len(report)):
        if abs(report[i - 1] - report[i]) < 1 or abs(report[i - 1] - report[i]) > 3:
            safe = False

        if (increasing and report[i] - report[i - 1] < 0) or (not increasing and report[i] - report[i - 1] > 0):
            safe = False
    
    return safe

def puzzle1():
    safecount = 0

    for report in reports:
        if is_safe(report):
            safecount += 1

    return safecount

def puzzle2():
    safecount = 0

    for report in reports:
        if is_safe(report):
            safecount += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1:]):
                    safecount += 1
                    break

    return safecount

print(puzzle2())