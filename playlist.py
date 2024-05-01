from track import Track
from random import randint

class Playlist:
    def __init__(self,name):
        self.name = name
        self.head = None
        self.duration = 0
        self.length = 0

    def traverse(self,i):
        # Efficient traversal to index i. Takes advantage of circularity and doubly linked nature
        # Time Complexity: O(min(i,N-i)), Auxiliary Space: O(1)
        count = 0
        if i>(self.length//2):
            current = self.head.prev
            while count<(self.length-i-1):
                current = current.prev
                count+=1
        else:
            current = self.head
            while count<i:
                current = current.next
                count+=1

        return current

    #Methods for insertion
    def insert_at_beginning(self,name,album,length):
        # Insert a new Track at the beginning of the linked list
        # Time Complexity: O(1), Auxiliary Space: O(1)
        new_track = Track(name,album,length)
        self.duration+=new_track.length
        self.length+=1

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
        # Append a new Track at the end of the linked list. Can use insert_at_beginning, then move head forward 1
        # Time Complexity: O(1), Auxiliary Space: O(1)
        self.insert_at_beginning(name,album,length)
        self.head = self.head.next

    def insert_at_index(self,pos,name,album,length):
        # Insert a new track at the specified positive index
        # Time Complexity: O(min(i,N-i)), Auxiliary Space: O(1)
        if pos < 0 or pos > self.length:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_beginning(name,album,length)
            return
        if pos == self.length:
            self.insert_at_end(name,album,length)
            return
        
        new_track = Track(name,album,length)
        self.duration+=new_track.length
        self.length+=1

        # Traverse to the specified position
        current = self.traverse(pos)

        # Insert the new node at the specified position
        new_track.next = current
        new_track.prev = current.prev
        current.prev.next = new_track
        current.prev = new_track

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
        
        self.duration-=self.head.length
        self.length-=1
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next

    def delete_at_index(self, pos):
        #Delete track at the specified pos
        # Time Complexity: O(N), Auxiliary Space: O(1)
        if pos == 0:
            self.delete_at_beginning()
            return
        if pos == self.length - 1:
            self.delete_at_end()
            return
        if pos < 0 or pos > self.length - 1:
            print("Invalid position")
            return
        if not self.head:
            print(self.name,"is empty!")
            return
        
        self.duration-=current.next.length
        self.length-=1

        #Traverse to the node to be deleted
        current = self.traverse(pos)

        #Link current.next and current.prev to eachother
        current.prev.next = current.next
        current.next.prev = current.prev

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
        self.length-=1
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev

    def move(self,old_index,new_index):
        #Move track from old index to new index
        # Time Complexity: O(N), Auxiliary Space: O(1)
        #Future consideration: It possible that the new and old index are close and so we don't have to traverse
        #from head to index both times. In this case, traverse to the closest index first, then from there to the
        #new index.
        if not self.head:
            print(self.name,"is empty!")
            return
        if old_index == new_index:
            return
        if old_index<0 or new_index<0 or old_index>self.length-1 or new_index>self.length-1:
            print("Invalid index")
            return
        
        #Fetch the track at the old index
        to_move = self.traverse(old_index)

        #Remove links to the track at old index
        to_move.prev.next = to_move.next
        to_move.next.prev = to_move.prev

        #If moving the track to the beginning
        if new_index == 0:
            to_move.next = self.head
            to_move.prev = self.head.prev
            self.head.prev.next = to_move
            self.head.prev = to_move
            self.head = to_move
            return
        #If moving the track to the end
        if new_index == self.length-1:
            to_move.next = self.head
            to_move.prev = self.head.prev
            self.head.prev.next = to_move
            self.head.prev = to_move
            return

        #Decrement the length to traverse properly
        self.length-=1

        #Fetch the track at the new index
        move_to = self.traverse(new_index)

        #Insert the track at the new index
        to_move.next = move_to
        to_move.prev = move_to.prev
        move_to.prev.next = to_move
        move_to.prev = to_move

        #Re-increment the length
        self.length+=1

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
            #print("Next track ->",current.next)
            #print("Previous track ->",current.prev)
            current = current.next
            count+=1
            if current == self.head:
                return
            print()
            
    def clear(self):
        # Delete all of the entires in the playlist
        # Time Complexity: O(1), Auxiliary Space: O(1)
        self.head = None
        self.duration = 0
        self.length = 0
        
    def sort_by_album(self):
        #Sort the playlist by album titles in descending alphabetical order
        if not self.head:
            print(self.name," is empty!")
            return
        if self.head.next == self.head:
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
        #Sort the playlist by song name in descending alphabetical order
        if not self.head:
            print(self.name," is empty!")
            return
        if self.head.next == self.head:
            return

        #Bubble sort algorithm to sort tracks by song name
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
        #Sort the playlist by length in descending alphabetical order
        if not self.head:
            print(self.name," is empty!")
            return
        if not self.head.next == self.head:
            return

        #Bubble sort algorithm to sort tracks by length
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
                
    def now_playing(self):
        if not self.head:
            print(self.name, " is empty!")
            return
        current = self.head
        print("Now Playing:", current.name, "from the album", current.album)
        print("             Remaining track time is:", current.length, "seconds.")

    def old_shuffle(self):
        # Fisher-Yates-like Shuffle Algorithm for Circular Doubly Linked list
        # Time Complexity: O(N^2), Auxiliary Space: O(1)
        """Fisher-Yates-Shuffle(A):
            n = length of array A
            for i from n - 1 down to 1:
            j = random integer such that 0 <= j <= i
            swap A[i] and A[j]"""
        if not self.head:
            print(self.name," is empty!")
            return
        #Can't shuffle 1 item playlist
        if self.head.next == self.head:
            return
        
        len = self.length
        ith = self.head.prev
        for i in range(len - 1, 0, -1):
            # Generate a random index within the remaining elements
            j = randint(0, i)

            # Move to the jth node
            jth = self.traverse(j)

            # Swap values of ith and jth
            ith.name, jth.name = jth.name, ith.name
            ith.album, jth.album = jth.album, ith.album
            ith.length, jth.length = jth.length, ith.length

            # Move ith back one and jth back to head
            ith = ith.prev
    
    def shuffle(self):
        # Fisher-Yates Shuffle Algorithm: Convert linked list to array, shuffle, convert back
        # Time Complexity: O(N), Auxiliary Space: O(N) -> Have to create new array
        if not self.head:
            print(self.name," is empty!")
            return
        #Can't shuffle 1 item playlist
        if self.head.next == self.head:
            return

        # Add all of the tracks to an array
        tracks = []
        current = self.head
        while True:
            tracks.append(current)
            current = current.next
            if current == self.head:
                break

        n = self.length
        # Shuffle the track. random.shuffle uses Fisher-Yates 
        for i in range(n-1,0,-1):
            # random.randint uses Mersenne Twister which is O(1) (https://stackoverflow.com/questions/25651532/what-is-the-time-complexity-of-the-mersenne-twister)
            j = randint(0,i+1)
    
            # Swap arr[i] with the element at random index
            tracks[i],tracks[j] = tracks[j],tracks[i]

        # Convert back to circular doubly linked list
        self.head = tracks[0]
        for i in range(n):
            #prev_index = (i - 1) % n if i != 0 else n - 1
            tracks[i].prev = tracks[i-1]
            tracks[i].next = tracks[(i + 1) % n]

if __name__ == '__main__':
    playlist = Playlist("test_playlist")
    playlist.insert_at_beginning("artist1","album1",120)
    playlist.insert_at_end("artist3","album3",100)
    playlist.insert_at_index(1,"artist2","album2",210)
    playlist.insert_at_index(3,"artist4","album4",40)
    playlist.insert_at_end("artist5","album5",13)
    #artist1,artist2,artist3,artist4
    #playlist.contents()
    print(playlist.traverse(0))
    print(playlist.traverse(1))
    print(playlist.traverse(2))
    print(playlist.traverse(3))
    print(playlist.traverse(4))

    #playlist.delete_at_index(2)
    #artist1,artist2,artist4
    #playlist.contents()

    print("--------------------------")
    #print(playlist.length)
    playlist.move(old_index=3,new_index=1)
    #artists1,artist4,artist2
    playlist.contents()

    #print("Duration:",playlist.duration,"seconds")

    #print("---------------------------")
    #playlist.clear()
    #playlist.sort_by_length()
    #playlist.contents()
    #print("---------------------------")

    #playlist.sort_by_artist()
    #playlist.contents()
    #print("---------------------------")

    #playlist.sort_by_album()
    #playlist.contents()
    #playlist.now_playing()
    #print("---------------------------")
    #playlist.shuffle()
    #playlist.contents()