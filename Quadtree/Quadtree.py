import pygame

quadtreeColor = (255,255,255)

class Quadtree:
    def __init__(self, pos, size, nodeCapacity):
        self.pos = pos
        self.size = size
        self.innerQuadtrees = {"NW":None, "NE":None, "SW":None, "SE":None}
        self.divided = False
        self.nodeCapacity = nodeCapacity
        self.particles = []


    def divide(self):
        self.innerQuadtrees["NW"] = Quadtree(self.pos, self.size//2, self.nodeCapacity)
        self.innerQuadtrees["NE"] = Quadtree([self.pos[0] + self.size//2, self.pos[1]], self.size//2, self.nodeCapacity)
        self.innerQuadtrees["SW"] = Quadtree([self.pos[0], self.pos[1] + self.size//2], self.size//2, self.nodeCapacity)
        self.innerQuadtrees["SE"] = Quadtree([self.pos[0] + self.size//2, self.pos[1] + self.size//2], self.size//2, self.nodeCapacity)

        for particle in self.particles:
            for quadTree in self.innerQuadtrees:
                if self.innerQuadtrees[quadTree].containsParticle(particle):
                    self.innerQuadtrees[quadTree].insert(particle)
                    break


    def insert(self, particle):
        if not self.divided and len(self.particles) < self.nodeCapacity:
            self.particles.append(particle)
            return True

        elif not self.divided and len(self.particles) >= self.nodeCapacity:
            self.divide()
            self.divided = True
                
        for quadTree in self.innerQuadtrees:
            if self.innerQuadtrees[quadTree].containsParticle(particle):
                self.innerQuadtrees[quadTree].insert(particle)


    def draw(self, window):
        pygame.draw.rect(window, quadtreeColor, (self.pos[0], self.pos[1], self.size, self.size), 1)
        if self.divided:
            for quadTree in self.innerQuadtrees:
                self.innerQuadtrees[quadTree].draw(window)


    def containsParticle(self, particle):
        if (self.pos[0] <= particle.pos[0] <= self.pos[0] + self.size) and (self.pos[1] <= particle.pos[1] <= self.pos[1] + self.size):
            return True
        else:
            return False
    

    def reset(self):
        self.innerQuadtrees = {"NW":None, "NE":None, "SW":None, "SE":None}
        self.divided = False
        self.particles = []


    def loop(self):
        quadtrees = []
        if self.divided:
            for quadTree in self.innerQuadtrees:
                if self.innerQuadtrees[quadTree].divided:
                    quadtrees.extend(self.innerQuadtrees[quadTree].loop())
                else:
                    quadtrees.append(self.innerQuadtrees[quadTree])
  
            return quadtrees
        return [self]