import pygame
from ray import Ray
import math

class Person:

    def __init__(self, pos, grid):
        self.pos = pos
        self.angle = math.radians(45)
        self.fov = 20
        self.color = (200, 0, 200)
        self.grid = grid
        self.velocity = 15
        self.sensitivity = math.radians(10)

        self.rays = [Ray(math.radians(offset - (self.fov//2)) + self.angle, grid) for offset in range(self.fov)]

    def move(self, forward):
        change_in_x = math.cos(self.angle) * self.velocity
        change_in_y = math.sin(self.angle) * self.velocity

        if not forward:
            change_in_x *= -1
            change_in_y *= -1
            
        x = self.pos[0] + change_in_x
        y = self.pos[1] + change_in_y

        if x < 0:
            x += (self.grid.width * self.grid.cell_size)
        elif x > self.grid.width * self.grid.cell_size:
            x -= self.grid.width * self.grid.cell_size

        if y < 0:
            y += (self.grid.height * self.grid.cell_size)
        elif y > self.grid.height * self.grid.cell_size:
            y -= self.grid.height * self.grid.cell_size

        if self.grid.cells[int(y // self.grid.cell_size)][int(x // self.grid.cell_size)].wall:
            return


        self.pos = (x, y)

    def change_angle(self, clockwise):
        change = self.sensitivity
        if not clockwise:
            change *= -1

        if self.angle + change >= 2 * math.pi:
            change -= 2 * math.pi
        elif self.angle + change < 0:
            change += 2 * math.pi
        self.angle += change

        for ray in self.rays:
            ray.add_angle(change)

    def update_collisions(self):
        for ray in self.rays:
            ray.find_colisions(self.pos)

    def drawPerson(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), 5)

    def drawRays(self, screen):
        for ray in self.rays:
            ray.calculate_collision(self.pos, screen)
            ray.drawRay(screen, self.pos)

    
