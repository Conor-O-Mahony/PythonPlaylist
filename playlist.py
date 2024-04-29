import track

class Playlist:
    def __init__(self,name):
        self.name = name

        self.head = None

    #Methods for insertion
    def insert_at_beginning(self,name,album,length):
        # Insert a new Track at the beginning of the linked list
        # Time Complexity: O(1), Auxiliary Space: O(1)
        new_track = track.Track(name,album,length)

        if not self.head:
            new_track.next = new_track
            new_track.prev = new_track
        else:
            new_track.next = self.head
            new_track.prev = self.head.prev
            self.head.prev.next = new_track
            self.head.prev = new_track
        self.head = new_track

    def insert_at_end(self,name,album,length):
        # Append a new Track at the end of the linked list
        # Time Complexity: O(1), Auxiliary Space: O(1)
        new_track = track.Track(name,album,length)

        if not self.head:
            new_track.next = new_track
            new_track.prev = new_track
        else:
            new_track.next = self.head
            new_track.prev = self.head.prev
            self.head.prev.next = new_track #new_track.next.prev = new_track #?????
            self.head.prev = new_track

    def insert_at_index(self,pos,name,album,length):
        # Insert a new track at the specified index
        # Time Complexity: O(N), Auxiliary Space: O(1)
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(name,album,length)
            return
        
        new_track = track.Track(name,album,length)
        current = self.head
        count = 0
        while count < pos - 1:
            # Traverse until the track before pos
            current = current.next
            count += 1

        # Insert the new node at the specified position
        new_track.next = current.next
        new_track.prev = current
        current.next.prev = new_track
        current.next = new_track

    #Methods for deletion
    def delete_at_beginning(self):
        #Delete track from beginning of the playlist
        # Time Complexity: O(1), Auxiliary Space: O(1)
        if not self.head:
            print(self.name," is empty!")
            return

        # If only one node in list
        if self.head.next == self.head:
            self.head = None
            return

        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next

    def delete_at_index(self, pos):
        #Delete track at the specified pos
        # Time Complexity: O(N), Auxiliary Space: O(1)
        if not self.head:
            print(self.name,"is empty!")
            return
        if pos < 0:
            print("Invalid position")
            return

        # Deleting the head node
        if pos == 0:
            self.delete_at_beginning()
            return
        current = self.head
        count = 0
        while count < pos - 1:
            # Traverse until the track before pos
            current = current.next
            count += 1

        current.next = current.next.next
        current.next.next = current.prev

    def delete_at_end(self):
        #Delete track from end of playlist
        # Time Complexity: O(1), Auxiliary Space: O(1)
        if not self.head:
            print("Playlist is empty!")
            return

        if self.head.next == self.head:
            self.head = None
            return

        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev
        
    def contents(self):
        # Display the elements of the linked list
        # Time Complexity: O(N), Auxiliary Space: O(1)
        current = self.head
        count=0
        if not self.head:
            print(self.name,"is empty")
            return
        while True:
            print("Track",count,"->",current)
            print("Next track ->",current.next)
            print("Previous track ->",current.prev)
            print()
            current = current.next
            count+=1
            if current == self.head:
                return

if __name__ == '__main__':
    playlist = Playlist("test_playlist")
    playlist.insert_at_beginning("artist1","album1",120)
    playlist.insert_at_end("artist3","album3",100)
    playlist.insert_at_index(1,"artist2","album2",210)
    playlist.insert_at_index(3,"artist4","album4",40)

    playlist.delete_at_index(2)
    playlist.contents()