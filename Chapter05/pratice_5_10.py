current_users = ["tom","ltx","alice","lily","admin"]
new_users = ["tom","ltx","ana","topson",'yatoro']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is already in use")
    else:
        print(f"{new_user} isn't being use")
