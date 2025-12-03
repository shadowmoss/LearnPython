from pathlib import Path

path = Path("./Chapter10/Python_Learn.txt")
content = path.read_text()
lines = content.splitlines()
for line in lines:
    print(line.replace("Python","CSharp"))