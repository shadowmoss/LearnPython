players = ['charles','martina','michael','florence','eli']
print(players[0:3])
# 不指定起始索引,代码将从起始索引开始到指定结尾
print(players[:4])
# 不指定终止索引,代码将从指定的起始索引到达列表结尾
print(players[2:])
# 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())