import pygame.font
class Button():
    def __init__(self,set,screen,msg):
        '''初始化按钮'''
        self.screen=screen
        self.screen_rect=screen.get_rect()

        '''设置按钮尺寸大小和其他属性'''
        self.width,self.height=300,90 #按钮尺寸，这里要注意文本的尺寸应小于按钮的，否则界面不美观
        self.button_color=(255,158,53) #按钮颜色
        self.text_color=(255,255,255) #文本颜色
        #self.font=pygame.font.SysFont(None,48)  #!!!!这句话与下面一句话的差别就是本句话不支持中文，下面支持中文，注意理解观察其不同之处
        self.font=pygame.font.Font('wd2.ttf',48)  #如何输出汉字

        '''创建按钮，使其居中'''
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)#单独处理文本

    def prep_msg(self,msg):
        '''将msg渲染为图像，使其在按钮上居中'''
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color) #实现把文本转化成图像，并绘制在主屏幕上
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        '''绘制按钮，文本'''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

''''
#打印出系统字体类型
#print (pygame.font.get_fonts())
ZiTi=pygame.font.get_fonts()

for i in ZiTi:
   print(i)
'''