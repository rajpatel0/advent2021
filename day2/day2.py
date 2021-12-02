with open('input.txt', 'r') as f:
    data = f.readlines()


inputData = [(val.split()[0], int(val.split()[1]))  for val in data]


def part1(dataIn):
    depth = 0
    distance = 0
    for item in dataIn:
        if item[0] == 'forward':
            distance += item[1]
        elif item[0] == 'up':
            depth -= item[1]
        else:
            depth += item[1]
    print("part1 answer", depth*distance)

def part2(dataIn):
    depth = 0
    distance = 0
    aim = 0
    for item in dataIn:
        if item[0] == 'forward':
            distance += item[1]
            depth += aim*item[1]
        elif item[0] == 'up':
            aim -= item[1]
        else:
            aim += item[1]
    print("part 2 answer",depth*distance)

part1(inputData)
part2(inputData)