from collections import deque

class Maze:
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"
    MAZE_START = "S"
    MAZE_END = "E"
    
    def __init__(self, numRows, numCols):
        self._mazeCells = [[' ' for i in range(numCols)] for i in range(numRows)]
        self._startCell = None
        self._exitCell = None
        self.numRows = numRows
        self.numCols = numCols
        self.stack = deque()
        
    def numRows(self):
        return self.numRows
    
    def numCols(self):
        return self.numCols
    
    def setWall(self,row,col):
        self._mazeCells[col][row] = self.MAZE_WALL
        
    def setStart(self, row, col):
        self._startCell = _CellPosition(row, col)
        self._mazeCells[col][row] = self.MAZE_START
        
    def setExit(self, row, col):
        self._exitCell = _CellPosition(row, col)
        self._mazeCells[col][row] = self.MAZE_END
        
    def findPath(self):

        while True:
            if self.stack == deque([]):
                self.stack.append(self._startCell.returnStart())

            elif self._validMove(self.stack[-1][0]-1, self.stack[-1][1]):
                self.stack.append([self.stack[-1][0]-1, self.stack[-1][1]])
                
            elif self._validMove(self.stack[-1][0], self.stack[-1][1]-1):
                self.stack.append([self.stack[-1][0], self.stack[-1][1]-1])

            elif self._validMove(self.stack[-1][0]+1, self.stack[-1][1]):
                self.stack.append([self.stack[-1][0]+1, self.stack[-1][1]])
                

            elif self._validMove(self.stack[-1][0], self.stack[-1][1]+1):
                self.stack.append([self.stack[-1][0], self.stack[-1][1]+1])


            elif self._exitFound(self.stack[-1][0], self.stack[-1][1]):
                print('Maze Complete!')
                break

            elif self.stack != deque([self._startCell.returnStart]):
                self._markTried(self.stack[-1][0], self.stack[-1][1])
                self.stack.pop()

            else:
                print('no valid move')
                break

            self._markPath(self.stack[-1][0],self.stack[-1][1])
        self.draw()
            
    def reset(self):
        
        self.stack = deque()
        
    def draw(self):
        for i in range(self.numRows):
            print(' ---' * self.numCols)
            row = ''
            for l in range(self.numCols):
                row= row + ' {} |'.format(self._mazeCells[i][l])
            print('|' + row)
        print(' ---' * self.numCols)
        
    def _validMove(self, row, col):
        return row >= 0 and row < self.numRows and col >= 0 and col < self.numCols and (self._mazeCells[col][row] == ' ' or self._exitFound(row, col))

    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col
    
    def _markTried(self, row, col):
        self._mazeCells[col][row] = self.TRIED_TOKEN
        
    def _markPath(self, row, col):
        self._mazeCells[col][row] = self.PATH_TOKEN
        
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def returnStart(self):
        return self.row, self.col


#DEMO

def setMaze():
    myMaze.setWall(0,0)
    myMaze.setWall(1,0)
    myMaze.setWall(2,0)
    myMaze.setWall(3,0)
    myMaze.setWall(4,0)
    myMaze.setWall(0,1)
    myMaze.setWall(2,1)
    myMaze.setWall(4,1)
    myMaze.setWall(0,2)
    myMaze.setWall(4,2)
    myMaze.setWall(0,3)
    myMaze.setWall(2,3)
    myMaze.setWall(0,4)
    myMaze.setWall(2,4)
    myMaze.setWall(3,4)
    myMaze.setWall(4,4)
    myMaze.setStart(1,4)
    myMaze.setExit(4,3)

myMaze = Maze(5, 5)
setMaze()
myMaze.draw()
myMaze.findPath()
