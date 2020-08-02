from collections import deque

class Maze:
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"
    MAZE_START = "S"
    MAZE_END = "E"
    
    def __init__(self, numRows, numCols):
        self._mazeCells = [[' ' for col in range(numCols)] for row in range(numRows)]
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
                self.stack.append(self._startCell.returnPos())

            elif self._exitFound(self.stack[-1][0], self.stack[-1][1]):
                print('Maze Complete!')
                break

            elif self._validMove(self.stack[-1][0]-1, self.stack[-1][1]):
                self.stack.append([self.stack[-1][0]-1, self.stack[-1][1]])
                
            elif self._validMove(self.stack[-1][0], self.stack[-1][1]-1):
                self.stack.append([self.stack[-1][0], self.stack[-1][1]-1])

            elif self._validMove(self.stack[-1][0]+1, self.stack[-1][1]):
                self.stack.append([self.stack[-1][0]+1, self.stack[-1][1]])

            elif self._validMove(self.stack[-1][0], self.stack[-1][1]+1):
                self.stack.append([self.stack[-1][0], self.stack[-1][1]+1])

            elif self.stack != deque([self._startCell.returnPos]):
                self._markTried(self.stack[-1][0], self.stack[-1][1])
                self.stack.pop()

            else:
                print('no valid move')
                break

            self._markPath(self.stack[-1][0],self.stack[-1][1])
        self.draw()
            
    def reset(self):
        self.stack = deque()
        self._mazeCells = [['{}'.format(' ' if (self._mazeCells[row][col] == ' ' or (self._mazeCells[row][col] == 'x' and not self._exitFound(col, row) and not self._startFound(col, row)) or self._mazeCells[row][col] == 'o') else '{}'.format('*' if self._mazeCells[row][col] == '*' else '{}'.format('E' if self._exitFound(col, row) else 'S'))) for col in range(self.numCols)] for row in range(self.numRows)]
        
    def draw(self):
        for i in range(self.numRows):
            print(' ---' * self.numCols)
            row = ''
            for l in range(self.numCols):
                row= row + ' {} |'.format(self._mazeCells[i][l])
            print('|' + row)
        print(' ---' * self.numCols)
        
    def _validMove(self, col, row):
        return (row >= 0 and row < self.numRows) and (col >= 0 and col < self.numCols) and ( self._mazeCells[row][col] == ' ' or self._exitFound(col, row))

    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col

    def _startFound(self, row, col):
        return row == self._startCell.row and col == self._startCell.col
    
    def _markTried(self, row, col):
        self._mazeCells[col][row] = self.TRIED_TOKEN
        
    def _markPath(self, row, col):
        self._mazeCells[col][row] = self.PATH_TOKEN
        
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def returnPos(self):
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
    myMaze.setWall(2,3)
    myMaze.setWall(0,4)
    myMaze.setWall(2,4)
    myMaze.setWall(3,3)
    myMaze.setWall(4,3)
    myMaze.setWall(5,0)
    myMaze.setWall(6,0)
    myMaze.setWall(6,2)
    myMaze.setWall(6,3)
    myMaze.setStart(0,3)
    myMaze.setExit(3,4)

myMaze = Maze(5, 7)
print('set maze:')
setMaze()
myMaze.draw()

print('solve maze:')
myMaze.findPath()

print('reset maze:')
myMaze.reset()
myMaze.draw()
