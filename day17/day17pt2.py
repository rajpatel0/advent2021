with open('input.txt','r') as f:
    data = f.readline().rstrip()

targets = data.split(':')[1]

xTar,yTar = targets.split(',')


xStart,xEnd = xTar.split('=')[1].split('..')
yStart,yEnd = yTar.split('=')[1].split('..')

validX = range(int(xStart),int(xEnd)+1)
validY = range(int(yStart),int(yEnd)+1)



validShot = set()
for initialVelocityY in range(validY[0],500): #arbitraily large range, needs at least lowest possible y
    for initialVelocityX in range(0,validX[-1]+1): #x has to be at least 17 tbh from part 1 but might as well include lower ranges
        yVel = initialVelocityY
        xVel = initialVelocityX
        xPos= 0
        yPos= 0 
        while True:
            if xPos>validX[-1] or yPos<validY[0]:
                break
            if xPos in validX and yPos in validY:
                validShot.add((initialVelocityX,initialVelocityY))
                break
            else:
                xPos+= xVel
                yPos+= yVel
                if xVel >0:
                    xVel-=1
                elif xVel < 0:
                    xVel+=1
                yVel -= 1

print(len(validShot))