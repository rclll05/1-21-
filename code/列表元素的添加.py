a = [20,40]
a.append(80)
print(a)

a = [20,40]
print(id(a))
print(a)
a = a+[50]
print(id(a))
print(a)

a = [20,40]
print(id(a))
b=[50,60]
a.extend(b)
print(id(a))
print(a)
a = a+b
print(id(a))
print(a)

a = [10,20,30]
a.insert(2,100)
print(a)

a = ['sxt',100]
b = a*3
print(a)
print(b)