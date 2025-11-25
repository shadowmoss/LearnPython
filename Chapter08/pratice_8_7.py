def make_album(singer,album_name):
    album = {"singer":singer,"album_name":album_name}
    return album
album_one = make_album("Jackson","Beat It")
album_two = make_album("TaoZhe","David Tao")
album_three = make_album("Pink Floyd","The Dark Side of the moon")
print(album_one)
print(album_two)
print(album_three)