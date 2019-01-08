'''设置这个游戏'''
class Settings():
    '''初始化游戏设置'''
    def __init__(self):
        '''静态设置'''
        ##屏幕screen设置
        self.screen_width=1200
        self.screen_height=900
        self.bg_color=(255,255,255)
        ##飞船ship设置
        #self.ship_speed_factor=3.5
        self.ship_limit=3   #飞船生命限制
        ##子弹bullet设置
        #self.bullet_speed_factor=1.5
        self.bullet_width=40
        self.bullet_height=20
        self.bullet_color=(255,158,53)  #橘黄色的RGB值
        #self.bullets_allowed=3,这句用于限定子弹数，结合game_functionS.py中的函数check_kdown_events（）使用
        ##alien设置
        self.fleet_drop_speed = 10
        #self.alien_speed_factor=0.5
        self.speedup_scale=1.1 #以什么样的速度加快游戏节奏
        self.score_scale=1.5
        #self.fleet_direction=1 #本句控制方向，1代表右移，-1代表左移

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''动态设置'''
        self.ship_speed_factor = 3.5
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 0.5
        self.fleet_direction = 1  # 本句控制方向，1代表右移，-1代表左移
        #记分
        self.alien_points=10 #消灭一个外星人的得分

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale

        self.alien_points=(self.alien_points*self.score_scale)