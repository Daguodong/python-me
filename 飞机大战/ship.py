import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,set,screen):
        super().__init__()
        '''初始化飞船位置'''
        self.screen=screen
        self.set=set
        #加载ship
        self.image=pygame.image.load('images/ship.jpg')
        self.rect=self.image.get_rect() #获取ship矩形
        self.screen_rect=screen.get_rect() #获取screen矩形
        #把ship放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #把飞船属性更新为小数值
        self.center=float(self.rect.centerx)
        self.center1=float(self.rect.bottom)
        #移动标志
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        '''根据移动调整飞船位置'''
        if self.moving_up and self.rect.top>0:
            self.center1-=self.set.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.center1+=self.set.ship_speed_factor
        if self.moving_right and self.rect.right<self.screen_rect.right+80:  #保证右移动时，子弹可以打到最右边的边界
            self.center+=self.set.ship_speed_factor
        if self.moving_left and self.rect.left>-53: #保证左移动时，子弹可以打到最左边的边界
            self.center-=self.set.ship_speed_factor
        #运行这句代码，才实际上更新飞船位置，
        self.rect.centerx=self.center
        self.rect.bottom=self.center1

    def bl(self):
        self.screen.blit(self.image,self.rect)#绘出ship在screen上

    def center_ship(self):
        '''
        #以下两句有很强的逻辑，注意只能用self.center/self.center1 而不能用self.rect.centerx/self.rect.bottom
        #前一组用于每次更新ship的位置，后一组用于最初"绘制"ship
        '''
        self.center=self.screen_rect.centerx
        self.center1 = self.screen_rect.bottom