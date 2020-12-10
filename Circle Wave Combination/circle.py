import math
import pygame

black = (0, 0, 0)
dark_red = (150, 30, 30)

class Circle:
    circle_width = 4
    
    def __init__(self, pos, radius, velocity):
        self.pos = pos
        self.radius = radius
        self.velocity = velocity
        self.angle = 0

    def update_angle(self):
        self.angle += self.velocity
    
    def calculate_x(self):
        return int(self.radius * math.cos(self.angle))

    def calculate_y(self):
        return int(self.radius * math.sin(self.angle))

    def draw_circle(self, window):
        pygame.draw.circle(window, dark_red, self.pos, self.radius + (Circle.circle_width//2), Circle.circle_width)
        pygame.draw.circle(window, black, (self.pos[0] + self.calculate_x(), self.pos[1] + self.calculate_y()), Circle.circle_width)


class Combination:
    def __init__(self, circleX, circleY, points_array_len):
        self.circleX = circleX
        self.circleY = circleY
        self.points = [ (circleX.calculate_x(), circleY.calculate_y()) for i in range(points_array_len)]

    def update_points(self):
        self.points.pop()
        self.points.insert(0, (self.circleX.calculate_x(), self.circleY.calculate_y()))

    def draw_combination(self, window):
        points = map(lambda x: (x[0] + self.circleX.pos[0], x[1] + self.circleY.pos[1]), self.points)
        pygame.draw.aalines(window, black, False, list(points), 4)