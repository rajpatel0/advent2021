
with open('input.txt','r') as f:
    data = f.readlines()
data = [val.rstrip() for val in data]
inputData = []
for val in data:
    start,end = val.split('->')
    startX,startY = start.split(',')
    endX,endY = end.split(',')
    startX,startY,endX,endY = int(startX),int(startY),int(endX),int(endY)
    inputData.append((startX,startY,endX,endY))


dictTable = {}

for coords in inputData:
    startX,startY,endX,endY = coords
    if startX != endX and startY != endY:
        if startX < endX and startY < endY:
            for i,j in zip(range(startX,endX+1),range(startY,endY+1)):
                if (i,j) in dictTable:
                    dictTable[(i,j)] += 1
                else:
                    dictTable[(i,j)] = 1
        elif startX > endX and startY<endY:
            for i,j in zip(range(startX,endX-1,-1),range(startY,endY+1)):
                if (i,j) in dictTable:
                    dictTable[(i,j)] += 1
                else:
                    dictTable[(i,j)] = 1
        elif startX < endX and startY> endY:
            for i,j in zip(range(startX,endX+1),range(startY,endY-1,-1)):
                if (i,j) in dictTable:
                    dictTable[(i,j)] += 1
                else:
                    dictTable[(i,j)] = 1
        else:
            for i,j in zip(range(startX,endX-1,-1),range(startY,endY-1,-1)):
                if (i,j) in dictTable:
                    dictTable[(i,j)] += 1
                else:
                    dictTable[(i,j)] = 1
    elif startX == endX:
        if startY>endY:
            for i in range(endY,startY+1):
                if (startX,i) in dictTable:
                    dictTable[(startX,i)] += 1
                else:
                    dictTable[(startX,i)] = 1
        else:
            for i in range(startY,endY+1):
                if (startX,i) in dictTable:
                    dictTable[(startX,i)] += 1
                else:
                    dictTable[(startX,i)] = 1

    else:
        if startX>endX:
            for i in range(endX,startX+1):
                if (i,startY) in dictTable:
                    dictTable[(i,startY)] += 1
                else:
                    dictTable[(i,startY)] = 1
        else:
            for i in range(startX,endX+1):
                if (i,startY) in dictTable:
                    dictTable[(i,startY)] += 1
                else:
                    dictTable[(i,startY)] = 1
 


    
count = 0
for key,val in dictTable.items():
    if val >= 2:
        count += 1
    

print(count)