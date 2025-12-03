from pathlib import Path

path = Path("./Chapter10/Python_Learn.txt")
content = path.read_text()
print(content)
lines = content.splitlines()
line_Content = []
for line in lines:
    line_Content.append(line)

for item in line_Content:
    print(item)