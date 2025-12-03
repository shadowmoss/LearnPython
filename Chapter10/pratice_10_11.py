from pathlib import Path
import json
path = Path("./Chapter10/favorite_number.txt")
favorite_number = input("Enter your favorite_number:")
content = json.dumps(favorite_number)
path.write_text(content)