
# -*- coding: gb2312 -*-
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/4.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘飞船放在屏幕底部中央位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #在飞船的属性centerx中存储小数值
        self.center = float(self.rect.centerx)
        
        #移动标志     
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        #更新飞船的center值而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def center_ship(self):
        """让飞船在屏幕中居中"""
        self.center = self.screen_rect.centerx
