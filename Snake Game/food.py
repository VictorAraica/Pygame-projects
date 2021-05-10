from pygame.draw import rect
class Food:
    color = (255, 0, 0)
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.eaten = False

    def draw(self, screen):
        rect(screen, Food.color, (self.pos, (self.size, self.size)))

    def move(self, new_pos):
        self.pos = new_pos