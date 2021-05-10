import math
import pygame

class Ray:
    def __init__(self, angle, grid):
        self.angle = angle
        self.grid = grid
        self.collision_pos = (0,0)
        self.color = (0,200,200)

    def add_angle(self, change):
        if self.angle + change > 2 * math.pi:
            change -= 2 * math.pi
        elif self.angle + change < 0:
            change += 2 * math.pi
        self.angle += change

    def calculate_collision(self, person_pos, screen):
        min_dist = self.grid.width * (self.grid.cell_size) * 2
        x_index_offset = 0 
        y_index_offset = 0
        collision_x_offset = 0
        collision_y_offset = 0

        collisions = []
        person_cell_pos = (person_pos[0]//(self.grid.cell_size), person_pos[1]//(self.grid.cell_size))
        minX = person_cell_pos[0] 
        minY = person_cell_pos[1]

        if math.pi / 2 >= self.angle or math.pi * 2 >= self.angle >= (3 * math.pi) / 2:
            maxX = self.grid.width
            minX += 1
            stepsX = 1 
        else:
            maxX = -1
            stepsX = -1
            x_index_offset = -1

        if math.pi >= self.angle >= 0:
            maxY = self.grid.height
            minY += 1
            stepsY = 1
        else:
            maxY = -1
            stepsY = -1
            y_index_offset = -1



        for x in range(int(minX), maxX, stepsX):
        
            try:
                collisionX = math.ceil(x * (self.grid.cell_size)) 
                m = math.tan(self.angle)
                b = person_pos[1] - m * person_pos[0]
                collisionY = math.ceil(m * collisionX + b)

                if self.grid.cells[collisionY//(self.grid.cell_size)][(collisionX//(self.grid.cell_size)) + x_index_offset].wall:        
                    min_dist = math.sqrt((person_pos[0] - collisionX)**2 + (person_pos[1] - collisionY)**2)
                    break

            except (OverflowError, ZeroDivisionError, IndexError):
                continue

        for y in range(int(minY), maxY, stepsY):
            try:
                collisionY = math.floor(y * (self.grid.cell_size))
                m = math.tan(self.angle)
                b = person_pos[1] - m * person_pos[0]
                collisionX = math.floor((collisionY - b) // m)

                if self.grid.cells[(collisionY//(self.grid.cell_size)) + y_index_offset][collisionX//(self.grid.cell_size)].wall:
                    dist = math.sqrt((person_pos[0] - collisionX)**2 + (person_pos[1] - collisionY)**2)
                    if dist < min_dist:
                        min_dist = dist
                    break

            except (OverflowError, ZeroDivisionError, IndexError):
                continue
            

        x = min_dist * math.cos(self.angle)
        y = min_dist * math.sin(self.angle)

        self.collision_pos = (x + person_pos[0], y + person_pos[1])


    def drawRay(self, screen, person_pos):
        pygame.draw.line(screen, self.color, person_pos, self.collision_pos)




        
            