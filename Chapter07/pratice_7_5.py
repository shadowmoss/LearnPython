prompt = "\nPlease Enter serise pizza recipe:"
prompt += "\n(Enter 'quit' quit the System)"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"Add {message} in pizza.")