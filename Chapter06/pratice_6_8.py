pet_1 = {
    "name":"lucy",
    "age":2,
    "owner":"ltx"
}
pet_2 = {
    "name":"lily",
    "age":3,
    "owner":"ana"
}
pet_3 = {
    "name":"lu",
    "age":4,
    "owner":"andy"
}
pets = [pet_1,pet_2,pet_3]
for item in pets:
    print(f"name:{item["name"]},age:{item["age"]},owner:{item["owner"]}")