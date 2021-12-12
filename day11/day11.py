import enum
import numpy as np
with open('input.txt', 'r') as f:
    data = f.readlines()

dataClean = [val.rstrip() for val in data]

dataMat = [list(map(int,val)) for val in dataClean]


#part 1 (for part 2 change numsteps from 100 to some large number ~800) 

numSteps = 600
numFlashes = 0


for iteration in range(numSteps):
    flashes = []
    flashed = set()
    for i,rowList in enumerate(dataMat):
        for j,elem in enumerate(rowList):
            dataMat[i][j]+=1

            if dataMat[i][j]>9 and (i,j) not in flashes:
                flashes.append((i,j))
    
    aroundTheWorld = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
    while len(flashes) > 0:
        row,column = flashes.pop()
        if (row,column) not in flashed:
            for rowWorld,columnWorld in aroundTheWorld:
                newRow = row+rowWorld
                newCol = column+columnWorld
                if newRow<0 or newRow>9 or newCol>9 or newCol<0:
                    continue
                else:
                    dataMat[newRow][newCol] +=1
                    if dataMat[newRow][newCol] > 9 and (newRow,newCol) not in flashes:
                        flashes.append((newRow,newCol))
            flashed.add((row,column))
    
    if len(flashed) == 100:
        print(iteration+1)
    for row,column in flashed:
        numFlashes+=1
        dataMat[row][column] = 0
        
    
print(numFlashes)


