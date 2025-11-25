def car_info(manufactory,factorinfo,**car_profile):
    car_profile['manufactory'] = manufactory
    car_profile['factorinfo'] = factorinfo
    return car_profile
car = car_info("一汽","座椅通风",long=2.13,power='2.0T')
print(car)