'''
类实例的属性和其对象的实例属性在不对对象的实例属性进行赋值时，指向
同一片内存

'''

class A():
    name = "aaa"
    age=17
    def say(self):
        self.name="666"
        self.age=200

#  A称为--类实例
print(A.name)
print(A.age)
print("*"*20)
print(id(A.name))   #1678811648104
print(id(A.age))    #1725066816
print("*"*20)

a=A()
print(a.name)
print(a.age)
print(id(a.name))    #1678811648104
print(id(a.age))     #1725066816
print("*"*20)
print(A.__dict__)
print(a.__dict__)
print("*"*20)
'''
如果对对象的实例进行赋值的话，则类实例属性和对象实力属性分别存储

'''
a.name="bianhua"
a.age="11"
print(a.__dict__)  #{'name': 'bianhua', 'age': '11'}
print(id(a.name))  #1820464169456
print(id(a.age))   #1820464169456