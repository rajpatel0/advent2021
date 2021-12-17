with open('input.txt','r') as f:
    data = f.readline().rstrip()
#binData = bin(int(data,2))[2:].zfill(len(data))
binData = bin(int(data, 16))[2:].zfill(len(data) * 4)
lenBinData = len(binData)
headerLen = 6
lenType0Bit = 15
lenType1Bit = 11
groupLen = 5

i = 0

    
def literalPacket(binData,curIndex):
    i = curIndex
    curBinString = ''
    while binData[i] == '1':
        curBinString += binData[i+1:i+groupLen]
        i += groupLen
    curBinString+=binData[i+1:i+groupLen] #the 0 group
    i += groupLen
    literal = int(curBinString,2)
    return literal,i

def getHeader(binData,curIndex):
    i = curIndex
    version = int(binData[i:i+3],2)
    typePk = int(binData[i+3:i+headerLen],2)
    i+=headerLen
    return version,typePk,i
 

def operatorPacket(binData,curIndex,op,listType,literalList):
    print(op)
    i = curIndex
    numpacks = 0
    if listType == '1':
        numSubpackets = int(binData[i:i+lenType1Bit],2)
        i+=lenType1Bit
        while numSubpackets>0:
            version,typePk,i = getHeader(binData,i)
            numpacks+=1
            if typePk == 4:
                literal,i=literalPacket(binData,i)
                literalList.append(literal)
                numSubpackets-=1
            else:
                lenType = binData[i] 
                i+=1
                i,literalList = operatorPacket(binData,i,typePk,lenType,literalList)
                numSubpackets-=1
    else:
        lengthBits = int(binData[i:i+lenType0Bit],2)
        i+=lenType0Bit
        startingI = i
        while i<startingI+lengthBits:
            version,typePk,i = getHeader(binData,i)
            numpacks+=1
            if typePk == 4:
                literal,i=literalPacket(binData,i)
                literalList.append(literal)
            else:
                lenType = binData[i] 
                i+=1
                i,literalList = operatorPacket(binData,i,typePk,lenType,literalList)
    print(op,literalList,numpacks)
    print()
    if op == 0:
        sumval = sum(literalList[-numpacks:])
        otherElems = literalList[:-numpacks]
        otherElems.append(sumval)
        return i,otherElems
    elif op == 1:
        val = 1
        for num in literalList[-numpacks:]:
            val *= num
        otherElems = literalList[:-numpacks]
        otherElems.append(val)
        return i,otherElems
    elif op == 2:
        minVal = min(literalList[-numpacks:])
        otherElems = literalList[:-numpacks]
        otherElems.append(minVal)
 
        return i, otherElems

    elif op == 3:
        maxVal = max(literalList[-numpacks:])
        otherElems = literalList[:-numpacks]
        otherElems.append(maxVal)
 
        return i, otherElems
    elif op ==4:
        return i, literalList
    elif op == 5:
        otherElems = literalList[:-numpacks]
        if literalList[-2]>literalList[-1]:
            otherElems.append(1)
            return i,otherElems
        else:
            otherElems.append(0)
            return i, otherElems
    elif op == 6:
        otherElems = literalList[:-numpacks]
        if literalList[-2]<literalList[-1]:
            otherElems.append(1)
            return i,otherElems
        else:
            otherElems.append(0)
            return i, otherElems

    else:
        otherElems = literalList[:-numpacks]
        if literalList[-2]==literalList[-1]:
            otherElems.append(1)
            return i,otherElems
        else:
            otherElems.append(0)
            return i, otherElems















 
version,typePk,i = getHeader(binData,i)
if typePk == 4: #literal
    literal,i = literalPacket(binData,i)
else:
    lengthType = binData[i]
    i+=1
    i,outList = operatorPacket(binData,i,typePk,lengthType,[])

if typePk == 4:
    print(f'Part 2 answer = {literal}')
else:
    print(f'Part 2 answer = {outList[0]}')