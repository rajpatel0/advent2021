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
versionList = []

    
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
 

def operatorPacket(binData,curIndex,typeVal):
    i = curIndex
    if typeVal == '1':
        numSubpackets = int(binData[i:i+lenType1Bit],2)
        i+=lenType1Bit
        while numSubpackets>0:
            version,typePk,i = getHeader(binData,i)
            versionList.append(version)
            if typePk == 4:
                literalStart = i
                literal,i=literalPacket(binData,i)
                numSubpackets-=1
            else:
                lenType = binData[i] 
                i+=1
                i = operatorPacket(binData,i,lenType)
                numSubpackets-=1
        return i
    else:
        lengthBits = int(binData[i:i+lenType0Bit],2)
        i+=lenType0Bit
        startingI = i
        while i<startingI+lengthBits:
            version,typePk,i = getHeader(binData,i)
            versionList.append(version)
            if typePk == 4:
                literal,i=literalPacket(binData,i)
            else:
                lenType = binData[i] 
                i+=1
                i = operatorPacket(binData,i,lenType)
        return i











 
startI = i
version,typePk,i = getHeader(binData,i)
versionList.append(version)
if typePk == 4: #literal
    literal,i = literalPacket(binData,i)
else:
    lenghtType = binData[i]
    i+=1
    i = operatorPacket(binData,i,lenghtType)

print(f'Part 1 answer = {sum(versionList)}')

        

