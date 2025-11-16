first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" 
print(full_name)
print(f"Hello,{full_name.title()}!")
message = f"Hello,{full_name.title()}!"
print(message)
favorite_language = 'python '
print(favorite_language.rstrip()) # 删除字符串右端空格
left_language = '  python  '
print(left_language.lstrip()) # 删除字符串左端空格
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))