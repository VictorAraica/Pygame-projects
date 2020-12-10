import pygame
import sys
from Board import Board

pygame.init()
clock = pygame.time.Clock()

width = 1800
height = 1000
cell_width = 20

screen = pygame.display.set_mode((width, height))


board = Board(cell_width, width // cell_width, height // cell_width, screen)

loop = False
end = False

board.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not loop:
            if board.startPoint == None:
                board.setStart(pygame.mouse.get_pos())
            elif board.endPoint == None:
                board.setEnd(pygame.mouse.get_pos())

        elif pygame.mouse.get_pressed()[2] and not end and not loop:
            board.setWall(pygame.mouse.get_pos())

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not loop and board.init():
                loop = True


    if len(board.openSet) == 0 and loop:
        loop = False
        end = True

    elif loop:
        if board.endPoint in board.closeSet: 
            loop = False
            end = True
        
        board.loop(board.getLowestF())
        
    elif end:
        board.startPoint.parent = False
        board.getPath(board.endPoint)


    pygame.display.update()

