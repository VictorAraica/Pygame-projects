import pygame
import sys
from grid import Grid
from person import Person

clock = pygame.time.Clock()

grid_width = 10
grid_height = 10
cell_size = 80

width = 800 
height = 800 

black = (0,0,0)

tickrate = 30

screen = pygame.display.set_mode((width, height))

wall_color = (0, 0, 0)
color = (255, 255, 255)
pink = (255, 0, 255)



grid = Grid(grid_width, grid_height, cell_size)
person = Person((width//2, height//2), grid)


while True:
    clock.tick(tickrate)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseCellX = pygame.mouse.get_pos()[0] // cell_size
                mouseCellY = pygame.mouse.get_pos()[1] // cell_size
                personCellX = person.pos[0] // cell_size
                personCellY = person.pos[1] // cell_size
                if (mouseCellX, mouseCellY) != (personCellX, personCellY):
                    if grid.cells[mouseCellY][mouseCellX].wall:
                        grid.cells[mouseCellY][mouseCellX].wall = False
                    else:
                        grid.cells[mouseCellY][mouseCellX].wall = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                person.move(forward=True)
            if event.key == pygame.K_a:
                person.change_angle(clockwise=False)
            if event.key == pygame.K_s:
                person.move(forward=False)
            if event.key == pygame.K_d:
                person.change_angle(clockwise=True)
                
    grid.drawGrid(screen)
    person.drawPerson(screen)
    person.drawRays(screen)

    pygame.display.update()