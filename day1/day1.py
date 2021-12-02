with open('input.txt', 'r') as f:
    data = f.readlines()

dataInt = [int(val) for val in data]


def part1(listOfInts):
    count = 0 
    listLen = len(listOfInts)
    i = 0
    while i< listLen-1:
        if listOfInts[i] < listOfInts[i+1]:
            count+=1
        i+=1
    print("part 1 count", count)

def part2(listOfInts):
    count = 0 
    listLen = len(listOfInts)
    i = 0
    while i< listLen-3:
        if listOfInts[i] < listOfInts[i+3]:
            count+=1
        i+=1
    print("part 2 count", count)


part1(dataInt)
part2(dataInt)
