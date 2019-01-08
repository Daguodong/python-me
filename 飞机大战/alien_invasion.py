'''

项目名称：打飞机游戏

工作记录：
        第一次    -----时间：2018年12月16日                    ||||   作者：郭祥栋
        第二次修改-----时间：2018年12月17日17:46:33            ||||   作者：郭祥栋                |||||||  代码量：共198行
        第三次修改-----时间：2018年12月17日22:47:00            ||||   作者：郭祥栋                |||||||  代码量：共279行
        第四次修改-----时间：2018年12月18日21:58:35            ||||   作者：郭祥栋                |||||||  代码量：共288行
        第五次修改-----时间：2018年12月24日16:52:07            \\\\   作者：郭祥栋                \\\\\\\  代码量：共329行
        第六次修改-----时间：2018年12月31日21:52:34            \\\\   作者：郭祥栋                \\\\\\\  代码量：共393行
        第七次修改-----时间：2019年 1月 3日22:19:29            \\\\   作者：郭祥栋                \\\\\\\  代码量：共535行
        第八次修改-----时间：2019年 1月 5日16:50:28            \\\\   作者：郭祥栋                \\\\\\\  代码量：共581行

'''
#import sys
#import local2utf8
import pygame
from setting import Settings
from ship import Ship
import game_functionS as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from alien import Alien


def run_game():
    #初始化游戏并创建一个屏幕
    pygame.init()
    set=Settings()
    screen=pygame.display.set_mode((set.screen_width,set.screen_height))
    #pygame.display.set_caption((u'宝贝看--这是飞机大战').encode('utf-8'))#此处没有结决
    pygame.display.set_caption('**宝贝看--这是飞机大战！**')
    play_button=Button(set,screen,'@我，嘿嘿！')
    stats=GameStats(set)
    sb=Scoreboard(set,screen,stats)
    ship=Ship(set,screen)
    #创建一个存储子弹的编组,
    bullets=Group()
    aliens=Group()
    #alien=Alien(set,screen)
    gf.create_fleet(set,screen,ship,aliens)


    #开始游戏主循环
    while True:
        gf.check_events(set,screen,stats,sb,play_button,ship,aliens,bullets) # !!!注意这个实参传入顺序，以此顺序为准
        if stats.game_active:
            ship.update()

            gf.update_bullets(set,screen,stats,sb,ship,aliens,bullets)    #先更新子弹bullet后更新alien，因为外星人被打落（结合：sprite.groupcollide()检测 理解）
            gf.update_aliens(set,screen,stats,sb,ship,aliens,bullets)

        '''
        bullets.update()
        #删除消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
        #print(len(bullets)),这句话检查消失子弹是否被移除，测试成功后，应立即删除，此处把它注释了，因为如果保留这句话将会影响游戏速度
        '''
        gf.update_screen(set,screen,stats,sb,ship,aliens,bullets,play_button)
        '''
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(set.bg_color)
        ship.bl()
        pygame.display.flip()
        
        '''
run_game()