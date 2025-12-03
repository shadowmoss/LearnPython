from pathlib import Path

path = Path("./Chapter10/cats.txt")
dogPath = Path("./Chapter10/dogs.txt")
try:
    catContent = path.read_text()
    dogContent = dogPath.read_text()
    print(catContent)
    print(dogContent)
except FileNotFoundError:
    pass