from pathlib import Path
import json

path = Path("./Chapter10/favorite_number.txt")
content = path.read_text()
number = json.loads(content)
if number:
    print(number)
else:
    favorite_number = input("Please Enter your favorite_number:")
    number_result =  json.dumps(favorite_number)
    path.write_text(number_result)