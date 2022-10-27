import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.dinossaur import Dinossaur


class PowerUpManager:
    def __init__(self):
        self.power_ups = []

    def update(self, game):

        if len(self.power_ups) == 0 and not game.player.has_power_up == True:
            power_up_type = random.randint(0,1)    
            if power_up_type == 1:
                self.power_ups.append(Shield())

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.dino_rect.colliderect(power_up.rect):
                game.player.has_shield = True
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                
    


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
