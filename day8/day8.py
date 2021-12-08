with open('input.txt','r') as f:
    data = f.readlines()


dataStr = [val.rstrip() for val in data]

#part1

dataImportant = [val.split('|')[1] for val in dataStr]

dataImportantSplit = [val.split() for val in dataImportant]

count = 0
for val in dataImportantSplit:
    for string in val:
        if len(string) in [2,3,4,7]:
            count+=1

print(count)

#part2
dataStrings = [val.split('|')[0] for val in dataStr]
dataStringsSplit = [val.split() for val in dataStrings]

def makeMappingAndReturnNumber(strings, ImportantNumbers):
    numSets = dict()
    stringsSet = dict()
    for val in strings:
        valLen = len(val)
        if valLen == 2:
            numSets[1] = set(val)
            stringsSet[''.join(sorted(val))] = 1
        elif valLen == 3:
            numSets[7] = set(val)
            stringsSet[''.join(sorted(val))] = 7
        elif valLen == 4:
            numSets[4] = set(val)
            stringsSet[''.join(sorted(val))] = 4
        elif valLen == 7:
            numSets[8] = set(val)
            stringsSet[''.join(sorted(val))] = 8
    

        
    for val in strings:
        if set(val) in numSets.values():
            continue
        else:
            valLen = len(val)
            if valLen == 6:
                if len(numSets[1].difference(val)) == 1: #aka doesn't fully have 1, missing one segment implies 6
                    numSets[6] = set(val)
                    stringsSet[''.join(sorted(val))] = 6
                else:
                    if len(numSets[4].difference(val)) ==1:
                        numSets[0] = set(val)
                        stringsSet[''.join(sorted(val))] = 0
                    else:
                        numSets[9] = set(val) 
                        stringsSet[''.join(sorted(val))] = 9

            if valLen == 5:
                if len(set(val).difference(numSets[4].difference(numSets[1]))) == 3: #if this length is true, can only be 5 as only 5 fully captures top left segment
                    numSets[5] = set(val)
                    stringsSet[''.join(sorted(val))] = 5
                else:
                    if len(numSets[1].difference(val)) == 1: # 2 doesn't have the full segment of 1 so its should be missing 1
                        numSets[2] = set(val)
                        stringsSet[''.join(sorted(val))] = 2
                    else:
                        numSets[3] = set(val)
                        stringsSet[''.join(sorted(val))] = 3
    string = ''
    for val in ImportantNumbers:
        string += str(stringsSet[''.join(sorted(val))])

    return int(string)

part2Sum = sum([makeMappingAndReturnNumber(inputString,calcString) for inputString,calcString in zip(dataStringsSplit,dataImportantSplit)])

print(part2Sum)





