import pygame
import sys
from circle import Circle
from circle import Combination
import math

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
dark_red = (150, 30, 30)

width = 900
height = 900

num_circles = 8
margin = 10
circle_radius = int((width / (2 * (num_circles + 1))) - margin)
space_per_circle = circle_radius * 2 + margin * 2
circle_width = 4

screen = pygame.display.set_mode((width, height))


def draw_combination(combination, pos):
    points = map(lambda x: (x[0] + pos[0], x[1] + pos[1]), combination.points)
    pygame.draw.aalines(screen, black, False, list(points), 4)


def draw_combination_line(combination, pos):
    p1 = (combination.points[0][0] + pos[0], combination.points[0][1] + pos[1])
    p2 = (combination.points[-1][0] + pos[0], combination.points[-1][1] + pos[1])
    pygame.draw.aaline(screen, dark_red, p1, p2)


def calculate_pos(x, y):
    # calculates the position of the circle in the screen
    space_x = space_per_circle * x + space_per_circle // 2
    space_y = space_per_circle * y + space_per_circle // 2
    return (space_x, space_y) 


vertical_circles = [Circle(calculate_pos(0, y), circle_radius, math.radians(y)) for y in range(1, num_circles + 1)]
horizontal_circles = [Circle(calculate_pos(x, 0), circle_radius, math.radians(x)) for x in range(1, num_circles + 1)]

# combination_line_len: is the amount of points saved to draw the combination
# when the list is full, they will add one on each update and delete the last one
combination_line_len = 200

combinations = [[ Combination(circleX, circleY, combination_line_len) for circleX in horizontal_circles ] for circleY in vertical_circles]


while True:
    clock.tick(60)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for x in range(len(horizontal_circles)):
        horizontal_circles[x].update_angle()
        horizontal_circles[x].draw_circle(screen)

    for y in range(len(combinations)):
        vertical_circles[y].update_angle()
        vertical_circles[y].draw_circle(screen)
        for x in range(len(combinations[0])):
            combinations[y][x].update_points()
            combinations[y][x].draw_combination(screen)

    pygame.display.update()
