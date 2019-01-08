import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''外星人类'''
    def __init__(self,set,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.set=set

        #加载外星人，并设置其rect属性
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()

        #放在screen的左上角附近，不是正好的左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)

    def check_edges(self):
        '''若有外星人移到屏幕边缘，返回True'''
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True

    def update(self, *args):
        '''左移或右移alien'''
        self.x+=(self.set.alien_speed_factor*self.set.fleet_direction)
        self.rect.x=self.x

    def bl(self):
        self.screen.blit(self.image,self.rect)