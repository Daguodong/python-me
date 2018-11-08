'''

类和对象的概念
  类：抽象名词，代表一个集合，共性的事物
  对象：具象的事物，单个个体
类跟对象的关系
   1，一个具象，代表一类事物的某一个个体
   2，一个是抽象，代表的是一大类事物
类中的内容，应该具有两个内容
   1，表明事物的特征，叫做属性(变量)--成员
   2，表明事物功能或动作， 称为成员方法(函数)

   定义一个学生类
'''


class Student():
    name=None   # # 用None给不确定的值赋值
    age=17
    course="deeplearning"
    #以上可以理解为类的成员

    def xuexi(self):   #定义成员方法，注意缩进
        print("好好学习，天天向上")


#实例化一个叫guodong的学生
guodong=Student()
#访问对象成员
print(guodong.name)
print(guodong.course)
guodong.xuexi()