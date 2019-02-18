'''
           这是一个关于python类的demo,包含了类的定义、实例的创建、使用类和实例、修改类属性值、
           类的继承、类中将类实例赋予类属性等等.........

           理清逻辑关系，相信关于类今后你一定可以轻松解决

           那么现在开始享受你的编程吧！！！！！
'''

class Car():
    '''一次模拟汽车的简单实验'''
    def __init__(self,make,model,year):
        self.model=model
        self.year=year
        self.make=make
        self.odmeter_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year) + ' '+ self.make + ' '+ self.model
        return long_name.title()

    def read_odometer(self):
        print('this car  has '+str(self.odmeter_reading)+' miles')

    def update_odometer(self,mileage):
        if mileage>=self.odmeter_reading:
            self.odmeter_reading=mileage
        else:
            print("you can't  roll back an odometer!")

    def increment_odometer(self,miles):
        self.odmeter_reading+=miles


class Battery():
    '''初始化电瓶属性'''
    def __init__(self,battery_size=70):
        '''初始化电瓶属性'''
        self.battery_size=battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的信息'''
        print('this car has a '+str(self.battery_size)+"-kwh battery.")


class ElecticCar(Car):  #继承
    '''电动汽车的独特之处'''
    def __init__(self,make,model,year):
        '''初始化父类的属性，在初始化电动汽车的属性'''
        super().__init__(make,model,year)
        self.battery=Battery(500)     #将实类用作属性，注意由第35-39句知：battery=Battery()，然后:self.battery=battery


my_audi=ElecticCar("audi","A8",2016)
print(my_audi.get_descriptive_name())
my_audi.update_odometer(25)
my_audi.read_odometer()  #第一次读取里程
my_audi.increment_odometer(50)
my_audi.read_odometer()  #第二次读取里程
my_audi.update_odometer(50)
my_audi.battery.describe_battery()  #注意调用格式，以及运行顺序


'''输出为：

           C:\ProgramData\Anaconda3\python.exe D:/pycharm项目/类/lei3.py
            2016 Audi A8
            this car  has 25 miles
            this car  has 75 miles
            you can't  roll back an odometer!
            this car has a 500-kwh battery.
            
            进程已结束，退出代码 0


'''