favorite_language={
    "ltx":"c",
    "tom":"c++",
    "lily":"python",
    "ana":"java"
}
check = ['ltx','tom']
for name in favorite_language.keys():
    if name in check:
        print("Thank you,join our check action")
    else:
        print("Hope you can join us")