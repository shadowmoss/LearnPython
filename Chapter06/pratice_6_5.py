river = {
    'changjiang':'china',
    'laiyin':'german',
    'mohe':'heilongjiang'
}
for key,v in river.items():
    print(f"The {key} runs thoungh {v}")
for item in river.keys():
    print(item)
for country in river.values():
    print(country)