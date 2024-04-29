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
        new_track.next = self.head
        self.head = new_track

    def insert_at_end(self,name,album,length):
        # Append a new Track at the end of the linked list
        # Time Complexity: O(N), Auxiliary Space: O(1)
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

    #Methods for deletion
    def delete_at_beginning(self):
        # Time Complexity: O(1), Auxiliary Space: O(1)
        if not self.head:
            print(self.name," is empty!")
            return

        # If only one node in list
        if self.head.next == self.head:
            self.head = None
            return

        current = self.head
        while current.next != self.head:
            current = current.next
            
        # Make last track point to second
        current.next = self.head.next
        
        # Point head to second track
        self.head = self.head.next

    def delete_at_position(self, pos):
        #Delete track at the specified pos
        if not self.head:
            print("Playlist is empty!")
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
        while count < pos - 1 and current.next != self.head:
            current = current.next
            count += 1
        if count < pos - 1:
            print("Index out of range")
            return
        current.next = current.next.next

    def delete_at_end(self):
        #Delete track from end of playlist
        if not self.head:
            print("Playlist is empty!")
            return
        current = self.head
        while current.next and current.next != self.head:
            # Traverse until last node
            current = current.next
        #FINISH THIS METHOD
        
    def contents(self):
        # Display the elements of the linked list
        current = self.head
        count=0
        while current:
            print("Track",count,"->",current)
            current = current.next
            count+=1

if __name__ == '__main__':
    playlist = Playlist("test_playlist")
    playlist.insert_at_beginning("artist1","album1",120)
    playlist.insert_at_end("artist2","album2",100)
    playlist.insert_at_index(1,"artist3","album3",210)
    playlist.insert_at_index(3,"artist4","album4",40)
    playlist.contents()