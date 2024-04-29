import playlist

def tui_decorator(func):  
    def inner():  
        print("====================================\n")   
        func()  
        print("\n====================================")  
            
    return inner

@tui_decorator
def present_options():
    print("Type 1 to insert a track")
    print("Type 2 to delete a track")
    print("Type 3 to move a track")
    print("Type 4 to print the playlist")
    print("Type 5 to see the playlist length")

    print("\nType 0 to exit...")

    try:
        user_input = int(input("Enter your choice: "))
    except:
        print("Invalid input")
        return

    if user_input == 0:
        return
    primary_input_handler(user_input)

def primary_input_handler(user_input):
    match user_input:
        case 1:
            insertion_options()
        case 2:
            deletion_options()
        case 3:
            move_options()
        case 4:
            print_playlist()
        case 5:
            playlist_length()
        case _:
            print("Invalid input")
            
@tui_decorator
def insertion_options():
    print("Type 1 to insert at beginning")
    print("Type 2 to insert at end")
    print("Type 3 to insert at index")

    print("\nType 0 to exit...")

    try:
        user_input = int(input("Enter your choice: "))
    except:
        print("Invalid input")
        return

    match user_input:
        case 0:
            return
        case 1:
            insertion("start")
        case 2:
            insertion("end")
        case 3:
            try:
                index = int(input("Input an index to insert at: "))
                insertion(index)
            except:
                print("Invalid input")
                return
        case _:
            print("Invalid input")
        
def insertion(where):
    name = str(input("Input the song name: "))
    album = str(input("Input the album name: "))
    length = int(input("Input its duration: "))

    if where=="start":
        try:
            p.insert_at_beginning(name,album,length)
        except:
            print("Invalid inputs")
    elif where=="end":
        try:
            p.insert_at_end(name,album,length)
        except:
            print("Invalid inputs")
    else:
        try:
            p.insert_at_index(where,name,album,length)
        except:
            print("Invalid inputs")

    print_playlist()

@tui_decorator
def deletion_options():
    print("Type 1 to delete the beginning")
    print("Type 2 to delete the end")
    print("Type 3 to delete at index")

    print("\nType 0 to exit...")

    try:
        user_input = int(input("Enter your choice: "))
    except:
        print("Invalid Input")
        return

    match user_input:
        case 0:
            return
        case 1:
            deletion("start")
        case 2:
            deletion("end")
        case 3:
            index = int(input("Input an index to delete: "))
            deletion(index)
        case _:
            print("Invalid input")

def deletion(where):
    if where=="start":
        try:
            p.delete_at_beginning()
        except:
            print("Invalid inputs")
    elif where=="end":
        try:
            p.delete_at_end()
        except:
            print("Invalid inputs")
    else:
        try:
            p.delete_at_index(where)
        except:
            print("Invalid inputs")

    print_playlist()

@tui_decorator
def move_options():
    try:
        old_index = int(input("Type the old index of the track: "))
        new_index = int(input("Type the new index of the track: "))
    except:
        print("Invalid inputs")
        return

    p.move(old_index=old_index,new_index=new_index)
    print_playlist()

@tui_decorator
def print_playlist():
    p.contents()

@tui_decorator
def playlist_length():
    len = p.length()
    if len>0:
        print(p.name,"is",p.length(),"songs long")

if __name__ == '__main__':
    print("Welcome!")
    print("====================================\n")

    playlist_name = str(input("Name your playlist: "))
    p = playlist.Playlist(playlist_name)

    while True:
        present_options()
    
        inp = input("Press 0 to exit, or any other key to continue... -> ")

        if inp == "0":
            break

        

