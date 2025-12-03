from pathlib import Path

path = Path("./Chapter10/guest_book.txt")
guest_list = ""
while True:

    guest_name = input("Enter the guest name:")

    if guest_name == 'q':
        break
    guest_list += guest_name+"\n"

path.write_text(guest_list)