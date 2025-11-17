motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

#向列表中添加元素
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#向列表中插入元素
motorcycles.insert(0,'ducati')
print(motorcycles)

#对列表删除内容
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#从列表中弹出内容
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycles I owned was a {last_owned.title()}")

#使用pop()删除任意位置的元素
new_motorcycles=['honda','yamaha','suzuki']
first_owned = new_motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#根据值删除元素,remove只删除列表中的第一个值相等的元素
last_motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)