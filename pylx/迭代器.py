'''
迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器


'''

list=[1,2,3,4,]
it=iter(list)
print(next(it))  #1

print(next(it))  #2

print(next(it))  #3

for x in it:
    print (x, end=" ")  #4