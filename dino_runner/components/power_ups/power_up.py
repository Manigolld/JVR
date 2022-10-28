import pygame
import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

Y_POS = 200
class PowerUp(Sprite):
    def __init__(self, image):
        self.image = image
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH 
        self.rect.y = Y_POS
        self.start_time = 0
        self.duration = random.randint(3,6)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed

        if self.rect.x < self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

