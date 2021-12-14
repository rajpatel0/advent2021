from collections import Counter
with open('input.txt', 'r') as f:
    data = f.readlines()

dataStrip = [val.rstrip() for val in data]

idxSplit = dataStrip.index('')
polTemp = dataStrip[0]
ruleList = dataStrip[idxSplit+1:]


ruleDict = {}

for rule in ruleList:
    subString,outputString = rule.split(' -> ')
    ruleDict[subString] = outputString


numberOfIters = 10
polTempPart1 = polTemp
for _ in range(numberOfIters):
    i = 0
    lenPolStr = len(polTempPart1)
    updatedString = ''
    while i < lenPolStr-1:
        subString = polTempPart1[i:i+2]
        newChar = ruleDict[subString]
        updatedString = updatedString + subString[0]+newChar
        i+=1
    updatedString = updatedString+polTempPart1[-1]
    polTempPart1 = updatedString
    
counterString = Counter(polTempPart1)
listOfCommonElems = counterString.most_common()

print(f'Day 14 Part 1 Solution = {listOfCommonElems[0][1] - listOfCommonElems[-1][1]}')


numberOfIters = 40

polTempPart2= polTemp
ruleDictPairs = ruleDict.keys()
countPairs = dict()
for pair in ruleDictPairs:
    countPairs[pair] = 0

letterDict = dict()
currentChar = ord('A')
while currentChar<ord('Z')+1:
    letterDict[chr(currentChar)] = 0
    currentChar+=1

for i in range(len(polTempPart2)-1):
    subString = polTempPart2[i:i+2]
    countPairs[subString] +=1

for i in range(numberOfIters):
    for keyVal,value in countPairs.copy().items():
        newChar = ruleDict[keyVal]
        string1,string2 = keyVal[0]+newChar,newChar+keyVal[1]

        countPairs[string1] += value
        countPairs[string2] += value
        countPairs[keyVal] -= value
for key,val in countPairs.items():
    letterDict[key[0]] += val
letterDict[polTempPart2[-1]] += 1 #count the last char since its not considered
cleanedLetterDict = {key:val for key,val in letterDict.items() if val>0}
print(f'Day 14 part 2 solution = {max(cleanedLetterDict.values()) - min(cleanedLetterDict.values())}')



