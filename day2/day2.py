import os

def problem1(input):
    x = 0
    y = 0

    for line in input:
        if line[0] is 'f':
            x+=int(line[-1])
        elif line[0] is 'u':
            y-=int(line[-1])
        else:
            y+=int(line[-1])

    return x*y

def problem2(input):
    x = 0
    y = 0
    aim = 0

    for line in input:
        if line[0] is 'f':
            x+=int(line[-1])
            y+=int(line[-1])*aim
        elif line[0] is 'u':
            aim-=int(line[-1])
        else:
            aim+=int(line[-1])

    return x*y


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "day2.txt")) as file:
        input = [x for x in file.read().splitlines()]

    print(problem1(input))
    print(problem2(input))