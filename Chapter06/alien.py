alien_0={'color':'green',"points":5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 从空字典开始创建字典
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

# 删除字典中不需要的字段
alien_2 = {'color':'green','points':5}
del alien_2['points']
print(alien_2)
# get()方法来访问字典内的值，防止访问出错