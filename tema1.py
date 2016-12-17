import random
import time


class EightPuzzle:
    def __init__(self):
        #self.values = [0,1,3,4,2,5,7,8,6]
        self.values = [8,1,3,4,0,2,7,6,5]
        self.previousValues = []
        self.currentPossibleMoves = []
        self.emptySquarePosition = -1
        self.fitness = -1

        self.updateState()

    def updateState(self):
        self.emptySquarePosition = self.values.index(0)
        self.getPossibleMoves()
        # DO this
        self.getCurrentStateFitness()

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
            return False

    def restoreState(self):
        self.values = list(self.previousValues)
        self.updateState()


def findSolutionPuzzleHillClimbing():
    startTime = time.time()

    puzzle = EightPuzzle()
    currentFitness = puzzle.fitness

    nextMove = random.choice(['up', 'down', 'left', 'right'])

    temperature = 100

    while not puzzle.finished():
        movesFitness = {'up': 0, 'down': 0, 'left': 0, 'right': 0}

        if puzzle.moveUp():
            movesFitness['up'] = puzzle.fitness
            puzzle.restoreState()

        if puzzle.moveDown():
            movesFitness['down'] = puzzle.fitness
            puzzle.restoreState()

        if puzzle.moveLeft():
            movesFitness['left'] = puzzle.fitness
            puzzle.restoreState()

        if puzzle.moveRight():
            movesFitness['right'] = puzzle.fitness
            puzzle.restoreState()

        found = False

        for move in movesFitness:
            if movesFitness[move] > currentFitness:
                currentFitness = movesFitness[move]
                nextMove = move
                found = True

        if found:
            puzzle.move(nextMove)
            currentFitness = puzzle.fitness
        else:
            found = False
            for move in movesFitness:
                if movesFitness[move] == currentFitness:
                    nextMove = move
                    found = True

            if found and temperature > 0:
                temperature -= 1
                puzzle.move(nextMove)
                currentFitness = puzzle.fitness
            else:
                return time.time() - startTime, puzzle.values, puzzle.fitness

    return time.time() - startTime, puzzle.values, puzzle.fitness


print(findSolutionPuzzleHillClimbing())
