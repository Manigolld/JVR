from re import S
from select import select
import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, ICON
from dino_runner.components.dinossaur import Dinossaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Dinossaur()
        self.obstacle_manager = ObstacleManager()
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def execute(self):
        self.executing = True

        while(self.executing):

            if not self.playing and self.death_count == 0:
                self.display_menu()

            if not self.playing and self.death_count > 0:
                self.death_menu()
                
            
        pygame.display.quit()
        pygame.quit()

    def display_menu(self):
        self.screen.fill((0,0,0))
        
        font_size = 28
        color = (255,255,255)
        FONT = 'freesansbold.ttf'

        font = pygame.font.Font(FONT, font_size)
        text = font.render(f'Press any key to start', True, color)

        menu_text_rect = text.get_rect()
        menu_text_rect.x = 380
        menu_text_rect.y = 280

        self.screen.blit(text, (menu_text_rect.x, menu_text_rect.y))

        pygame.display.update()

        self.events_on_menu()

    def death_menu(self):
        self.screen.fill((0,0,0))
        
        font_size = 28
        color = (255,255,255)
        FONT = 'freesansbold.ttf'

        font = pygame.font.Font(FONT, font_size)
        text = font.render(f'Press any key to try again', True, color)

        death_text_rect = text.get_rect()
        death_text_rect.x = 350
        death_text_rect.y = 280

        self.screen.blit(text, (death_text_rect.x, death_text_rect.y))

        ##Texto para mostrar a pontuação
        score2_text = font.render(f'Score: {self.score}', True, color)
        score2_text_rect = text.get_rect()
        score2_text_rect.x = 475
        score2_text_rect.y = 320


        self.screen.blit(score2_text, (score2_text_rect.x, score2_text_rect.y))
        
        ##Texto para mostrar as mortes
        death_count = font.render(f'Deaths: {self.death_count}', True, color)
        death_count_rect = text.get_rect()
        death_count_rect.x = 475
        death_count_rect.y = 360


        self.screen.blit(death_count, (death_count_rect.x, death_count_rect.y))
        
        ##Mostra o icone do dinossauro
        dino_dead_icon = ICON
        dino_dead_icon_rect = text.get_rect()
        dino_dead_icon_rect.x = 495
        dino_dead_icon_rect.y = 175
        
        self.screen.blit(dino_dead_icon, (dino_dead_icon_rect.x, dino_dead_icon_rect.y))

        pygame.display.update()
        self.events_on_menu()
        

    def events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            if event.type == pygame.KEYDOWN:
                self.reset()
                self.run()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        
        self.update_score()
        self.update_game_speed()

    def update_score(self):
    
        self.score += 1

    def update_game_speed(self):
        if self.score % 100 == 0:
            self.game_speed += 5

    def reset(self):
        self.score = 0
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()
    
        

    def draw_score(self):
        font_size = 28
        color = (0,0,0)
        FONT = 'freesansbold.ttf'

        font = pygame.font.Font(FONT, font_size)
        text = font.render(f'Score: {self.score}', True, color)

        score_text_rect = text.get_rect()
        score_text_rect.x = 950
        score_text_rect.y = 10

        self.screen.blit(text, (score_text_rect.x, score_text_rect.y))

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
