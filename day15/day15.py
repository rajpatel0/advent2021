with open('input.txt', 'r') as f:
    data = f.readlines()

dataClean = [val.rstrip() for val in data]
dataMat = [[int(digit) for digit in val] for val in dataClean]


#part1

costToIndex = dict()
costToIndex[(0,0)] = 0

for i in range(1,len(dataMat[0])):
    costToIndex[(0,i)] = costToIndex[(0,i-1)] + dataMat[0][i]
for i in range(1,len(dataMat)):
    costToIndex[(i,0)] = costToIndex[(i-1,0)] + dataMat[i][0]

for i in range(1,len(dataMat)):
    for j in range(1,len(dataMat[0])):
        costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[i,j-1]) + dataMat[i][j]

print(costToIndex[(len(dataMat)-1,len(dataMat[0])-1)])