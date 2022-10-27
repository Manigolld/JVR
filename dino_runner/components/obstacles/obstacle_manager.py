import random
import pygame
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:            
            obstacle_index = random.randint(0,2)
            if obstacle_index == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif obstacle_index == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_index == 2:
                self.obstacles.append(Bird(BIRD))
                      
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            #manage the colision
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_shield:
                    game.playing = False
                    pygame.time.delay(500)
                    game.death_count += 1
                    print(game.death_count)
                    break
                else:
                    self.obstacles.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []