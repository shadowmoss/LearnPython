from pathlib import Path

path = Path('./Chapter10/Python_Learn.txt')
for item in path.read_text().splitlines():
    print(item)
