from cell import Cell
import pygame

class Grid:

    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.wall_color = (0, 0, 0)
        self.color = (255, 255, 255) 
        self.cell_size = cell_size

        self.cells = [ [Cell(self.cell_size, pygame.math.Vector2(j, i)) for j in range(self.width)] for i in range(self.height) ]


    def drawGrid(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                cell_color = self.wall_color if self.cells[y][x].wall else self.color
                pygame.draw.rect(screen, cell_color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    


