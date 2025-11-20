user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
# 遍历字典中的键和值
for key,v in user_0.items():
    print(f"Key: {key}")
    print(f"value : {v}\n")
# 遍历字典中的所有键
for key in user_0.keys():
    print(key.title())

# 遍历字典中的所有值
for value in user_0.values():
    print(value.title())