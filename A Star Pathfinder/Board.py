import pygame
from Cell import Cell

class Board:
    def __init__(self, cellSize, width, height, screen):
        self.board = [ [ Cell(x, y, cellSize, screen) for y in range(height) ] for x in range(width) ]
        self.startPoint = None
        self.endPoint = None
        self.openSet = []
        self.closeSet = []
        self.walls = []
        self.cellSize = cellSize
        self.screen = screen


    def draw(self):
        for column in self.board:
            for cell in column:

                cell.draw()


    def setStart(self, mousePos):
        x, y = mousePos[0] // self.cellSize, mousePos[1] // self.cellSize
        if self.board[x][y].wall == False:
            self.board[x][y].startPoint = True
            self.board[x][y].color = (0, 0, 255)
            self.startPoint = self.board[x][y]
            self.startPoint.draw()


    def setEnd(self, mousePos):
        x, y  = mousePos[0] // self.cellSize, mousePos[1] // self.cellSize
        if self.board[x][y].wall == False:
            self.board[x][y].endPoint = True
            self.board[x][y].color = (0, 0, 255)
            self.endPoint = self.board[x][y]
            self.endPoint.draw()


    def setWall(self, mousePos):
        x, y = mousePos[0] // self.cellSize, mousePos[1] // self.cellSize
        if self.board[x][y].startPoint == False and self.board[x][y].endPoint == False:
            self.board[x][y].wall = True
            self.board[x][y].color = (0, 0, 0)
            self.board[x][y].draw()


    def init(self):
        if self.startPoint and self.endPoint:
            self.openSet.append(self.startPoint)
            return True
        return False

    
    def loop(self, current):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= int(x + current.pos[0]) < len(self.board) and 0 <= int(y + current.pos[1]) < len(self.board[0]) and (abs(x + y) == 1):
                    neighbor = self.board[int(x + current.pos[0])][int(y + current.pos[1])]
                    if not neighbor in self.closeSet and not neighbor.wall:
                        if neighbor not in self.openSet:
                            self.openSet.append(neighbor)
                            neighbor.parent = current
                            neighbor.calculate(self.endPoint)
                            neighbor.visited = True
                            if not neighbor.startPoint and not neighbor.endPoint:
                                neighbor.color = (255, 0, 0)
                                neighbor.draw()

                        elif neighbor in self.openSet:
                            if neighbor.calculateG(current) < neighbor.g:
                                neighbor.parent = current
                                neighbor.calculate(self.endPoint)

        current.expanded = True
        if not current.startPoint and not current.endPoint:
            current.color = (0, 255, 0) 
            current.draw()
        self.closeSet.append(current)
        self.openSet.remove(current)

    
    def getLowestF(self):
        best = 0
        for i in range(len(self.openSet)):
            if self.openSet[i].f < self.openSet[best].f:
                best = i

        return self.openSet[best]


    def getPath(self, cell):
        if cell.parent and not cell.startPoint:
            cell.parent.bestPath = True
            cell.parent.color = (255, 0, 255)
            cell.draw()
            self.getPath(cell.parent)
            
