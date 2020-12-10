import pygame
import math
import random

width = 4
notCollidingColor = (100,100,100)
collidingColor = (255,255,255)



class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.colliding = False


    def draw(self, window):
        if not self.colliding:
            pygame.draw.circle(window, notCollidingColor, self.pos, width)
        else:
            pygame.draw.circle(window, collidingColor, self.pos, width)


    def randomMove(self):
        self.pos[0] += random.randint(-1, 1)
        self.pos[1] += random.randint(-1, 1)

    @staticmethod
    def distance(a, b):
        return math.sqrt((a.pos[0] - b.pos[0]) ** 2 + (a.pos[1] - b.pos[1]) ** 2)


    @staticmethod
    def checkCollision(a, b):
        if Particle.distance(a, b) < width * 2:
            return True
        return False

