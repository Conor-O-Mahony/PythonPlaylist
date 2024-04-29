class Track:
    def __init__(self,name,album,length):
        self.name = name
        self.album = album
        self.length = length

        self.next = None

    def __repr__(self):
        return f"Track(name={self.name},album={self.album},length={self.length})"
        
    def __str__(self):
        return f"Name: {self.name}, Album: {self.album}, Duration: {self.length} seconds"