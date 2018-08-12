#Erin Cox
import random

class BinaryHeap:
    def __init__(self):
        #initialized with 0 to allow for division
        self.heapList= [0]
        self.size = 0
        
    def swapUp(self, listSize):
        #to move smaller numbers up in the tree
        while listSize // 2 > 0:
            if self.heapList[listSize] < self.heapList[listSize // 2]:
                self.heapList[listSize // 2], self.heapList[listSize] = self.heapList[listSize], self.heapList[listSize // 2]
            listSize = listSize // 2
            
    def insert(self, listItem):
        self.heapList.append(listItem)
        self.size += 1
        self.swapUp(self.size)
        
    def buildHeap(self, listInput):
        i = len(listInput) // 2
        self.size = len(listInput)
        self.heapList += listInput
        while i > 0:
            self.swapDown(i)
            i -= 1
        return self.heapList[1:]
            
    def swapDown(self, i):
        #to move larger numbers down in the tree
        while i * 2 <= self.size:
            minChild = self.minChild(i)
            if self.heapList[i] > self.heapList[minChild]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild
    
    def minChild(self, i):
        #i * 2 is the position of the left child/parent
        #i * 2 + 1 is the position of the right child/parent
        if i * 2 + 1 > self.size:
            return i * 2
        elif self.heapList[i * 2] < self.heapList[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1
        
    def getHeap(self):
        return self.heapList[1:]
        
    
def main():
    binaryHeap = BinaryHeap()
    randomNumList = []
    for i in range(5):
        randomNumList.append(random.randrange(1, 101))
    for i in range(len(randomNumList)):
        binaryHeap.insert(randomNumList[i])
    print('--Result from inserting integers one at a time--')
    print('Starting list: ', randomNumList)
    print('Ending list: ', binaryHeap.getHeap())
    
    binaryHeap2 = BinaryHeap()
    print()
    print()
    print('--Result from inserting the integer list all together--')
    print('Starting list: ', randomNumList)
    print('Ending list: ', binaryHeap2.buildHeap(randomNumList))

main()