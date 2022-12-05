import os

def problem1(input):
    var_length = len(input[0])
    gamma = ''
    epsilon = ''
    for pos in range(var_length):
        mcb = '0' if sum(int(line[pos]) for line in input) < len(input) / 2 else '1'
        gamma += mcb
        epsilon += '0' if mcb == '1' else '1'
    return int(gamma, 2) * int(epsilon, 2)

def problem2(input):
    var_length = len(input[0])
    oxygen = input
    c02 = input

    for pos in range(var_length):
        mcb = 0 if sum(int(line[pos]) for line in oxygen) < len(oxygen) / 2 else 1
        oxygen = [num for num in oxygen if int(num[pos]) is mcb]
        if len(oxygen) == 1:
            break
    
    for pos in range(var_length):
        lcb = 1 if sum(int(num[pos]) for num in c02) < len(c02) / 2 else 0
        c02 = [num for num in c02 if int(num[pos]) is lcb]
        if len(c02) == 1:
            break
    
    return int(c02[0], 2) * int(oxygen[0], 2)

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "day3.txt")) as file:
        input = file.read().splitlines()
        print(problem1(input))
        print(problem2(input))