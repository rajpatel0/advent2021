import statistics
import math
with open('input.txt','r') as f:
    data = f.readlines()

dataInt = [int(val) for val in data[0].split(',')]

minCost = float('inf')
for val in range(min(dataInt),max(dataInt)):
    gasCost = sum([abs(val-i) for i in dataInt])
    minCost = min(gasCost,minCost)
print(minCost)

#day2

minCost = float('inf')
for val in range(min(dataInt),max(dataInt)):
    gasCost = sum([(abs(val-i)*(abs(val-i)+1))/2 for i in dataInt])
    minCost = min(gasCost,minCost)
print(minCost)


#simplier solution to part 2
valToSub = math.floor(statistics.fmean(dataInt))
print(sum([(abs(val-valToSub)*(abs(val-valToSub)+1))/2 for val in dataInt]))