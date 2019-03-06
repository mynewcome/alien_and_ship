# -*- coding: gb2312 -*-
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
       #向右移动飞船
       ship.moving_right = True
    elif event.key == pygame.K_LEFT:
       #向左移动飞船 
       ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一颗子弹并将它加入到编组中 而且只有当未消失的子弹数小于三个时才会创建新子弹
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
               
def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 
            
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)               
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,
                ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,
        bullets,mouse_x,mouse_y):
    #玩家单击play按钮的时候开始游戏
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        #隐藏鼠标的光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        #显示剩余飞船数
        sb.prep_ships()
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
    
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    #更新屏幕上的图像并切换到新屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #显示得分
    sb.show_score()
    #如果游戏在非活动状态，绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹位置并删除已经消失在屏幕外的子弹"""
    #更新位置
    bullets.update()
    #消除子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)  
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
    
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #检查是否有子弹碰撞到了外星人，如果是就将子弹和外星人都删除　高能子弹第一个实参设为False
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():          
            stats.score +=ai_settings.alien_points *len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        #外星人都被消灭后，提高一个等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)
        
def fire_bullet(ai_settings,screen,ship,bullets):
    #创建一颗子弹并将它加入到编组中 而且只有当未消失的子弹数小于三个时才会创建新子弹
    if len(bullets) < ai_settings.bullet_allow:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
            
def get_number_rows(ai_settings,ship_height,alien_height):
    availiable_space_y = (ai_settings.screen_height - (3*alien_height) - 
        ship_height)
    number_rows = int(availiable_space_y /(2*alien_height))
    return number_rows
 
def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳多少外星人"""
    availiable_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(availiable_space_x /(2*alien_width))
    return number_aliens_x
    
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width +2*alien_width*alien_number      
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height +2*alien.rect.height*row_number
    aliens.add(alien)
    
def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
        alien.rect.height)
    
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,
                row_number)
               
def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘的时候采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        #将ships_left减1
        stats.ships_left -= 1
        #更新记分牌
        sb.prep_ships()
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人并把飞船放到屏幕底部中央位置
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """检查是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()     
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break
            
def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    #更新外星人群中的所有外星人
    check_fleet_edges(ai_settings,aliens)
    aliens.update() 
    
    #监测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
              
    check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)

def check_high_score(stats,sb):
    """检查是否诞生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
