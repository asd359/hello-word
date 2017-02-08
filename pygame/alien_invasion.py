#coding:utf-8
import sys
import  pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()#初始化背景设置
    # screen = pygame.display.set_mode((900,600))#创建一个游戏窗口
    pygame.display.set_caption('Alien Invasion')

    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    # bg_color = (230,230,230)
    while True:
        # for event in pygame.event.get():
        #     if   event.type == pygame.QUIT:
        #            sys.exit()
        # screen.fill(bg_color)
        # pygame.display.flip()
        gf.check_events()

        gf.update_screen(ai_settings,screen,ship)

run_game()

