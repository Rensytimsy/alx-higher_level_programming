class MyList(list):
    """This is MyList class that inherits from list class"""
    def __init__(self):
        """Using the super and init to access all values present """
        super().__init__()
    
    def print_sorted(self):
        """The code below returns an arrnged list from small to big numbers"""
        print(sorted(self))
