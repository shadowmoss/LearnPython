foods = ['pizza','falafel','carrot cake','cannoli']
print("The first three items in the list are:")
for food in foods[:3]:
    print(food)
print('The items from the middle of the list are:')
for food in foods[1:3]:
    print(food)
print('The last three items in the list are:')
for food in foods[-3:]:
    print(food)