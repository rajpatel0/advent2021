with open('input.txt','r') as f:
    data = f.readlines()

initialState = [int(val) for val in data[0].split(',')]
countOfFishByDays = [0 for i in range(0,9)]
for i in range(0,9):
    countOfFishByDays[i] = initialState.count(i)

numDays = 256 #change this for part 1 or part2
for _ in range(numDays):
    newFish = countOfFishByDays[0]
    for i in range(len(countOfFishByDays)-1):
        countOfFishByDays[i] =countOfFishByDays[i+1]
    countOfFishByDays[-1] = newFish
    countOfFishByDays[6] += newFish #fish start cycle again
print(sum(countOfFishByDays))

