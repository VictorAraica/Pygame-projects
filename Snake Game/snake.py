from pygame.draw import rect

class Snake:
    color = (255,255,255)
    def __init__(self, pos, size, body_margin):
        self.init_pos = pos
        self.body = [pos]
        self.speed = {"up":[False, (0, -1)], "down":[False, (0, 1)], "right":[False, (1, 0)], "left":[False, (-1, 0)]}
        self.size = size
        self.body_margin = body_margin


    def get_new_head_pos(self):
        for movement in self.speed:
            if self.speed[movement][0]:
                direction = self.speed[movement][1]
                pos = self.body[0]
                return [pos[0] + (direction[0] * (self.size + self.body_margin)),
                                pos[1] + (direction[1] * (self.size + self.body_margin))]
        return None

    
    def move(self):
        new_head_pos = self.get_new_head_pos()
        if new_head_pos == None:
            return False

        elif len(self.body) == 1:
            self.body[0] = new_head_pos
            return True

        self.body = self.body[:-1]
        self.body.insert(0, new_head_pos)
        return True
        

    def draw(self, screen):
        for piece_pos in self.body:
            rect(screen, Snake.color, (piece_pos, (self.size, self.size)))
        
    
    def speed_reset(self):
        for direction in self.speed:
            self.speed[direction][0] = False

    
    def change_dir(self, direction):
        self.speed_reset()
        self.speed[direction][0] = True


    def get_direction(self):
        for direction in self.speed:
            if self.speed[direction][0]:
                return direction
        else:
            return None


    def check_food(self, food):
        if list(self.body[0]) == list(food.pos):
            return True
        
        return False


    def grow(self):
        for movement in self.speed:
            if self.speed[movement][0]:
                direction = self.speed[movement][1]
                tail = self.body[-1]
                self.body.append([tail[0] + (direction[0] * (self.size + self.body_margin) * -1),
                                  tail[1] + (direction[1] * (self.size + self.body_margin) * -1)])


    def check_self_collision(self):
        if self.body[0] in self.body[1:]:
            return True
        return False

    
    def check_wall_collision(self, limits):
        if self.body[0][0] < 0 or self.body[0][1] < 0:
            return True
        if self.body[0][0] > limits[0] or self.body[0][1] > limits[1]:
            return True
        return False

    
    def reset(self):
        self.body = [self.init_pos]
        self.speed = {"up":[False, (0, -1)], "down":[False, (0, 1)], "right":[False, (1, 0)], "left":[False, (-1, 0)]}