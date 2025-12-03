from pathlib import Path
import json

path = Path("./Chapter10/remeberme.txt")
user_info = {
    "username":'',
    "age":0,
    "gender":""
}
user_info["username"] = input("Please Enter your name:")
user_info["age"] = input("Please Enter your age:")
user_info["gender"] = input("Please Enter your gender:")
info = json.dumps(user_info)
path.write_text(info)