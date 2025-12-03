while True:
    try:
        first_number = input("Please Enter first_number:")
        if first_number == 'q':
            break
        second_number = input("Please Enter second_number:")
        if second_number == 'q':
            break
        sum_result = int(first_number) + int(second_number)
    except ValueError:
        print("we got a ValueError")
    print(f"sum_result:{sum_result}")