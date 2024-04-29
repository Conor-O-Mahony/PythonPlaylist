import track

class Playlist:
    def __init__(self,name):
        self.name = name

        self.head = None

    def insert_at_beginning(self,name,album,length):
        # Insert a new Track at the beginning of the linked list
        new_track = track.Track(name,album,length)
        new_track.next = self.head
        self.head = new_track

    def insert_at_end(self,name,album,length):
        # Append a new Track at the end of the linked list
        new_track = track.Track(name,album,length)
        if not self.head:
            #Linked list empty
            self.head = new_track
            return
        current = self.head
        while current.next:
            # Traverse until last node
            current = current.next
        current.next = new_track

    def insert_at_index(self,pos,name,album,length):
        # Insert a new node with data at the specified position in the linked list
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(name,album,length)
            return
        new_track = track.Track(name,album,length)
        current = self.head
        count = 0
        while count < pos - 1 and current:
            # Traverse until the track before pos
            current = current.next
            count += 1
        if not current:
            # If the pos out of range
            print("Position out of range")
            return
        # Insert the new node at the specified position
        new_track.next = current.next
        current.next = new_track

    def contents(self):
        # Display the elements of the linked list
        current = self.head
        i=0
        while current:
            print("Track",i,"->",current)
            current = current.next
            i+=1

if __name__ == '__main__':
    playlist = Playlist("test_playlist")
    playlist.insert_at_beginning("artist1","album1",120)
    playlist.insert_at_end("artist2","album2",100)
    playlist.insert_at_index(1,"artist3","album3",210)
    playlist.insert_at_index(3,"artist4","album4",40)
    playlist.contents()