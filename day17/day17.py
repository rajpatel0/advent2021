with open('input.txt','r') as f:
    data = f.readline().rstrip()

targets = data.split(':')[1]

xTar,yTar = targets.split(',')


xStart,xEnd = xTar.split('=')[1].split('..')
yStart,yEnd = yTar.split('=')[1].split('..')

validX = range(int(xStart),int(xEnd)+1)
validY = range(int(yStart),int(yEnd)+1)

validXRange = []

for xVal in range(30):
    xPos = 0 
    xVel = xVal
    while True:
        if xPos in validX:
            validXRange.append(xVal)
            break
        if xVel == 0:
            break
        xPos+= xVel
        if xVel >0:
            xVel-=1
        elif xVel < 0:
            xVel+=1
#the lowest xvelocity should be used becuase it ensures that we get to the point the rest can be focused on height  since X and Y are independent


xPos = 0
yPos = 0




highestYVel = 0
for initialVelocityY in range(0,1000): #arbitraily large range
    yVel = initialVelocityY
    xVel = validXRange[0]
    xPos= 0
    yPos= 0 
    while True:
        if xPos>validX[-1] or yPos<validY[0]:
            break
        if xPos in validX and yPos in validY:
            highestYVel = max(highestYVel,initialVelocityY)
            break
        else:
            xPos+= xVel
            yPos+= yVel
            if xVel >0:
                xVel-=1
            elif xVel < 0:
                xVel+=1
            yVel -= 1

maxY = sum(range(highestYVel+1))
print(maxY)