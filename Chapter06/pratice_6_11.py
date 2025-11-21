cities = {
    "changjiang":{
        "country":"china",
        "population":14,
        "description":"5000 years country"
    },
    "tokoyo":{
        "country":"japan",
        "population":3,
        "description":"asia financial point"
    },
    "London":{
        "country":"England",
        "population":4,
        "description":"Britsh capital"
    }
}
for city,value in cities.items():
    print(f"city_name:{city}")
    for key,info in value.items():{
        print(f"{key}:{info}")
    }
