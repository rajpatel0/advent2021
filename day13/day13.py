import numpy as np
with open('input.txt','r') as f:
    data = f.readlines()

dataClean = [val.rstrip() for val in data]

idxSplit = dataClean.index('')
dots = dataClean[:idxSplit]
folds = dataClean[idxSplit+1:]
dotCoords = [(int(val.split(',')[0]),int(val.split(',')[1])) for val in dots]
foldsCleaned = [val.split()[-1].split('=') for val in folds]
foldsCleanedInt = [[val[0],int(val[1])] for val in foldsCleaned]

dotCoords = set(dotCoords)
for i,fold in enumerate(foldsCleanedInt):
    newDots = set()
    dotsToRemove = set()
    if fold[0] == 'x':
        for dot in dotCoords:
            if dot[0] < fold[1]: # x coord is left of fold
                continue
            elif dot[0] == fold[1]:
                dotsToRemove.add(dot)
            else:
                newDot = (fold[1]-(dot[0]-fold[1]),dot[1])
                dotsToRemove.add(dot)
                newDots.add(newDot)
    if fold[0] == 'y':
        for dot in dotCoords:
            if dot[1] < fold[1]: #y cord is above fold
                continue
            elif dot[1] == fold[1]:
                dotsToRemove.add(dot)
            else:
                newDot = (dot[0],fold[1]-(dot[1]-fold[1]))
                dotsToRemove.add(dot)
                newDots.add(newDot)
    dotCoords = dotCoords-dotsToRemove
    dotCoords = dotCoords.union(newDots)
    print(f'Fold {i+1} has {len(dotCoords)} elements')

#part 2
maxX = max([val[0] for val in dotCoords])
maxY = max([val[1] for val in dotCoords])

print(maxX)
mat = [[" " for _ in range(maxY+1)] for _ in range(maxX+1)]
for x,y in dotCoords:
    mat[x][y] = '#'

np.set_printoptions(edgeitems=30,linewidth=1000)
print(np.transpose(np.array(mat)))

    
 
            





