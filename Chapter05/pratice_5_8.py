user = ['tom','ltx','ali','admin','lily']
for item in user:
    if item == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {item},thank you for logging in again.")
