with open('input.txt', 'r') as f:
    data = f.readlines()

dataClean = [val.rstrip() for val in data]
dataMat = [[int(digit) for digit in val] for val in dataClean]



#part2

cols = len(dataMat[0])
rows = len(dataMat)
costToIndex = dict()
costToEnter = dict()
costToIndex[(0,0)] = 0
for i in range(rows*5):
    for j in range(cols*5):
        if i ==0 and j==0:
            costToEnter[(i,j)] = 0
        else:
            costToEnter[(i,j)] =  (dataMat[i%rows][j%cols] + i//rows + j//cols -1)%9 + 1

for i in range(1,cols*5):
    costToIndex[(0,i)] = costToIndex[(0,(i-1))] + costToEnter[(0,i)]
for i in range(1,rows*5):
    costToIndex[(i,0)] = costToIndex[((i-1),0)] + costToEnter[(i,0)]




for i in range(1,rows*5):
    for j in range(1,cols*5):
        costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[i,j-1]) +costToEnter[(i,j)]

for _ in range(10): #treat it like a stability problem and wait til the answer stabilizes, the number should increase if you still see change
    for i in range(rows*5):
        for j in range(cols*5):
            if j==0:
                if i ==0:
                    continue
                elif i == rows*5-1:
                    costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[(i,j+1)]) + costToEnter[(i,j)]
                else:
                    costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[(i+1,j)],costToIndex[(i,j+1)]) + costToEnter[(i,j)]
        
            elif j==cols*5-1:
                if i == 0:
                    costToIndex[(i,j)] = min(costToIndex[(i+1,j)],costToIndex[(i,j-1)]) + costToEnter[(i,j)] #honestly kinda irrelevant
                elif i == rows*5-1:
                    costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[(i,j-1)]) + costToEnter[(i,j)]
                else:
                    costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[(i+1,j)],costToIndex[(i,j-1)]) + costToEnter[(i,j)]
            else:
                if i == 0:
                    costToIndex[(i,j)] = min(costToIndex[(i+1,j)],costToIndex[(i,j-1)],costToIndex[(i,j+1)]) + costToEnter[(i,j)] 
                elif i == rows*5-1:
                    costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[(i,j-1)],costToIndex[(i,j+1)]) + costToEnter[(i,j)] 
                else:
                    costToIndex[(i,j)] = min(costToIndex[(i-1,j)],costToIndex[(i+1,j)],costToIndex[(i,j-1)],costToIndex[(i,j+1)]) + costToEnter[(i,j)]

    print(costToIndex[(rows*5-1,cols*5-1)])