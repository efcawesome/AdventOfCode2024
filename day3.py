with open("day3input.txt") as f:
    input = ""

    for x in f.readlines():
        input += x

print(input)

def puzzle1():
    sum = 0

    for i in range(len(input)):
        word = input[i:i + 4]

        if word == "mul(":
            num1 = ""
            ind = 0
            for j, c in enumerate(input[i + 4:]):
                try:
                    "0123456789".index(c)
                    num1 += c
                except:
                    ind = i + 5 + j
                    break


            num2 = ""
            for d in input[ind:]:
                try:
                    "0123456789".index(d)
                    num2 += d
                except:
                    if d == ")":
                        sum += int(num1) * int(num2)

                    break

            print(num1)
            print(num2)

    return sum

def puzzle2():
    sum = 0

    enabled = True

    for i in range(len(input)):
        do_word = input[i:i + 4]
        dont_word = input[i:i + 7]
        mul_word = input[i:i + 4]

        if do_word == "do()":
            enabled = True

        if dont_word == "don't()":
            enabled = False

        if enabled and mul_word == "mul(":
            num1 = ""
            ind = 0
            for j, c in enumerate(input[i + 4:]):
                try:
                    "0123456789".index(c)
                    num1 += c
                except:
                    ind = i + 5 + j
                    break


            num2 = ""
            for d in input[ind:]:
                try:
                    "0123456789".index(d)
                    num2 += d
                except:
                    if d == ")":
                        sum += int(num1) * int(num2)

                    break

            print(num1)
            print(num2)

    return sum


print(puzzle2())