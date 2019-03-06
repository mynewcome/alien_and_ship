# -*- coding: gb2312 -*-
import sys
import pygame
from pygame.sprite import Group
from settings import Settings_1
from ship import Ship
from game_stats import GameStats
from botton import Button
from scoreboard import Scoreboard
import game_func as gf
#初始化游戏并创建一个屏幕对象
def run_game():
    pygame.init()
    new_setting = Settings_1()
    screen = pygame.display.set_mode((new_setting.screen_width,
    new_setting.screen_height))
    pygame.display.set_caption("Alian Invasion")
    #创建一个play按钮
    play_button = Button(new_setting,screen,"Play")
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(new_setting)
    #创建存储游戏统计信息的实例，并创建记分牌
    sb = Scoreboard(new_setting,screen,stats)
    #创建一艘飞船
    ship = Ship(new_setting,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人
    #alien = Alien(new_setting,screen)
    aliens = Group()
    gf.create_fleet(new_setting,screen,ship,aliens)
    #游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(new_setting,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(new_setting,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(new_setting,stats,sb,screen,ship,aliens,bullets)
        #print(len(bullets))  主句代码用于监测是否所有的子弹都被删除了   
        #让最近绘制的屏幕可见
        gf.update_screen(new_setting,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
