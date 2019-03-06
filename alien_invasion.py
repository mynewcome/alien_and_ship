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
#��ʼ����Ϸ������һ����Ļ����
def run_game():
    pygame.init()
    new_setting = Settings_1()
    screen = pygame.display.set_mode((new_setting.screen_width,
    new_setting.screen_height))
    pygame.display.set_caption("Alian Invasion")
    #����һ��play��ť
    play_button = Button(new_setting,screen,"Play")
    #����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
    stats = GameStats(new_setting)
    #�����洢��Ϸͳ����Ϣ��ʵ�����������Ƿ���
    sb = Scoreboard(new_setting,screen,stats)
    #����һ�ҷɴ�
    ship = Ship(new_setting,screen)
    #����һ�����ڴ洢�ӵ��ı���
    bullets = Group()
    #����һ��������
    #alien = Alien(new_setting,screen)
    aliens = Group()
    gf.create_fleet(new_setting,screen,ship,aliens)
    #��Ϸ��ѭ��
    while True:
        #���Ӽ��̺�����¼�
        gf.check_events(new_setting,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(new_setting,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(new_setting,stats,sb,screen,ship,aliens,bullets)
        #print(len(bullets))  ����������ڼ���Ƿ����е��ӵ�����ɾ����   
        #��������Ƶ���Ļ�ɼ�
        gf.update_screen(new_setting,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
