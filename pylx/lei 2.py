'''
成员函数里的self不是关键字，只是一个用于接受对象的普通参数，
理论上可以用任何一个普通变量名代替可通过下面代码验证
'''
class Student():
    name = "dana"
    age=38

    def say(self):
        self.name="aaa"
        self.age=200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def do(s):
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))

xiaode=Student()
xiaode.say()
xiaode.do()
'''
上面代码输出为
My name is aaa
My age is 200
My name is aaa
My age is 200
'''
class teacher():
    name="jk"
    age=9

    def do(self):
        self.age=8
        self.name="xg"
        print("my name is {0}".format(self.name))
        #调用父类成员变量的格式为__class__
        print("my age is {0}".format(__class__.age))


    def doagain():
        print(__class__.name)
        print(__class__.age)

t=teacher()
t.do()
#调用没有（self）的类
teacher.doagain()

'''
关于self的举例
'''


class A():
    name = " li"
    age = 18

    def __init__(self):
        self.name = "aaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbb"
    age = 90
a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()
# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)
# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

# 以上代码，利用了鸭子模型