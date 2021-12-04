class BingoCard:
    def __init__(self,listOfRows):
        self.row1 = [int(val) for val in listOfRows[0].split()]
        self.row2 = [int(val) for val in listOfRows[1].split()]
        self.row3 = [int(val) for val in listOfRows[2].split()]
        self.row4 = [int(val) for val in listOfRows[3].split()]
        self.row5 = [int(val) for val in listOfRows[4].split()]
        self.row1Sel = []
        self.row2Sel = []
        self.row3Sel = []
        self.row4Sel = []
        self.row5Sel = []
    def draw(self,binNum):
        if binNum in self.row1:
            self.row1Sel.append(self.row1.index(binNum))
        if binNum in self.row2:
            self.row2Sel.append(self.row2.index(binNum))
        if binNum in self.row3:
            self.row3Sel.append(self.row3.index(binNum))
        if binNum in self.row4:
            self.row4Sel.append(self.row4.index(binNum))
        if binNum in self.row5:
            self.row5Sel.append(self.row5.index(binNum))
            
    def printState(self):
        print(self.row1)
        print(self.row2)
        print(self.row3)
        print(self.row4)
        print(self.row5)

    def printStateChosen(self):
        print(self.row1Sel)
        print(self.row2Sel)
        print(self.row3Sel)
        print(self.row4Sel)
        print(self.row5Sel)



    def checkBingo(self):
        if len(self.row1Sel) == 5 or len(self.row2Sel) == 5 or len(self.row3Sel) == 5 or len(self.row4Sel) == 5 or len(self.row5Sel) == 5:
            return True
        elif set(self.row1Sel).intersection(set(self.row2Sel)).intersection(set(self.row3Sel)).intersection(set(self.row4Sel)).intersection(set(self.row5Sel)) != set():
            return True
        else:
            return False
    def getUnmarkedSum(self):
        runningSum = 0
        runningSum += sum([num for i,num in enumerate(self.row1) if i not in self.row1Sel])    
        runningSum += sum([num for i,num in enumerate(self.row2) if i not in self.row2Sel])    
        runningSum += sum([num for i,num in enumerate(self.row3) if i not in self.row3Sel])    
        runningSum += sum([num for i,num in enumerate(self.row4) if i not in self.row4Sel])    
        runningSum += sum([num for i,num in enumerate(self.row5) if i not in self.row5Sel])    
        return runningSum



with open('input.txt', 'r') as f:
    data = f.readlines()

dataNlineStrip = [val.rstrip() for val in data]
dataCleaned = [val for val in dataNlineStrip if val != '']
bingoNums = dataCleaned[0]
listOfLists = [dataCleaned[i:i+5] for i in range(1,len(dataCleaned),5)]

bingoCards = [BingoCard(listOfNums) for listOfNums in listOfLists]


def part1(bingoCards,bingoNums):
    for number in bingoNums.split(','):
        intNum = int(number)
        for card in bingoCards:
            card.draw(intNum)
            checkBingo = card.checkBingo()
            if checkBingo:
                return card.getUnmarkedSum() *intNum
    return False
def part2(bingoCards, bingoNums):
    winningCards = []
    for number in bingoNums.split(','):
        intNum = int(number)

        for card in bingoCards:
            if card in winningCards:
                continue
            card.draw(intNum)
            checkBingo = card.checkBingo()
            if checkBingo:
                winningCards.append(card)
                if len(winningCards) == len(bingoCards):
                    card.printState()
                    print(intNum)
                    return card.getUnmarkedSum()*intNum

    
    
 

print(part2(bingoCards,bingoNums))


