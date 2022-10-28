import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.dinossaur import Dinossaur


class PowerUpManager:
    def __init__(self):
        self.power_ups = []

    def update(self, game):

        if len(self.power_ups) == 0 and not game.player.has_power_up == True and self.when_appears == game.score:
            self.when_appears += random.randint(200,300)
            power_up_type = random.randint(0,1)    
            if power_up_type == 1:
                self.power_ups.append(Shield())
            else:
                self.power_ups.append(Hammer())

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()     
                if self.power_ups == 1:
                    game.player.has_shield = True
                    game.player.has_hammer = False
            
                else:
                    game.player.has_hammer = True
                    game.player.has_shield = False


                
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                
    


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200,300)
