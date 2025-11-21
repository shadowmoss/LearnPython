prompt = "\nPlease Enter serise pizza recipe:"
prompt += "\n(Enter 'quit' quit the System)"
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"Add {message} in pizza.")