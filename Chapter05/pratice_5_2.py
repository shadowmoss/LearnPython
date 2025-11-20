str1 = "equals"
str2 = "equals"
print("Is str1 == str2 ? I predict True")
print(str1 == str2)
str3 = "Name_Test"
str4 = "Name_test"
print("Is str3 == str4.lower()? I predict False")
print(str3 == str4.lower())
number1 = 100
number2 = 200
print("Is number1 < number2? I predict True")
print(number1 < number2)
number3 = 300
number4 = 300
print("Is number3 == number4? I predict True")
print(number3 == number4)
number5 = 400
number6 = 500
print("Is number6 > number5? I predict True ")
print(number6 > number5)
number7 = 700
number8 = 800
number9 = 900
number10 = 1000
print("Is number7 < number8 and number10 > number9?I predict True")
print(number7 < number8 and number10 > number9)
name_list = ['ltx','tom','candy','casy']
if 'ltx' in name_list:
    print('ltx is find')
if 'ready' not in name_list:
    print('ready is not in name_list')