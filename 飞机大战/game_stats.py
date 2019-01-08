class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self,set):
        '''初始化统计信息'''
        self.set=set
        self.rest_stats()
        self.game_active=False
        self.high_score=0 #用来保存游戏最高分，并且任何情况下都不更新,除非重启游戏

    def rest_stats(self):
        self.ship_left=self.set.ship_limit  #存储可用的生命也就是飞船的数量
        self.score=0
        self.level=1