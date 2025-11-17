cars = ['bmw','audi','toyota','subaru']
# 永久排序,按字母顺序
cars.sort()
print(cars)
# 永久倒排,按字母顺序
cars.sort(reverse=True)
print(cars)
# 临时排序,按字母顺序
print(sorted(cars))
# 翻转当前列表
cars.reverse()
print(cars)
# 计算列表长度
print(len(cars))