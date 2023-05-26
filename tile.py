class Tile:

    def __init__(self, moveable, name, up, down, left, right, position):
        self.moveable = moveable
        self.name = name
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.position = position
    
    def __str__(self):
        return str(self.name + " at " + str(self.position))

    def change_position(self, new_position):
        self.position = new_position        