import pygame
from Quadtree import Quadtree
from Particle import Particle
import random
import sys

clock = pygame.time.Clock()

width = 800 
height = 800

black = (0,0,0)

tickrate = 30

screen = pygame.display.set_mode((width, height))

numberParticles = 50
quadtreeCapacity = 5 

particles = [Particle([random.randint(0, width), random.randint(0, height)]) for i in range(numberParticles)]
quadTree = Quadtree([0, 0], width, quadtreeCapacity)

mouseOnePressed = False
drawQuadtree = False
mouseThreePressed = False


while True:
    clock.tick(tickrate)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouseOnePressed:
            pos = pygame.mouse.get_pos()
            particles.append((Particle(list(pos))))
            mouseOnePressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouseOnePressed:
            mouseOnePressed = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not mouseThreePressed: 
            mouseThreePressed = True
            if drawQuadtree:
                drawQuadtree = False
            else:
                drawQuadtree = True
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3 and mouseThreePressed:
            mouseThreePressed = False
            
    quadTree.reset()

    for particle in particles:
        particle.randomMove()
        quadTree.insert(particle)

    if drawQuadtree:
        quadTree.draw(screen)

    for tree in quadTree.loop():
        for particleA in tree.particles:

            particleA.colliding = False
            
            for particleB in tree.particles:
                if particleA != particleB and Particle.checkCollision(particleA, particleB):
                    particleA.colliding = True

            particleA.draw(screen)

    pygame.display.update()