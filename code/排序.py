import random

a = [20,10,30,40]
print(a)

a.sort()   #升序
print(a)

a.sort(reverse=True) #降序
print(a)

random.shuffle(a) #打乱
print(a)


x = [20,10,30,40]   #以下是建新的列表排序
y = sorted(a)
z = sorted(a,reverse=True)
print(x)
print(y)
print(z)
print(sum(x))
print(max(x))
print(min(y))

