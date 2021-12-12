import sys

sys.setrecursionlimit(2000)

with open('input.txt','r') as f:
    data = f.readlines()

dataInt = [val.rstrip() for val in data]
dataIntList = [list(map(int,val)) for val in dataInt] 


#pt1

sumLowPoints = 0
lenSublist = len(dataIntList[0])
lenList = len(dataIntList)
lowPoints = []
for i,largeList in enumerate(dataIntList):
    for j,elem in enumerate(largeList):
        if i==0:
            if j==0:
                if elem< dataIntList[i+1][j] and elem<dataIntList[i][j+1]:
                    sumLowPoints+=elem+1
                    lowPoints.append((i,j))
            elif j==lenSublist-1:
                if elem<dataIntList[i+1][j] and elem<dataIntList[i][j-1]:
                    sumLowPoints+=elem+1
                    lowPoints.append((i,j))
            else:
                if elem<dataIntList[i+1][j] and elem<dataIntList[i][j-1] and elem<dataIntList[i][j+1]:
                    sumLowPoints+=elem+1
                    lowPoints.append((i,j))
        elif i == lenList-1:
            if j==0:
                if elem< dataIntList[i-1][j] and elem<dataIntList[i][j+1]:
                    sumLowPoints+=elem+1
                    lowPoints.append((i,j))
            elif j==lenSublist-1:
                if elem<dataIntList[i-1][j] and elem<dataIntList[i][j-1]:
                    sumLowPoints+=elem+1
                    lowPoints.append((i,j))
            else:
                if elem<dataIntList[i-1][j] and elem<dataIntList[i][j-1] and elem<dataIntList[i][j+1]:
                    sumLowPoints+=elem+1
                    lowPoints.append((i,j))
        else:
            if j==0:
                if elem< dataIntList[i+1][j] and elem<dataIntList[i][j+1] and elem<dataIntList[i-1][j]:
                    sumLowPoints+= elem+1
                    lowPoints.append((i,j))
            elif j==lenSublist-1:
                if elem< dataIntList[i+1][j] and elem<dataIntList[i][j-1] and elem<dataIntList[i-1][j]:
                    sumLowPoints+= elem+1
                    lowPoints.append((i,j))
            else:
                if elem< dataIntList[i+1][j] and elem<dataIntList[i][j-1] and elem<dataIntList[i-1][j] and elem<dataIntList[i][j+1]:
                    sumLowPoints+= elem+1
                    lowPoints.append((i,j))
print("Low Points", sumLowPoints)



#part 2

visited = []
basinList = []


def getBasinSize(row,column):
    if column<0 or column>lenSublist-1 or row>lenList-1 or row<0 or dataIntList[row][column]==9 or (row,column) in visited:
        return 0
    else:
        visited.append((row,column))
        return 1+getBasinSize(row+1,column) + getBasinSize(row,column+1) + getBasinSize(row-1,column) + getBasinSize(row,column-1)
for row,column in lowPoints:
    basinSize = getBasinSize(row,column)
    visited = []
    basinList.append(basinSize)

basinList=sorted(basinList)

greatestBasins = basinList[-3:]

print(greatestBasins[0]*greatestBasins[1]*greatestBasins[2])
    
