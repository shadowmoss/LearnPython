def send_message(messages,sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
    return sent_messages
messages = ["hello","world","bind"]
sent_messages = []
send_message(messages,sent_messages)
print(sent_messages)