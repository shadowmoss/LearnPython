sandwich_orders=["hambager","sara","spicy"]
finished_sandwiches=[]
while sandwich_orders:
    move_sandwich = sandwich_orders.pop()
    print(f"I made your {move_sandwich}")
    finished_sandwiches.append(move_sandwich)