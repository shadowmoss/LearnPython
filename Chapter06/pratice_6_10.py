favorite_number = {
    "ltx":[7,9,36],
    "tom":[21,30,56],
    "alice":[2,4,6,8]
}
for key,value in favorite_number.items():
    print(f"{key} like numbers:")
    for number in value:
        print(f"{number}")