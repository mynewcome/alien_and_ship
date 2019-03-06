
# -*- coding: gb2312 -*-
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #���طɴ�ͼ�񲢻�ȡ����Ӿ���
        self.image = pygame.image.load('image/4.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #��ÿ�ҷɴ�������Ļ�ײ�����λ��
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #�ڷɴ�������centerx�д洢С��ֵ
        self.center = float(self.rect.centerx)
        
        #�ƶ���־     
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        #���·ɴ���centerֵ������rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def center_ship(self):
        """�÷ɴ�����Ļ�о���"""
        self.center = self.screen_rect.centerx
