from Song import Song
from Library import Library
from Never_gonna_give_you_up import Never_gonna_give_you_up

menu = Song()
Rick = Never_gonna_give_you_up()
while True:
    print("Enter command: ")
    command = input()
    if command == 'exit':
        print("Bye little rockstar")
        break
    elif command == "Rick":
        Rick.Rick()
    elif command == 'add':
        print("Enter song name:")
        name = input()
        print("Enter author:")
        author = input()
        print("Enter year:")
        year = int(input())
        print("Enter album:")
        album = input()
        Library = Library(name, author, year, album)
        menu.addSong(Library)
    elif command == 'delete':
        print("Enter name:")
        name = input()
        menu.deleteSong(name)
    elif command == 'print':
        menu.printLibrary()
    elif command == 'Find':
        name = input("Enter name:\n")
        if menu.isSongExists(name) == False:
            print("Is no song like this")
        else:
            The_song = menu.isSongExists(name)
            print(f' This song:'
                  f'{str(The_song.name)}\n'
                  f'   author: {The_song.author}\n'
                  f'   year: {The_song.year}\n'
                  f'   album: {The_song.album}')
    else:
        print("If you see this, I am disappointed in you(")
