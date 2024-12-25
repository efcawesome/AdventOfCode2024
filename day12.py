from copy import deepcopy

with open("day12input.txt") as f:
    garden = [[z for z in x.strip()] for x in f.readlines()]

def get_region(plot_type, i, j, points):
    if i >= 0 and j >= 0 and i < len(garden) and j < len(garden[0]):
        if garden[i][j] == plot_type and points.count((i, j)) == 0:
            points.append((i, j))
        
            get_region(plot_type, i - 1, j, points)
            get_region(plot_type, i + 1, j, points)
            get_region(plot_type, i, j - 1, points)
            get_region(plot_type, i, j + 1, points)

def get_perimeter_sides(i, j):
    plot_type = garden[i][j]

    count = 0

    if i == 0 or garden[i - 1][j] != plot_type:
        count += 1
    if i == len(garden) - 1 or garden[i + 1][j] != plot_type:
        count += 1
    if j == 0 or garden[i][j - 1] != plot_type:
        count += 1
    if j == len(garden[0]) - 1 or garden[i][j + 1] != plot_type:
        count += 1

    return count

def puzzle1():
    regions = []

    used_points = []

    for i, row in enumerate(garden):
        for j, plot in enumerate(row):
            if used_points.count((i, j)) == 0:
                temp = []
                get_region(plot, i, j, temp)
                regions.append(temp)
                [used_points.append(x) for x in temp]

    total_cost = 0

    for region in regions:
        cost = len(region)
        perimeter = 0

        for i, j in region:
            perimeter += get_perimeter_sides(i, j)

        cost *= perimeter
        total_cost += cost
            
    return total_cost

def get_i_dict(region):
    i_vals = {}
    
    for i, j in region:
        try:
            i_vals[i].append(j)
        except:
            i_vals[i] = [j]

    return i_vals

def get_j_dict(region):
    j_vals = {}
    
    for i, j in region:
        try:
            j_vals[j].append(i)
        except:
            j_vals[j] = [i]

    return j_vals

def get_up_side_count(region):
    i_vals = get_i_dict(region)

    side_count = 0

    for i, plots in i_vals.items():
        plots.sort()
        prev_plot = -2
        for j in plots:
            if i == 0 or garden[i - 1][j] != garden[i][j]:
                if j - prev_plot > 1:
                    side_count += 1
                
                prev_plot = j

    return side_count

def get_down_side_count(region):
    i_vals = get_i_dict(region)

    side_count = 0

    for i, plots in i_vals.items():
        plots.sort()
        prev_plot = -2
        for j in plots:
            if i == len(garden) - 1 or garden[i + 1][j] != garden[i][j]:
                if j - prev_plot > 1:
                    side_count += 1
                
                prev_plot = j

    return side_count

def get_left_side_count(region):
    j_vals = get_j_dict(region)

    side_count = 0

    for j, plots in j_vals.items():
        plots.sort()
        prev_plot = -2
        for i in plots:
            if j == 0 or garden[i][j - 1] != garden[i][j]:
                if i - prev_plot > 1:
                    side_count += 1
                
                prev_plot = i

    return side_count

def get_right_side_count(region):
    j_vals = get_j_dict(region)

    side_count = 0

    for j, plots in j_vals.items():
        plots.sort()
        prev_plot = -2
        for i in plots:
            if j == len(garden[0]) - 1 or garden[i][j + 1] != garden[i][j]:
                if i - prev_plot > 1:
                    side_count += 1
                
                prev_plot = i

    return side_count

def get_side_count(region):
    return get_up_side_count(region) + get_down_side_count(region) + get_left_side_count(region) + get_right_side_count(region)

def puzzle2():
    regions = []

    used_points = []

    for i, row in enumerate(garden):
        for j, plot in enumerate(row):
            if used_points.count((i, j)) == 0:
                temp = []
                get_region(plot, i, j, temp)
                regions.append(temp)
                [used_points.append(x) for x in temp]

    total_cost = 0

    for region in regions:
        cost = len(region)

        side_count = get_side_count(region)

        cost *= side_count
        total_cost += cost
            
    return total_cost

print(puzzle2())