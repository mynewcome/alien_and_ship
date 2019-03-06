# -*- coding: gb2312 -*-
class Settings_1():
    #�洢��������Ϸ���������õ���    
    def __init__(self):
        """��ʼ����Ϸ�ľ�̬����"""
        self.screen_width = 1800
        self.screen_height = 1000
        self.bg_color = (255,255,255)
        #�ɴ���λ��
        self.ship_limit = 3
        #�ӵ�����   
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allow = 30
        #����������
        self.fleet_drop_speed = 10
        #�����˵���������ٶ�
        self.score_scale = 1.5
        
        #��ʲô�����ٶȼӿ���Ϸ�Ľ���
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """��ʼ������Ϸ���ж��仯������"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        #fleet_directionΪ1��ʾ�����ƶ���Ϊ-1��ʾ�����ƶ�
        self.fleet_direction = 1
        #�Ʒ�
        self.alien_points = 50
    def increase_speed(self):
        """����ٶ�����"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale   
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
