a = [100,200,888,300,400,888]
del a[2]
print(a)

a = [100,200,888,300,400,888]
a.pop(2)
#a.pop() 默认删除最后一个
print(a)

a = [100,200,888,300,400,888]
a.remove(888)   #删除指定的值
#a.remove(88888)  报错
print(a)
