import random
import time
import heapq


class EightPuzzle:
    def __init__(self):
        #self.values = [0,1,3,4,2,5,7,8,6]
        self.values = [8,1,3,4,0,2,7,6,5]
        self.previousValues = []
        self.currentPossibleMoves = []
        self.emptySquarePosition = -1
        self.fitness = -1
        self.manhattanDistance = 0
        self.priority = 0
        self.depth = 0

        self.updateState()

    def updateState(self):
        self.emptySquarePosition = self.values.index(0)
        self.getPossibleMoves()
        # DO this
        self.getCurrentStateFitness()
        self.getManhattan()
        self.getPriority()

    def generateRandomPuzzle(self):
        valuesList = list(range(9))
        random.shuffle(valuesList)
        self.values = valuesList
        print(self.values)

    def printCurrentPuzzle(self):
        print('_______________________________________________________________')
        print ('|' + str(self.values[0]) + '|' + str(self.values[1]) + '|' + str(self.values[2]) + '|')
        print ('|' + str(self.values[3]) + '|' + str(self.values[4]) + '|' + str(self.values[5]) + '|')
        print ('|' + str(self.values[6]) + '|' + str(self.values[7]) + '|' + str(self.values[8]) + '|')

    def getPossibleMoves(self):
        if self.emptySquarePosition == 0:
            self.currentPossibleMoves = ['right', 'down']
        elif self.emptySquarePosition == 1:
            self.currentPossibleMoves = ['left', 'right', 'down']
        elif self.emptySquarePosition == 2:
            self.currentPossibleMoves = ['left', 'down']
        elif self.emptySquarePosition == 3:
            self.currentPossibleMoves = ['right', 'up', 'down']
        elif self.emptySquarePosition == 4:
            self.currentPossibleMoves = ['left','right', 'up', 'down']
        elif self.emptySquarePosition == 5:
            self.currentPossibleMoves = ['left', 'up', 'down']
        elif self.emptySquarePosition == 6:
            self.currentPossibleMoves = ['right', 'up']
        elif self.emptySquarePosition == 7:
            self.currentPossibleMoves = ['left','right', 'up']
        elif self.emptySquarePosition == 8:
            self.currentPossibleMoves = ['left', 'up']

    def moveUp(self):
        if 'up' in self.currentPossibleMoves:
            self.previousValues = list(self.values)
            aux = self.values[self.emptySquarePosition - 3]
            self.values[self.emptySquarePosition - 3] = 0
            self.values[self.emptySquarePosition] = aux
            self.updateState()
            return True
        else:
            return False

    def moveDown(self):
        if 'down' in self.currentPossibleMoves:
            self.previousValues = list(self.values)
            aux = self.values[self.emptySquarePosition + 3]
            self.values[self.emptySquarePosition + 3] = 0
            self.values[self.emptySquarePosition] = aux
            self.updateState()
            return True
        else:
            return False

    def moveLeft(self):
        if 'left' in self.currentPossibleMoves:
            self.previousValues = list(self.values)
            aux = self.values[self.emptySquarePosition - 1]
            self.values[self.emptySquarePosition - 1] = 0
            self.values[self.emptySquarePosition] = aux
            self.updateState()
            return True
        else:
            return False

    def moveRight(self):
        if 'right' in self.currentPossibleMoves:
            self.previousValues = list(self.values)
            aux = self.values[self.emptySquarePosition + 1]
            self.values[self.emptySquarePosition + 1] = 0
            self.values[self.emptySquarePosition] = aux
            self.updateState()
            return True
        else:
            return False

    def move(self, selectedMove):
        if selectedMove == 'up':
            self.moveUp()
        elif selectedMove == 'down':
            self.moveDown()
        elif selectedMove == 'left':
            self.moveLeft()
        elif selectedMove == 'right':
            self.moveRight()

    def getCurrentStateFitness(self):
        fitness = 0
        if self.values[0] == 1:
            fitness += 1
        if self.values[1] == 2:
            fitness += 1
        if self.values[2] == 3:
            fitness += 1
        if self.values[3] == 4:
            fitness += 1
        if self.values[4] == 5:
            fitness += 1
        if self.values[5] == 6:
            fitness += 1
        if self.values[6] == 7:
            fitness += 1
        if self.values[7] == 8:
            fitness += 1
        if self.values[8] == 0:
            fitness += 1
        self.fitness = fitness

    def finished(self):
        if self.fitness == 9:
            return True
        else:
            self.depth += 1
            return False

    def restoreState(self):
        self.values = list(self.previousValues)
        self.updateState()

    def getManhattan(self):
        manhattanDistanceSum = 0
        x = 0
        row = []
        matrix = []

        #Create Matrix
        for i in range(0, 3):
            for j in range(0, 3):
                row.append(self.values[x])
                x += 1
            matrix.append(row)
            row = []

        #Compute manhattan
        for x in range(3):
            for y in range(3):
                v = matrix[x][y]
                if v != 0:
                    targetX = (v - 1) / 3
                    targetY = (v - 1) % 3
                    targetX = int(targetX)
                    dx = x - targetX
                    dy = y - targetY
                    manhattanDistanceSum += abs(dx) + abs(dy)
        self.manhattanDistance = manhattanDistanceSum

    def getPriority(self):
        self.priority = self.depth + self. manhattanDistance

    def setValues(self, newPriority, newValues):
        self.values = newValues
        self.updateState()
        self.priority = newPriority
        self.depth = self.priority - self.manhattanDistance

def aStar():
    startTime = time.time()
    puzzle = EightPuzzle()
    openList = []
    closeList = []
    index = 0

    while not puzzle.finished():
        if puzzle.moveUp():
            heapq.heappush(openList, (puzzle.priority, puzzle.values))
            puzzle.restoreState()

        if puzzle.moveDown():
            heapq.heappush(openList, (puzzle.priority, puzzle.values))
            puzzle.restoreState()

        if puzzle.moveLeft():
            heapq.heappush(openList, (puzzle.priority, puzzle.values))
            puzzle.restoreState()

        if puzzle.moveRight():
            heapq.heappush(openList, (puzzle.priority, puzzle.values))
            puzzle.restoreState()

        nextState = heapq.heappop(openList)
        closeList.append(nextState)
        #print(closeList)
        puzzle.setValues(nextState[0],nextState[1])
        #puzzle.printCurrentPuzzle()
        index += 1

    return index, time.time() - startTime

print(aStar())
