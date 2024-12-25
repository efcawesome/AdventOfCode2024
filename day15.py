with open("day15input.txt") as f:
    input = [x.strip() for x in f.readlines()]

    box_map = []
    instructions = []

    is_map = True

    for row in input:
        if row == "":
            is_map = False
        elif is_map:
            new_row = []

            for c in row:
                
                match c:
                    case "#":
                        new_row.append("#")
                        new_row.append("#")
                    case "O":
                        new_row.append("[")
                        new_row.append("]")
                    case ".":
                        new_row.append(".")
                        new_row.append(".")
                    case "@":
                        new_row.append("@")
                        new_row.append(".")
            
            box_map.append(new_row)
                
        else:
            for c in row:
                match c:
                    case "<":
                        instructions.append((0, -1))
                    case "v":
                        instructions.append((1, 0))
                    case "^":
                        instructions.append((-1, 0))
                    case ">":
                        instructions.append((0, 1))

def get_init_robot_pos():
    for i, row in enumerate(box_map):
        for j, c in enumerate(row):
            if c == "@":
                return [i, j]
            
def get_gps_sum():
    total = 0
    
    for i, row in enumerate(box_map):
        for j, c in enumerate(row):
            if c == "O":
                total += 100 * i + j

    return total

def puzzle1():
    pos = get_init_robot_pos()

    for instruction in instructions:
        new_pos_x = pos[1] + instruction[1]
        new_pos_y = pos[0] + instruction[0]

        can_move = True

        if box_map[new_pos_y][new_pos_x] == "#":
            can_move = False

        if instruction[1] != 0:
            while box_map[pos[0]][new_pos_x] == "O":
                new_pos_x += instruction[1]
            if box_map[pos[0]][new_pos_x] == "#":
                can_move = False
        else:
            while box_map[new_pos_y][pos[1]] == "O":
                new_pos_y += instruction[0]
            if box_map[new_pos_y][pos[1]] == "#":
                can_move = False

        if can_move:
            if instruction[1] != 0:
                box_map[pos[0]][new_pos_x] = "O"
                box_map[pos[0]][pos[1] + instruction[1]] = "@"
            else:
                box_map[new_pos_y][pos[1]] = "O"
                box_map[pos[0] + instruction[0]][pos[1]] = "@"

            box_map[pos[0]][pos[1]] = "."

            pos[0] += instruction[0]
            pos[1] += instruction[1]

    return get_gps_sum()

def can_push_box_vertically(i, j, dir):
    if box_map[i + dir][j] == "#" or box_map[i + dir][j + 1] == "#":
        return False
    elif box_map[i + dir][j] == "." and box_map[i + dir][j + 1] == ".":
        return True
    elif box_map[i + dir][j] == "[":
        return can_push_box_vertically(i + dir, j, dir)
    else:
        can_push = True
        
        if box_map[i + dir][j] == "]" and not can_push_box_vertically(i + dir, j - 1, dir):
            can_push = False
        if box_map[i + dir][j + 1] == "[" and not can_push_box_vertically(i + dir, j + 1, dir):
            can_push = False
        
        return can_push
    
def move_boxes_vertically(i, j, dir):
    if box_map[i + dir][j] != "." or box_map[i + dir][j + 1] != ".":
        if box_map[i + dir][j] == "]":
            move_boxes_vertically(i + dir, j - 1, dir)
        if box_map[i + dir][j] == "[":
            move_boxes_vertically(i + dir, j, dir)
        if box_map[i + dir][j + 1] == "[":
            move_boxes_vertically(i + dir, j + 1, dir)
        
    box_map[i + dir][j] = "["
    box_map[i + dir][j + 1] = "]"
    box_map[i][j] = "."
    box_map[i][j + 1] = "."

def get_new_gps_sum():
    total = 0

    for i, row in enumerate(box_map):
        for j, c in enumerate(row):
            if c == "[":
                total += 100 * i + j
    
    return total

def print_map():
    for row in box_map:
        result = ""
        for c in row:
            result += c
        print(result)
        
    print()

def puzzle2():
    pos = get_init_robot_pos()

    for instruction in instructions:
        new_pos_x = pos[1] + instruction[1]
        new_pos_y = pos[0] + instruction[0]

        can_move = True

        if box_map[new_pos_y][new_pos_x] == "#":
            can_move = False

        if instruction[1] != 0:
            while "[]".count(box_map[pos[0]][new_pos_x]) > 0:
                new_pos_x += instruction[1]
            if box_map[pos[0]][new_pos_x] == "#":
                can_move = False
        else:
            if box_map[new_pos_y][pos[1]] == "[" and not can_push_box_vertically(new_pos_y, pos[1], instruction[0]):
                can_move = False
            elif box_map[new_pos_y][pos[1]] == "]" and not can_push_box_vertically(new_pos_y, pos[1] - 1, instruction[0]):
                can_move = False

        if can_move:
            if instruction[1] != 0:
                while new_pos_x != pos[1]:
                    box_map[pos[0]][new_pos_x] = box_map[pos[0]][new_pos_x - instruction[1]]
                    new_pos_x -= instruction[1]
            else:
                if box_map[new_pos_y][pos[1]] == "[":
                    move_boxes_vertically(new_pos_y, pos[1], instruction[0])
                elif box_map[new_pos_y][pos[1]] == "]":
                    move_boxes_vertically(new_pos_y, pos[1] - 1, instruction[0])
                
                box_map[new_pos_y][pos[1]] = "@"

            box_map[pos[0]][pos[1]] = "."

            pos[0] += instruction[0]
            pos[1] += instruction[1]

    print_map()

    return get_new_gps_sum()

print(puzzle2())