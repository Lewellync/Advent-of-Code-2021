import os

def problem1(input):
    x = 0
    for i in range(1, len(input)):
        if input[i-1] < input[i]:
            x += 1
    return x

def problem2(input):
    new_input = [input[i-2] + input[i-1] + input[i] for i in range(2, len(input))]
    return problem1(new_input)

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "day1.txt")) as file:
        input = [int(i) for i in file.read().splitlines()]

    print(problem1(input))
    print(problem2(input))