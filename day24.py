with open("day24input.txt") as f:
    wire_vals = {}

    gates = []

    gate_dict = {}

    add_default_val = True

    for line in f.readlines():
        line = line.strip()
        if line == "":
            add_default_val = False
        elif add_default_val:
            split_line = line.split(": ")
            wire_vals[split_line[0]] = bool(int(split_line[1]))
        else:
            split_line = line.split(" ")
            arg1 = split_line[0]
            arg2 = split_line[2]
            gate_type = split_line[1]
            output_wire = split_line[4]

            gates.append((arg1, arg2, gate_type, output_wire))
            gate_dict[output_wire] = (arg1, arg2, gate_type)

def get_output(arg1, arg2, gate_type):
    match gate_type:
        case "AND":
            return arg1 and arg2
        case "OR":
            return arg1 or arg2
        case "XOR":
            return arg1 != arg2

def puzzle1():
    while len(gates) > 0:
        for gate in gates:
            arg1, arg2, gate_type, output_wire = gate

            if arg1 in wire_vals and arg2 in wire_vals:
                wire_vals[output_wire] = get_output(wire_vals[arg1], wire_vals[arg2], gate_type)

                gates.remove(gate)

    z_dict = {k:v for k, v in wire_vals.items() if k[0] == "z"}
    
    result = 0

    for wire in sorted(z_dict, reverse=True):
        result = result * 2 + int(z_dict[wire])

    return result

def get_adder(z_wire):
    wire1, wire2, g_type = gate_dict[z_wire]

    sum_xor_op = f"{wire1} {g_type} {wire2} -> {z_wire}"

    print(f"sum_xor = {sum_xor_op}") # should be XOR

    cin = ""
    a = ""
    b = ""
    a_b_t = ""

    is_wire1 = True

    if gate_dict[wire1][0] in wire_vals: # first is A XOR B
        a, b, a_b_t = gate_dict[wire1]
        cin = wire2
    else: # second is A XOR B
        is_wire1 = False
        a, b, a_b_t = gate_dict[wire2]
        cin = wire1

    a_xor_b = f"{a} {a_b_t} {b} -> {wire1 if is_wire1 else wire2}"

    print(f"a_xor_b = {a_xor_b}")
    print(f"cin = {cin}")

    a_and_b_out = ""

    a_xor_b_and_cin = ""
    a_x_b_c_out = ""

    for output, v in gate_dict.items():
        if ((is_wire1 and wire1 in v) or (not is_wire1 and wire2 in v)) and output != z_wire:
            a_xor_b_and_cin = f"{v[0]} {v[2]} {v[1]} -> {output}"
            a_x_b_c_out = output
        if a in v and b in v:
            result = f"{v[0]} {v[2]} {v[1]} -> {output}"

            if result != a_xor_b:
                a_and_b_out = result
                print(f"a_and_b = {a_and_b_out}")

    print(f"a_xor_b_and_cin = {a_xor_b_and_cin}")

    cout_gate = ""

    for output, v in gate_dict.items():
        if a_x_b_c_out in v:
            cout_gate = f"{v[0]} {v[2]} {v[1]} -> {output}"

    print(f"cout_gate = {cout_gate}")
    print()

def puzzle2_real():
    for z in gate_dict:
        if z[0] == "z" and z != "z00" and z != "z30":
                get_adder(z)

    r = sorted(["mwp", "btb", "z23", "rmj", "z17", "cmv", "z30", "rdg"])

    result = ""
    for c in r:
        result += c + ","

    return result[:-1]

print(puzzle2_real())

