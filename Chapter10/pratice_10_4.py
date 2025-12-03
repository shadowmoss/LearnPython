from pathlib import Path

path = Path("./Chapter10/guest.txt")
message = input("Please Enter you name:")

path.write_text(message)