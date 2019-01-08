import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):    #继承模块pygame.sprite中的Sprite类,这样可以编组，可同时操作编组中的所有元素
    '''管理飞船发射子弹的类'''
    def __init__(self,set,screen,ship):
        '''创建子弹对象'''
        super(Bullet,self).__init__()
        self.screen=screen
        #(0,0)处创建一个子弹矩形，并更正其位置
        self.rect=pygame.Rect(0,0,set.bullet_width,set.bullet_height) #注意理解这句代码
        self.rect.centerx=ship.rect.centerx-15
        self.rect.top=ship.rect.top

        self.y=float(self.rect.y)

        self.color=set.bullet_color
        self.speed_factor=set.bullet_speed_factor
        #self.fase=False

    def update(self):
        #if self.fase:
            '''上移子弹'''
            #类似于ship改变
            self.y-=self.speed_factor
            self.rect.y=self.y

    def draw_bullet(self):
        '''在屏幕上绘出子弹bullet'''
        pygame.draw.rect(self.screen,self.color,self.rect)