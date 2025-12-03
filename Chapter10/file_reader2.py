from pathlib import Path

path = Path('./Chapter10/pi_digits.txt')
contents = path.read_text()

# 读取每一行
lines = contents.splitlines()
for line in lines:
    print(line)