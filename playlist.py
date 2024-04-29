import track

class Playlist:
    def __init__(self,name):
        self.name = name
        self.head = None
        self.duration = 0

    #Methods for insertion
    def insert_at_beginning(self,name,album,length):
        # Insert a new Track at the beginning of the linked list
        # Time Complexity: O(1), Auxiliary Space: O(1)
        new_track = track.Track(name,album,length)
        self.duration+=new_track.length

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
        self.duration+=new_track.length

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
        self.duration+=new_track.length
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

        self.duration-=self.head.length
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
        if pos == 0:
            self.delete_at_beginning()
            return
        if not self.head:
            print(self.name,"is empty!")
            return
        if pos < 0:
            print("Invalid position")
            return
        
        current = self.head
        count = 0
        while count < pos - 1:
            # Traverse until the track before pos
            current = current.next
            count += 1

        self.duration-=current.next.length
        current.next = current.next.next
        current.next.prev = current

    def delete_at_end(self):
        #Delete track from end of playlist
        # Time Complexity: O(1), Auxiliary Space: O(1)
        if not self.head:
            print(self.name,"is empty!")
            return

        if self.head.next == self.head:
            self.duration-=self.head.length
            self.head = None
            return

        self.duration-=self.head.prev.length
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev

    def move(self,old_index,new_index):
        #Move track from old index to new index
        # Time Complexity: O(N) (actually O(old_index + new_index)), Auxiliary Space: O(1)
        if not self.head:
            print(self.name,"is empty!")
            return
        if old_index == new_index:
            return
        if old_index<0 or new_index<0:
            print("Invalid index")
            return
        
        current = self.head
        count = 0
        while count < old_index - 1:
            # Traverse until the track before pos
            current = current.next
            count += 1

        #Create a temp variable to hold the track
        to_move = current.next
        #Remove the links to the track at its old position
        current.next = current.next.next
        current.next.prev = current

        #Restart traversal to insert
        current = self.head
        count = 0
        while count < new_index - 1:
            # Traverse until the track before pos
            current = current.next
            count += 1

        #Insert track into its new positon
        to_move.next = current.next
        to_move.prev = current
        current.next.prev = to_move
        current.next = to_move

    def length(self):
        # Count how many tracks are in the playlist
        # Time Complexity: O(N), Auxiliary Space: O(1)
        if not self.head:
            print(self.name,"is empty")
            return
        
        current = self.head
        count=0
        while True:
            current = current.next
            count+=1
            if current == self.head:
                return count

    def contents(self):
        # Display the elements of the linked list
        # Time Complexity: O(N), Auxiliary Space: O(1)
        if not self.head:
            print(self.name,"is empty")
            return
        
        current = self.head
        count=0
        while True:
            print("Track",count,"->",current)
            print("Next track ->",current.next)
            print("Previous track ->",current.prev)
            print()
            current = current.next
            count+=1
            if current == self.head:
                return
            
    def clear(self):
        # Delete all of the entires in the playlist
        # Time Complexity: O(1), Auxiliary Space: O(1)
        self.head = None
        self.duration = 0

    def duration(self):
        # Find the total duration of all songs in the playlist
        # Time Complexity: O(1), Auxiliary Space: O(1)
        return self.duration
        
    def sort_by_album(self):
        #Sort the playlist by album titles in descending alphabetical order
        if not self.head:
            print(self.name," is empty!")
            return
        if not self.head.next == self.head:
            return

        #Bubble sort algorithm to sort tracks by album title
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next != self.head:
                next_track = current.next
                if current.album > next_track.album:
                    #Swap all track features to replace them
                    current.name, next_track.name = next_track.name, current.name
                    current.album, next_track.album = next_track.album, current.album
                    current.length, next_track.length = next_track.length, current.length
                    swapped = True
                current = current.next
                
    def sort_by_artist(self):
        #Sort the playlist by album titles in descending alphabetical order
        if not self.head:
            print(self.name," is empty!")
            return
        if not self.head.next == self.head:
            return

        #Bubble sort algorithm to sort tracks by album title
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next != self.head:
                next_track = current.next
                if current.name > next_track.name:
                    #Swap all track features to replace them
                    current.name, next_track.name = next_track.name, current.name
                    current.album, next_track.album = next_track.album, current.album
                    current.length, next_track.length = next_track.length, current.length
                    swapped = True
                current = current.next
                
    def sort_by_length(self):
        #Sort the playlist by album titles in descending alphabetical order
        if not self.head:
            print(self.name," is empty!")
            return
        if not self.head.next == self.head:
            return

        #Bubble sort algorithm to sort tracks by album title
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next != self.head:
                next_track = current.next
                if current.length > next_track.length:
                    #Swap all track features to replace them
                    current.name, next_track.name = next_track.name, current.name
                    current.album, next_track.album = next_track.album, current.album
                    current.length, next_track.length = next_track.length, current.length
                    swapped = True
                current = current.next

if __name__ == '__main__':
    playlist = Playlist("test_playlist")
    playlist.insert_at_beginning("artist1","album1",120)
    playlist.insert_at_end("artist3","album3",100)
    playlist.insert_at_index(1,"artist2","album2",210)
    playlist.insert_at_index(3,"artist4","album4",40)
    #artist1,artist2,artist3,artist4
    #playlist.contents()

    #playlist.delete_at_index(2)
    #artist1,artist2,artist4
    #playlist.contents()

    #print(playlist.length())
    #playlist.move(old_index=1,new_index=2)
    #artists1,artist4,artist2
    playlist.contents()

    print("Duration:",playlist.duration,"seconds")

    print("---------------------------")
    #playlist.clear()
    playlist.sort_by_length()
    playlist.contents()
    print("---------------------------")

    playlist.sort_by_artist()
    playlist.contents()
    print("---------------------------")

    playlist.sort_by_album()
    playlist.contents()