import statistics
with open("input.txt","r") as f:
    data = f.readlines()

dataStrip  = [val.rstrip() for val in data]



#part1

scoreDict = {')': 3, ']':57,'}':1197, '>':25137}
mapping = {')':'(', ']':'[','}':'{','>':'<'}
reverseMapping = {'(':')','[':']','{':'}','<':'>'}

score = 0
linesToComplete = []
for line in dataStrip:
    lineToBeCompleted = True
    stack = []
    for char in line:
        if char in scoreDict.keys():
            if mapping[char] != stack[-1]:
                score+=scoreDict[char]
                lineToBeCompleted = False
                break
            stack.pop()
        else:
            stack.append(char)
    if lineToBeCompleted:
        linesToComplete.append(line)

print(score) 
#part 2 
autoScore = {')': 1, ']':2,'}':3,'>':4}

lineScores = []
for line in linesToComplete:
    score = 0
    stack = []
    for char in line:
        if char in scoreDict.keys():
            stack.pop()
        else:
            stack.append(char)
    stack.reverse()
    for char in stack:
        score = score*5 + autoScore[reverseMapping[char]]
    lineScores.append(score)

print(statistics.median(lineScores))


            
            