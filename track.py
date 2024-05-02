class Track:
    def __init__(self,name,album,length):
        self.name = name
        self.album = album
        self.length = length

        #Pointer to next track
        self.next = None
        #Pointer to previous track
        self.prev = None

    def compare_attributes(obj1, obj2, attr):
        if getattr(obj1, attr) < getattr(obj2, attr):
            return True
        return False
        
    def attribute_exists(obj, attr):
         try:
              getattr(obj, attr)
              return True
         except:
              return False

    def __repr__(self):
        return f"Track(name={self.name},album={self.album},length={self.length})"
        
    def __str__(self):
        return f"Name: {self.name}, Album: {self.album}, Duration: {self.length} seconds"