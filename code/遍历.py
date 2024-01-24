a = [20,10,30,40]
for temp in a:
    print(temp*100)

list1 = [30,40,50]
#list2 = list1  地址不变 还是原对象
list2 = [] + list1  #产生新对象
print(id(list1))
print(id(list2))