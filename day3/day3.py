from statistics import mode
with open('input.txt','r') as f:
    data = f.readlines()

dataVal = [val.rstrip() for val in data]


def part1(dataVal):
    dataValLen = len(dataVal)
    gamma = ''
    epsilon = ''

    for i in range(len(dataVal[0])):
        count = [1 for val in dataVal if val[i] == '1']
        if sum(count) > dataValLen//2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma,2)*int(epsilon,2)

def getMostCommonBit(listOfBits):
    if listOfBits.count('0') == listOfBits.count('1'):
        return '1'
    else:
        return mode(listOfBits)

def getListOfBits(listOfBins, idx):
    return [val[idx] for val in listOfBins]

def getImportantIdx(listOfBins, listOfIdx):
    return [listOfBins[idx] for idx in listOfIdx]
def updateList(listIdx, listOfBins, commonBit, idx):
    if len(listIdx) == 1:
        return listIdx
    listOfBits = [val[idx] for val in listOfBins]
    newIdx = [idxs for idxs in listIdx if listOfBits[idxs] == commonBit]
    return newIdx

def part2(dataVal):
    listOfOxyIdx = [i for i in range(len(dataVal))]
    listOfCO2Idx = [i for i in range(len(dataVal))]
    for i in range(len(dataVal[0])):
        OxyBit = getMostCommonBit(getListOfBits(getImportantIdx(dataVal,listOfOxyIdx),i))
        CO2Bit = getMostCommonBit(getListOfBits(getImportantIdx(dataVal,listOfCO2Idx),i))
        print(OxyBit)
        if CO2Bit == '0':
            CO2Bit = '1'
        else:
            CO2Bit = '0'
        listOfOxyIdx=updateList(listOfOxyIdx,dataVal, OxyBit,i)
        listOfCO2Idx=updateList(listOfCO2Idx,dataVal, CO2Bit,i)
    print(int(dataVal[listOfOxyIdx[0]],2), int(dataVal[listOfCO2Idx[0]],2))
    return int(dataVal[listOfOxyIdx[0]],2) * int(dataVal[listOfCO2Idx[0]],2)

print(part2(dataVal))


