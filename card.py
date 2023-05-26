class Card:

    def __init__(self, visited, name):
        self.visited = visited
        self.name = name

    def __str__(self):
        return str(self.name)
    
    def change_visited(self, new_visited):
        self.visited = new_visited