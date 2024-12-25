with open("day13input.txt") as f:
    machines = []
    curr_line = 0
    curr_list = []

    for line in f.readlines():
        if curr_line <= 1:
            x_increase = int(line.split("+")[1].split(",")[0])
            y_increase = int(line.split("+")[2])
            curr_list.append((x_increase, y_increase))
        elif curr_line == 2:
            x_goal = int(line.split("=")[1].split(",")[0])
            y_goal = int(line.split("=")[2])
            curr_list.append((x_goal, y_goal))
        else:
            machines.append(curr_list)
            curr_list = []
            curr_line = -1

        curr_line += 1

    machines.append(curr_list)

def puzzle1():
    total_cost = 0

    for a_comands, b_commands, goals in machines:
        min_cost = 1000
        x_goal = goals[0]
        y_goal = goals[1]
        a_x = a_comands[0]
        a_y = a_comands[1]
        b_x = b_commands[0]
        b_y = b_commands[1]

        for a_presses in range(101):
            for b_presses in range(101):
                if a_presses * a_x + b_presses * b_x == x_goal and a_presses * a_y + b_presses * b_y == y_goal:
                    print(f"{a_presses}, {b_presses}")
                    min_cost = min(min_cost, a_presses * 3 + b_presses)
                    
        if min_cost != 1000:
            total_cost += min_cost

    return total_cost

def puzzle2():
    total_cost = 0

    for a_comands, b_commands, goals in machines:
        x_goal = goals[0] + 10000000000000
        y_goal = goals[1] + 10000000000000
        a_x = a_comands[0]
        a_y = a_comands[1]
        b_x = b_commands[0]
        b_y = b_commands[1]

        b_sol = (x_goal - (a_x/a_y)*y_goal)/(b_x - (a_x / a_y * b_y))
        a_sol = (x_goal - b_x * round(b_sol))/a_x

        if a_sol >= 0 and b_sol >= 0 and abs(b_sol - round(b_sol)) < 0.01 and abs(a_sol - round(a_sol)) < 0.01:
            print(f"{a_sol}, {b_sol}")
            total_cost += round(a_sol) * 3 + round(b_sol)

    return total_cost

print(puzzle2())