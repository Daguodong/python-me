import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    '''显示得分信息的类'''
    def __init__(self,set,screen,stats):
        '''初始化显示得分涉及的属性'''
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.set=set
        self.stats=stats

        #显示得分信息使用字体
        self.text_color=(255,158,53)
        self.font=pygame.font.Font('wd.ttf',38) #这里用的是系统字体，结合button理解

        #准备初始得分图像（包括最高分）
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分绘制成图'''
        rounded_score=round(self.stats.score)
        score_str='得分：{:,}'.format(rounded_score)  ####字符串的格式化用法（format）
        self.score_image=self.font.render(score_str,True,self.text_color,self.set.bg_color)

        #将得分绘制在screen的右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=0

    def prep_high_score(self):
        '''将最高得分转换成渲染图像'''
        high_score=round(self.stats.high_score)
        high_score_str="Baby！最高分:{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.set.bg_color)

        #将得分最高放在屏幕顶部
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.score_rect.top

    def prep_level(self):
        '''将等级转换为渲染图像'''
        level=self.stats.level
        level_str='等级：{:,}'.format(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,self.set.bg_color)
        #下面这一句与上面3句等效
        #self.level_image=self.font.render(('Baby！等级：{:,}'.format(self.stats.level)),True,self.text_color,self.set.bg_color)

        #将等级放在得分下方
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    def prep_ships(self):
        '''显示还剩下多少飞船'''
        self.ships=Group()
        for ship_number in range(self.stats.ship_left):
            ship=Ship(self.set,self.screen)
            ship.rect.x=ship_number*ship.rect.width
            ship.rect.y=0
            self.ships.add(ship)

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
