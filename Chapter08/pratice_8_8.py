def make_album(singer,album_name):
    album = {"singer":singer,"album_name":album_name}
    return album
while True:
    print("\nPlease enter the singer and album_name")
    singer = input("singer = ")
    if singer == 'q':
        break
    album_name = input("album_name = ")
    if album_name == 'q':
        break
    album =  make_album(singer,album_name)
    print(album)
