import pygame
import sys
from food import Food 
from snake import Snake
from random import randint

clock = pygame.time.Clock()

black = (0,0,0)

grid_width = 50
grid_height = 50
cell_size = 15 
grid_margin = 2 
screen_width = grid_width * cell_size + ((grid_width - 1) * grid_margin)
screen_height = grid_height * cell_size + ((grid_height - 1) * grid_margin)

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', cell_size * 3)
textsurface = myfont.render('Press a, w, s, d to start playing', False, (255,255,0))
textsurface1 = myfont.render('Game Over', False, (255,255,0))
textsurface2 = myfont.render('Press space to restart', False, (255,255,0))

screen = pygame.display.set_mode((screen_width, screen_height))

food_size = 15 
grid_margin = 2 

food = Food((0, 0), food_size)
food.move((randint(0, grid_width) * (cell_size + grid_margin), 
           randint(0, grid_height) * (cell_size + grid_margin)))

snake = Snake([grid_width // 2 * (cell_size + grid_margin),grid_height // 2 * (cell_size + grid_margin)], cell_size, grid_margin)

game_over = False
game_started = False

while True:
    clock.tick(13)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.get_direction() != "down":
                snake.change_dir("up")
            elif event.key == pygame.K_a and snake.get_direction() != "right":
                snake.change_dir("left")
            elif event.key == pygame.K_s and snake.get_direction() != "up":
                snake.change_dir("down")
            elif event.key == pygame.K_d and snake.get_direction() != "left":
                snake.change_dir("right")

            if (not game_started) and event.key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]:
                game_started = True
            
            if event.key == pygame.K_SPACE and game_over:
                snake.reset()
                food.move((randint(0, grid_width - 1) * (cell_size + grid_margin), 
                           randint(0, grid_height - 1) * (cell_size + grid_margin)))
                game_over = False
                game_started = False           


    screen.fill(black)

    if not game_over:
        snake.move()
        if snake.check_self_collision() or snake.check_wall_collision((screen_width, screen_height)):
            game_over = True

        if snake.check_food(food):
            food.move((randint(0, grid_width - 1) * (cell_size + grid_margin), 
                    randint(0, grid_height - 1) * (cell_size + grid_margin)))
            snake.grow()
        
    snake.draw(screen)
    food.draw(screen)


    if game_over:
        screen.blit(textsurface1,(int(screen_width * 0.35), int(screen_height * 0.01)))
        screen.blit(textsurface2,(int(screen_width * 0.15), int(screen_height * 0.9)))

    if not game_started:
        screen.blit(textsurface,(int(screen_width * 0.15), int(screen_height * 0.01)))
    pygame.display.update()
