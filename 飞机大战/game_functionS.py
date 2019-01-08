import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
##############################################################################################################################
def get_number_rows(set,ship_height,alien_height):
    '''计算能容纳多少行alien'''
    available_space_y=(set.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))-1 #调整外星人行数，
    return number_rows

def get_number_aliens_x(set,alien_width):
    '''计算每行容纳多少alien'''
    available_space_x = set.screen_width - alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))+1 #调整alien，多加一列
    return number_aliens_x

def create_alien(set,screen,aliens,alien_number,row_number):
    '''创建一个alien放在当前行'''
    alien = Alien(set, screen)
    alien_width = alien.rect.width
    alien.x = (alien_width + 2 * alien_width * alien_number-60) #调整alien之间的间距（x方向上的）
    alien.rect.x = alien.x
    alien.rect.y=(alien.rect.height+2*alien.rect.height*row_number+70) #调整alien 之间的距离（y方向上的）
    aliens.add(alien)

def create_fleet(set,screen,ship,aliens):  #fleet=舰队
    '''创建外形人群'''
    alien=Alien(set,screen)
    number_aliens_x=get_number_aliens_x(set,alien.rect.width)
    number_rows=get_number_rows(set,ship.rect.height,alien.rect.height)
    # alien_width=alien.rect.width
    '''
    available_space_x=set.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    '''
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(set,screen,aliens,alien_number,row_number)
        #alien=Alien(set,screen)
        # alien.x=alien_width+2*alien_width*alien_number
        # alien.rect.x=alien.x
        #aliens.add(alien)

def check_fleet_edgs(set,aliens):
    '''alien到屏幕边缘时采取相应措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(set,aliens)
            break

def change_fleet_direction(set,aliens):
    '''所有alien下移，并改变方向'''
    for alien in aliens.sprites():
        alien.rect.y+=set.fleet_drop_speed
    set.fleet_direction*=-1

##########################################################################################################################
def fire_bullet(set, screen, ship, bullets):
    # if len(bullets)<set.bullets_allowed:

    # 新建一颗子弹，并将其加入bullets中
    new_bullet = Bullet(set, screen, ship)
    # bullets.fase=True
    bullets.add(new_bullet)

###########################################################################################################################
'''检查键盘响应事件'''
def check_kdown_events(event,set,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        # ship.rect.centerx+=1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_UP:
        ship.moving_up = True
    elif event.key==pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(set,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_kup_events(event,ship):  # def check_kup_events(event,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    # elif event.key==pygame.K_SPACE:
    #     bullets.fase=False

def check_events(set,screen,stats,sb,play_button,ship,aliens,bullets):
    '''响应按键和鼠标事件，所有键盘和鼠标事件都将促使for循环！'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_kdown_events(event,set,screen,ship,bullets)
            '''
            if event.key==pygame.K_RIGHT:
                #ship.rect.centerx+=1
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                ship.moving_left=True
            '''
        elif event.type==pygame.KEYUP:
            check_kup_events(event,ship)   #check_kup_events(event,ship,bullets)
            '''
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                ship.moving_left=False
            '''
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos() #返回一个元祖，包含点击鼠标的x/y坐标
            check_play_button(set,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

###########################################################################################################################

def check_play_button(set,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''玩家单击屏幕按钮便开始新游戏'''
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y) #检查点击鼠标位置是否在按钮的rect内
    if button_clicked and not stats.game_active:
        #重置游戏设置
        set.initialize_dynamic_settings()
        #游戏开始隐藏鼠标
        pygame.mouse.set_visible(False)
        #一旦点击按钮重置游戏
        stats.rest_stats()
        stats.game_active=True

        #重置记分
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #清空外星人和子弹
        aliens.empty()
        bullets.empty()
        #创建外星人，并让飞船居中
        create_fleet(set,screen,ship,aliens)
        ship.center_ship()


###########################################################################################################################
def check_high_score(stats,sb):
    '''检查是否诞生最高分'''
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()


############################################################################################################################
def check_bullet_alien_collisions(set,screen,stats,sb,ship,aliens,bullets):
    '''检查外星人和子弹的碰撞'''
    # collisions=碰撞\\\*****sprite.groupcollide()检测两个编组成员之间的碰撞，另外还要注意后两个布尔型参数的含义（第一个：超级子弹，第二个：删除碰撞的子弹和飞船）*********
    # 返回值为：字典
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=set.alien_points
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens)==0:
        #删除现有的子弹并新建一群外星人，在加快游戏节奏即提高飞船、外星人等速度
        bullets.empty()
        set.increase_speed()
        stats.level+=1  #提高等级
        sb.prep_level()
        create_fleet(set,screen,ship,aliens)

############################################################################################################################
def ship_hit(set,screen,stats,sb,ship,aliens,bullets):
    '''外星人与飞船碰撞时作出响应'''
    if stats.ship_left>0:
        stats.ship_left-=1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(set,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)  #暂停
    else:
        stats.game_active= False
        pygame.mouse.set_visible(True)

############################################################################################################################
def check_aliens_bottom(set,screen,stats,sb,ship,aliens,bullets):
    '''检查是否有alien到达screen的底部'''
    screen_rect=screen.get_rect()   #获取screen矩形
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(set,screen,stats,sb,ship,aliens,bullets)
            break


###########################################################################################################################
'''更新主屏幕'''
def update_screen(set,screen,stats,sb,ship,aliens,bullets,play_button):
    #重绘屏幕
    screen.fill(set.bg_color)
    #重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #重绘飞船
    ship.bl()
    #alien.bl()
    aliens.draw(screen)
    sb.show_score()

    #如果游戏处于非活动状态，就绘制按钮（stats.game_active的标志时刻控制着按钮是否会出现在主屏幕中）
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制屏幕可见
    pygame.display.flip()

def update_bullets(set,screen,stats,sb,ship,aliens,bullets):
    '''删除消失的子弹'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(set,screen,stats,sb,ship,aliens,bullets)

def update_aliens(set,screen,stats,sb,ship,aliens,bullets):
    '''更新外星人群中所有外星人位置'''
    check_fleet_edgs(set,aliens)
    aliens.update()
    #检查外星人和飞船间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens): #注意这里与同样是检查碰撞但与pygame.sprite.groupcollide（，）传的参数有点不同，重点是返回值也不同
        ship_hit(set,screen,stats,sb,ship,aliens,bullets)
    #检查是否有外星人到达屏幕底部
    check_aliens_bottom(set,screen,stats,sb,ship,aliens,bullets)