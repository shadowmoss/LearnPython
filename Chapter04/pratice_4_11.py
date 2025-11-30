pizza = ['pizza','falafel','carrot cake']
friend_pizza = pizza[:]

pizza.append('polo')
friend_pizza.append('orange')
print('My favorite pizzas are:')
for first in pizza:
    print(first)
print("My friend's favorite pizzas are:")
for friend in friend_pizza:
    print(friend)