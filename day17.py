registers = {
    "a": 6596076101,
    "b": 0,
    "c": 0
    }

program = [2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0]

def get_combo(num):
    if num <= 3:
        return num
    else:
        match num:
            case 4:
                return registers["a"]
            case 5:
                return registers["b"]
            case 6:
                return registers["c"]

def puzzle1():
    instruction_pointer = 0

    while instruction_pointer < len(program):
        has_jumped = False

        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        match opcode:
            case 0: #adv
                registers["a"] = int(registers["a"] / pow(2, get_combo(operand)))
            case 1: #bxl
                registers["b"] = registers["b"] ^ operand
            case 2: #bst
                registers["b"] = get_combo(operand) % 8
            case 3: #jnz
                if registers["a"] != 0:
                    instruction_pointer = operand
                    has_jumped = True
            case 4: #bxc
                registers["b"] = registers["b"] ^ registers["c"]
            case 5: #out
                print(str(get_combo(operand) % 8) + ",", end="")
            case 6: #bdv
                registers["b"] = int(registers["a"] / pow(2, get_combo(operand)))
            case 7: #cdv
                registers["c"] = int(registers["a"] / pow(2, get_combo(operand)))
        
        if not has_jumped:
            instruction_pointer += 2

def get_output(a):
    """
    b = a % 8
    b = (a % 8) ^ 3
    c = a >> ((a % 8) ^ 3)
    b = ((a % 8) ^ 3) ^ 5
    b = (((a % 8) ^ 3) ^ 5) ^ (a >> ((a % 8) ^ 3))
    return

    a = a >> 3
    """

    temp = (a % 8) ^ 3
    return ((temp ^ 5) ^ (a >> temp)) % 8

def puzzle2():
    a_vals = {0}


    for prog in reversed(program):
        new_a_vals = set()

        for val in a_vals:
            for a in range(0, 8):
                new_num = val * 8 + a

                if get_output(new_num) == prog:
                    new_a_vals.add(new_num)
        
        a_vals = new_a_vals
    
    temp = min(a_vals)
    while temp > 0:
        print(str(get_output(temp)) + ",", end = "")
        temp = temp >> 3

    print()

    return min(a_vals)

print(puzzle2())
