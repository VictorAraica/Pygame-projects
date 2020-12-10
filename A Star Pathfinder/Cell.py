import pygame
import math

class Cell:
    def __init__(self, x, y, size, screen):
        self.size = size
        self.pos = pygame.math.Vector2(x, y)
        self.startPoint = False
        self.endPoint = False
        self.visited = False
        self.expanded = False
        self.wall = False
        self.bestPath = False

        self.f = 0
        self.g = 0
        self.h = 0

        self.parent = None

        self.color = (255,255,255)

        self.screen = screen


    def draw(self):
        pygame.draw.rect(self.screen, self.color, ((self.pos.x * self.size) + 1, (self.pos.y * self.size) + 1, self.size - 1, self.size - 1)) 

        
    def calculate(self, endPoint):
        self.g = self.calculateG(self.parent)
        if self.h == 0:
            self.h = math.sqrt((self.pos[0] - endPoint.pos[0])**2 + (self.pos[1] - endPoint.pos[1])**2)  
        self.f = self.g + self.h


    def calculateG(self, parentCell):
        return parentCell.g + abs(self.parent.pos[0] - self.pos[0]) + abs(self.parent.pos[1] - self.pos[1])