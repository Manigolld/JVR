from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

Y_POS_BIRD = 250

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        self.image = BIRD

        super().__init__(images, self.type)

        self.rect.y = Y_POS_BIRD
        self.bird_index = 0

    def draw(self, screen):
       
        if self.bird_index < 5:
            self.image = 0
        else:
            self.image = 1

        screen.blit(self.images[self.image], (self.rect.x, self.rect.y))

        self.bird_index+=1

        if self.bird_index >= 10:
            self.bird_index = 0