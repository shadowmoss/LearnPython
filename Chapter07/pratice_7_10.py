prompt = "If you could visit one place in the world,where would you go?"
visit_place = []
while True:
    place = input(prompt)
    visit_place.append(place)
    message = input("Have you have other place to go?(yes/no)")
    if message == 'no':
        break
print("follow list is the place you want to go:")
print(visit_place)